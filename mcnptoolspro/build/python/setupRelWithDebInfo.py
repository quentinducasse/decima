import os
import re
import sys
import platform
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['C:/Program Files/CMake/bin/cmake.exe', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        build_args = ['--config', 'RelWithDebInfo', '--target', '_mcnptools_wrap']

        subprocess.check_call(['C:/Program Files/CMake/bin/cmake.exe', '--build', 'C:/Users/qduca/OneDrive/Applications/DECIMA_v2/mcnptoolspro/build'] + build_args)

def internalize_libs():
    '''This function internalizes the HDF5 dynamic library to permit
    packaging/installation for Python 3.8 and later, which changes the library
    search procedure as documented at:
    https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew'''

    if os.name == 'nt':
        import shutil
        dlls = "C:/Python313/python313.dll;C:/Program Files/HDF_Group/HDF5/1.14.6/bin/hdf5.dll".split(";")
        for dll in dlls:
            if "hdf5" in dll.lower():
                assert(os.path.isfile(dll))
                shutil.copy(dll, os.path.join("mcnptoolspro"))

internalize_libs()

setup(
    name='mcnptoolspro',
    version='5.3.1',
    description = 'mcnptoolspro - enhanced tools for manipulating mcnp output with filter support',
    author = ['Clell J. (CJ) Solomon', 'Cameron Bates', 'Joel Kulesza', 'DECIMA Pro'],
    author_email = ['csolomon@lanl.gov', 'batesca@lanl.gov, jkulesza@lanl.gov'],
    packages=['mcnptoolspro'],
    package_data={'mcnptoolspro' : ['_mcnptools_wrap.pyd', "*.dll"]},
    test_suite='mcnptools_tests',
    ext_modules=[CMakeExtension('mcnptoolspro._mcnptools_wrap')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)
