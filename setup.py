"""
DECIMA - Data Extraction & Contextual Inference for MCNP Analysis

This setup.py provides pip installation with automatic mcnptoolspro compilation.
It builds the mcnptoolspro C++ extension using CMake and installs the DECIMA package.
mcnptoolspro is an enhanced version of mcnptools with complete MCNP 6.2/6.3 filter support.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from setuptools.command.develop import develop
from setuptools.command.install import install


class CMakeBuild(build_ext):
    """Custom build extension that uses CMake to compile mcnptoolspro C++ code"""

    def run(self):
        # Check CMake is installed
        try:
            subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError(
                "CMake must be installed to build mcnptoolspro. "
                "Install it with: pip install cmake"
            )

        # Build each extension
        for ext in self.extensions:
            self.build_cmake(ext)

    def build_cmake(self, ext):
        """Run CMake build process for mcnptoolspro"""

        # Paths
        script_dir = Path(__file__).parent.absolute()
        mcnptools_source_dir = script_dir / 'mcnptoolspro'
        mcnptools_build_dir = mcnptools_source_dir / 'build'
        mcnptools_python_dir = mcnptools_source_dir / 'python' / 'mcnptoolspro'

        # Check if mcnptoolspro directory exists
        if not mcnptools_source_dir.exists():
            raise RuntimeError(
                f"\n"
                f"=" * 70 + "\n"
                f"ERROR: mcnptoolspro source directory not found at {mcnptools_source_dir}\n"
                f"\n"
                f"Please ensure the mcnptoolspro/ directory exists in the DECIMA repository.\n"
                f"=" * 70
            )

        # Check if CMakeLists.txt exists
        if not (mcnptools_source_dir / 'CMakeLists.txt').exists():
            raise RuntimeError(
                f"\n"
                f"=" * 70 + "\n"
                f"ERROR: CMakeLists.txt not found in {mcnptools_source_dir}\n"
                f"=" * 70
            )

        # Create build directory
        mcnptools_build_dir.mkdir(exist_ok=True)

        print(f"\n{'='*70}")
        print(f"Building mcnptoolspro C++ extension...")
        print(f"  Source: {mcnptools_source_dir}")
        print(f"  Build:  {mcnptools_build_dir}")
        print(f"{'='*70}\n")

        # CMake configure
        print(f"[1/3] Configuring CMake...")
        cmake_args = [
            'cmake',
            '-S', str(mcnptools_source_dir),
            '-B', str(mcnptools_build_dir),
            '-DCMAKE_BUILD_TYPE=Release',
            '-DBUILD_TESTING=OFF',  # Skip tests
        ]

        # Add platform-specific args
        if sys.platform.startswith('win'):
            # Windows: Use Visual Studio generator
            cmake_args.extend([
                '-G', 'Visual Studio 17 2022',
                '-A', 'x64',
            ])

        try:
            subprocess.check_call(cmake_args, cwd=str(mcnptools_build_dir))
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"CMake configuration failed: {e}")

        # CMake build
        print(f"\n[2/3] Building with CMake (this may take a few minutes)...")
        build_args = [
            'cmake',
            '--build', str(mcnptools_build_dir),
            '--config', 'Release',
            '--target', '_mcnptools_wrap',
            '-j', str(os.cpu_count() or 4)
        ]

        try:
            subprocess.check_call(build_args)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"CMake build failed: {e}")

        # Copy compiled wrapper to package directory
        print(f"\n[3/3] Copying compiled wrapper to package...")

        if sys.platform.startswith('win'):
            # Windows: .pyd file
            wrapper_src = mcnptools_build_dir / 'python' / 'mcnptoolspro' / 'Release' / '_mcnptools_wrap.pyd'
            wrapper_name = '_mcnptools_wrap.pyd'
        else:
            # Linux/Mac: .so file
            wrapper_src = mcnptools_build_dir / 'python' / 'mcnptoolspro' / '_mcnptools_wrap.so'
            wrapper_name = '_mcnptools_wrap.so'

        if not wrapper_src.exists():
            raise RuntimeError(
                f"Compiled wrapper not found at {wrapper_src}\n"
                f"Build may have failed. Check CMake output above."
            )

        # Copy to mcnptools package directory
        wrapper_dst = mcnptools_python_dir / wrapper_name
        shutil.copy(str(wrapper_src), str(wrapper_dst))
        print(f"[OK] Copied {wrapper_src.name} -> {wrapper_dst}")

        # Also copy to build lib directory for wheel packaging
        ext_path = Path(self.get_ext_fullpath(ext.name))
        ext_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(str(wrapper_src), str(ext_path))
        print(f"[OK] Copied {wrapper_src.name} -> {ext_path}")

        # Copy HDF5 DLLs on Windows
        if sys.platform.startswith('win'):
            self._copy_hdf5_dlls(mcnptools_python_dir)

        print(f"\n{'='*70}")
        print(f"mcnptoolspro build completed successfully!")
        print(f"{'='*70}\n")

    def _copy_hdf5_dlls(self, target_dir):
        """Copy HDF5 DLLs to mcnptools package on Windows"""
        print("\n[4/4] Copying HDF5 DLLs...")

        # Common HDF5 installation paths on Windows
        hdf5_paths = [
            Path(r"C:\Program Files\HDF_Group\HDF5\1.14.6\bin"),
            Path(r"C:\Program Files\HDF_Group\HDF5\1.14.5\bin"),
            Path(r"C:\Program Files\HDF_Group\HDF5\1.14.4\bin"),
            Path(r"C:\Program Files\HDF_Group\HDF5\1.14\bin"),
            Path(r"C:\Program Files (x86)\HDF_Group\HDF5\1.14.6\bin"),
            Path(r"C:\HDF5\bin"),
        ]

        # Also check PATH environment
        path_dirs = os.environ.get('PATH', '').split(';')
        for path_dir in path_dirs:
            if 'hdf5' in path_dir.lower() or 'hdf' in path_dir.lower():
                hdf5_paths.append(Path(path_dir))

        # Required DLL files
        required_dlls = ['hdf5.dll', 'hdf5_cpp.dll', 'hdf5_hl.dll']
        dlls_found = {}

        # Search for DLLs
        for hdf5_path in hdf5_paths:
            if not hdf5_path.exists():
                continue

            for dll_name in required_dlls:
                dll_file = hdf5_path / dll_name
                if dll_file.exists() and dll_name not in dlls_found:
                    dlls_found[dll_name] = dll_file

            # If we found all DLLs, stop searching
            if len(dlls_found) == len(required_dlls):
                break

        # Copy found DLLs
        copied_count = 0
        for dll_name, dll_src in dlls_found.items():
            dll_dst = target_dir / dll_name
            try:
                shutil.copy(str(dll_src), str(dll_dst))
                print(f"[OK] Copied {dll_name}")
                copied_count += 1
            except Exception as e:
                print(f"[WARN] Could not copy {dll_name}: {e}")

        if copied_count == 0:
            print(f"\n[WARN] No HDF5 DLLs found in common locations.")
            print(f"       mcnptoolspro may fail to import.")
            print(f"       Please install HDF5 from: https://www.hdfgroup.org/downloads/hdf5/")
            print(f"       Or manually copy DLLs to: {target_dir}")
        elif copied_count < len(required_dlls):
            print(f"\n[WARN] Only {copied_count}/{len(required_dlls)} DLLs copied.")
            print(f"       Missing: {set(required_dlls) - set(dlls_found.keys())}")
        else:
            print(f"[OK] All {copied_count} HDF5 DLLs copied successfully")


# Custom install command that builds mcnptoolspro first
class CustomInstall(install):
    def run(self):
        self.run_command('build_ext')
        install.run(self)


# Custom develop command that builds mcnptoolspro first
class CustomDevelop(develop):
    def run(self):
        self.run_command('build_ext')
        develop.run(self)


# Read version from pyproject.toml or default
def get_version():
    """Extract version from pyproject.toml or use default"""
    pyproject_file = Path(__file__).parent / 'pyproject.toml'

    if pyproject_file.exists():
        with open(pyproject_file, 'r') as f:
            for line in f:
                if line.strip().startswith('version'):
                    # Extract version from: version = "1.2.0"
                    import re
                    match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', line)
                    if match:
                        return match.group(1)

    return '1.2.0'


# Read long description from README
def get_long_description():
    """Get long description from README"""
    readme_path = Path(__file__).parent / 'README.md'

    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "Data Extraction & Contextual Inference for MCNP Analysis"


setup(
    name='decima',
    version=get_version(),

    author='Quentin Ducasse, Feda Almuhisen',
    author_email='quentin.ducasse@gmail.com',

    description='Data Extraction & Contextual Inference for MCNP Analysis',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',

    url='https://github.com/quentinducasse/decima',
    project_urls={
        'Bug Tracker': 'https://github.com/quentinducasse/decima/issues',
        'Documentation': 'https://github.com/quentinducasse/decima/tree/main/doc',
        'Source Code': 'https://github.com/quentinducasse/decima',
    },

    # Main DECIMA packages
    packages=find_packages(include=['modules', 'modules.*', 'kg', 'kg.*', 'utils', 'utils.*', 'tools', 'tools.*', 'frontend', 'frontend.*'])
    + ['mcnptoolspro'],  # Add mcnptoolspro package

    package_dir={
        'mcnptoolspro': 'mcnptoolspro/python/mcnptoolspro',
    },

    include_package_data=True,

    # Include compiled mcnptoolspro extension and Python files
    package_data={
        'mcnptoolspro': [
            '*.pyd',  # Windows compiled extension
            '*.so',   # Linux/Mac compiled extension
            '*.dll',  # Windows DLL dependencies
            '*.py',
        ],
        'frontend': ['static/**/*', 'templates/**/*'],
    },

    # mcnptoolspro extension (built by CMake)
    ext_modules=[Extension('mcnptoolspro._mcnptools_wrap', sources=[])],
    cmdclass={
        'build_ext': CMakeBuild,
        'install': CustomInstall,
        'develop': CustomDevelop,
    },

    # Requirements
    python_requires='>=3.10',
    install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.9.0",
        "blinker==1.9.0",
        "certifi==2025.4.26",
        "charset-normalizer==3.4.2",
        "click==8.2.1",
        "colorama==0.4.6",
        "contourpy==1.3.2",
        "cycler==0.12.1",
        "Flask==3.1.1",
        "flask-cors==6.0.1",
        "fonttools==4.58.5",
        "h11==0.16.0",
        "httpcore==1.0.9",
        "httpx==0.28.1",
        "idna==3.10",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.6",
        "jiter==0.10.0",
        "jsonpatch==1.33",
        "jsonpointer==3.0.0",
        "kiwisolver==1.4.8",
        "langchain-core==0.3.61",
        "langgraph==0.4.7",
        "langgraph-checkpoint==2.0.26",
        "langsmith==0.3.42",
        "MarkupSafe==3.0.2",
        "matplotlib==3.10.3",
        "neo4j==5.28.1",
        "numpy==2.2.6",
        "openai==1.82.0",
        "orjson==3.10.18",
        "ormsgpack==1.9.1",
        "packaging==24.2",
        "pillow==11.3.0",
        "pydantic==2.11.5",
        "pydantic_core==2.33.2",
        "pyparsing==3.2.3",
        "python-dateutil==2.9.0.post0",
        "python-dotenv==1.1.1",
        "pytz==2025.2",
        "PyYAML==6.0.2",
        "requests==2.32.3",
        "requests-toolbelt==1.0.0",
        "six==1.17.0",
        "sniffio==1.3.1",
        "tenacity==9.1.2",
        "termcolor==3.1.0",
        "tqdm==4.67.1",
        "typing_extensions==4.13.2",
        "urllib3==2.4.0",
        "Werkzeug==3.1.3",
        "xxhash==3.5.0",
        "zstandard==0.23.0",
    ],

    # Extras for development and building
    extras_require={
        'dev': [
            'pytest>=8.3.5',
            'pre-commit>=4.2.0',
        ],
        'build': [
            'cmake>=3.13',
            'build',
            'twine',
        ]
    },

    # Metadata
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: C++',
        'Operating System :: OS Independent',
    ],

    keywords='mcnp ptrac monte-carlo nuclear-physics llm knowledge-graph',

    # Not zip-safe because of compiled extension
    zip_safe=False,
)
