cmake_minimum_required(VERSION 3.9)
project(graph_code)
set(CMAKE_CXX_STANDARD 17)

# Check for OpenMP
find_package(OpenMP REQUIRED)

# these compiler flags are not valid for all compilers (not portable!)
set(CMAKE_CXX_FLAGS "-Ofast -std=c++11 -fopenmp -march=native")

# create a variable with all your source files
set(SOURCE_FILES main_graph.cpp)

# create executable with name pi
add_executable(graph_code ${SOURCE_FILES})

# Hinzufügen von OpenMP
target_link_libraries(graph_code PUBLIC OpenMP::OpenMP_CXX)