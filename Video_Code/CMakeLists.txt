cmake_minimum_required(VERSION 3.9)
project(video_code)
set(CMAKE_CXX_STANDARD 17)

# these compiler flags are not valid for all compilers (not portable!)
set(CMAKE_CXX_FLAGS "-Ofast -std=c++11 -fopenmp -march=native")

# create a variable with all your source files
set(SOURCE_FILES main_video.cpp)

# create executable with name pi
add_executable(video_code ${SOURCE_FILES})

