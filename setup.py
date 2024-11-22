#! usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="ATL11-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'os', 'sys', 'h5py', 'configparser', 'json', 'pyogrio', 'numpy', 'pandas', 
        'geopandas', 'xarray', 'rasterio', 'shapely', 'datetime', 'time', 'matplotlib', 
        'cmcrameri', 'contextily', 'earthpy', 'utils', 'traceback'
    ],
)