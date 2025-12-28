#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mcnptools::mcnptools_boost" for configuration "Debug"
set_property(TARGET mcnptools::mcnptools_boost APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(mcnptools::mcnptools_boost PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/mcnptools_boost.lib"
  )

list(APPEND _cmake_import_check_targets mcnptools::mcnptools_boost )
list(APPEND _cmake_import_check_files_for_mcnptools::mcnptools_boost "${_IMPORT_PREFIX}/lib/mcnptools_boost.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
