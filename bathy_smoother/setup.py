"""
bathy_smoother is a suite of tools for working with ROMS bathymetry.
(ripped from matlab script LP_bathymetry)

Requires:
    NumPy (http://numpy.scipy.org)
    lpsolve (http://lpsolve.sourceforge.net/)

Contains:
    bathy_smoothing - Tools for smoothing the bathymetry

    bathy_tools - Various bathymetry tools

    LP_bathy_smoothing - Tools for smoothing the bathymetry using LP

    LP_bathy_tools - LP tools for smoothing the bathymetry

    LP_tools - Various LP tools
"""

from setuptools import setup, find_packages

doclines = __doc__.split("\n")

setup(
    name='bathy_smoother',
    version='0.2.0',
    description=doclines[0],
    long_description="\n".join(doclines[2:]),
    url='https://github.com/ESMG/pyroms',
    license='BSD',
    platforms=["any"],
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        'numpy',  # Add any other dependencies here
    ],
)
