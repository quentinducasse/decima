#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mcnptools" for configuration "Release"
set_property(TARGET mcnptools APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mcnptools PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/mcnptools.lib"
  )

list(APPEND _cmake_import_check_targets mcnptools )
list(APPEND _cmake_import_check_files_for_mcnptools "${_IMPORT_PREFIX}/lib/mcnptools.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
