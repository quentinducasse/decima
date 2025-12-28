include(CMakeFindDependencyMacro)

if( 0 )
  list(APPEND boost_components "regex")
endif()

if(  )
  list(APPEND boost_components "serialization")
endif()

if(  )
  list(APPEND boost_components "mpi")
endif()

if( boost_components )
  find_dependency(Boost 1.60 COMPONENTS "${boost_components}")
else()
  find_dependency(mcnptools_boost)
endif()

if(  )
  find_dependency(MPI)
endif()

if( NOT DEFINED shacl::F5_CXX )
  find_dependency(shacl-F5_CXX HINTS "${CMAKE_CURRENT_LIST_DIR}/../")
endif()

include("${CMAKE_CURRENT_LIST_DIR}/mcnptoolsTargets.cmake")
