cmake_minimum_required(VERSION 3.15)
project(pyroms Fortran)

# Set the build type to Release for optimized builds
set(CMAKE_BUILD_TYPE Release)

# Include Fortran extensions
add_library(_interp MODULE pyroms/src/interp.f)
add_library(_obs_interp MODULE pyroms/src/obs_interp.f)
add_library(_remapping MODULE pyroms/src/remapping.f)
add_library(_remapping_fast MODULE pyroms/src/remapping_fast.f)
add_library(_remapping_fast_weighted MODULE pyroms/src/remapping_fast_weighted.f)
add_library(_iso MODULE pyroms/src/iso.f)

# Link the extensions with necessary libraries (if needed)
# target_link_libraries(_interp <necessary_libs>)
# target_link_libraries(_obs_interp <necessary_libs>)
# Add more target_link_libraries calls as needed

# Ensure libraries are installed into the Python package
install(TARGETS _interp _obs_interp _remapping _remapping_fast _remapping_fast_weighted _iso
        LIBRARY DESTINATION pyroms)
