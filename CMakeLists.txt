cmake_minimum_required(VERSION 3.9)
project(Beispiel)
set(CMAKE_CXX_STANDARD 17)
set(SOURCE_FILES main.cpp)

# these compiler flags are not valid for all compilers (not portable!)
set(CMAKE_CXX_FLAGS "-Ofast -std=c++11 -fopenmp -march=native")

# create executable with name pi
add_executable(Beispiel ${SOURCE_FILES})

