#!/usr/bin/env python

"""
pyroms_toolbox is a suite of tools for working with ROMS.

Requires:
    pyroms (https://github.com/ESMG/pyroms)

Contains:
    many things...

"""

from setuptools import setup, Extension, find_packages

# # Define the extension modules
# average = Extension(
#     name='_average',
#     sources=['pyroms_toolbox/src/average.f90'],
#     extra_f77_compile_args=['-O2'],  # Example of adding optimization flags
# )

# creep = Extension(
#     name='creep',
#     sources=['pyroms_toolbox/src/creeping_sea.f90']
# )

# move_river = Extension(
#     name='_move_river_t',
#     sources=['pyroms_toolbox/src/move_river_t.f90']
# )

# move_runoff = Extension(
#     name='_move_runoff',
#     sources=['pyroms_toolbox/src/move_runoff.f90']
# )

doclines = __doc__.split("\n")

if __name__ == '__main__':
    setup(
        name="pyroms_toolbox",
        version='0.2.0',
        description=doclines[0],
        long_description="\n".join(doclines[2:]),
        author="ESMG",
        url='https://github.com/ESMG/pyroms',
        license='BSD',
        platforms=["any"],
        packages=find_packages(),  # Automatically find packages
        # ext_modules=[average, creep, move_river, move_runoff],
        install_requires=[
            'pyroms',  # Add any other dependencies here
        ],
    )
