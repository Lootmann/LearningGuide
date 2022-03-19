set(CMAKE_VERBOSE_MAKEFILE 1)
cmake_minimum_required(VERSION 3.12)

project(PROJECT CXX)
set(CMAKE_CXX_FLAGS
  "-std=c++17 -Wall -Wextra --pedantic-errors"
  )

# gtest suite
enable_testing()

add_subdirectory(src)
add_subdirectory(test)

add_executable(a.out main.cpp)
target_link_libraries(a.out Lib)
