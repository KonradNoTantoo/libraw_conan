cmake_minimum_required(VERSION 3.2)
project(libraw LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(libraw_SOURCES
    "internal/dcraw_common.cpp"
    "internal/dcraw_fileio.cpp"
    "internal/demosaic_packs.cpp"
    "src/libraw_cxx.cpp"
    "src/libraw_c_api.cpp"
    "src/libraw_datastream.cpp"
)

include_directories(".")
add_library(libraw SHARED ${libraw_SOURCES})

if(MSVC)
    target_compile_definitions(libraw PUBLIC WIN32 LIBRAW_BUILDLIB _CRT_SECURE_NO_WARNINGS)
endif(MSVC)
