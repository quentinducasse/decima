#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mcnptools::mcnptools_boost" for configuration "Release"
set_property(TARGET mcnptools::mcnptools_boost APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(mcnptools::mcnptools_boost PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/mcnptools_boost.lib"
  )

list(APPEND _cmake_import_check_targets mcnptools::mcnptools_boost )
list(APPEND _cmake_import_check_files_for_mcnptools::mcnptools_boost "${_IMPORT_PREFIX}/lib/mcnptools_boost.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
