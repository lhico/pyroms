cmake_minimum_required(VERSION 3.15)

project(bathy_smoother)

find_package(PythonLibs REQUIRED)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
find_package(NumPy REQUIRED)


include_directories(${NUMPY_INCLUDE_DIRS})

# Add your source files here
add_library(bathy_smoother src/your_source_file.cpp)

# Link against Python libraries
target_link_libraries(bathy_smoother ${PYTHON_LIBRARIES})
