"""
eoutils.py — Earth Observation Utility Functions

This script provides a collection of simple geospatial utility functions 
commonly used in Earth Observation (EO) data processing workflows. It is 
intended as part of an assignment (A4) to demonstrate basic functionality 
such as spectral index calculation, raster clipping, and coordinate conversion.

Functions:
- calculate_ndvi(): Calculate NDVI from NIR and Red band arrays.
- clip_raster_to_bounds(): Clip a raster file to a bounding box and save the output.
- latlon_to_utm(): Convert latitude and longitude to UTM coordinates.

Usage:
Import this script as a module in your Jupyter notebook or Python script:
    
    from eoutils import calculate_ndvi, clip_raster_to_bounds, latlon_to_utm
"""

import numpy as np
import rasterio
from rasterio.windows import from_bounds
from pyproj import Proj, Transformer

def calculate_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """
    Calculate the Normalized Difference Vegetation Index (NDVI).

    Args:
        nir (np.ndarray): Near-infrared band array.
        red (np.ndarray): Red band array.

    Returns:
        np.ndarray: NDVI values ranging from -1 to 1.
    """
    ndvi = (nir.astype(float) - red.astype(float)) / (nir + red + 1e-6)
    return np.clip(ndvi, -1, 1)

def clip_raster_to_bounds(raster_path: str, bounds: tuple, output_path: str):
    """
    Clip a raster to given bounding box coordinates and save the result.

    Args:
        raster_path (str): Path to input raster file.
        bounds (tuple): Bounding box in the form (minx, miny, maxx, maxy).
        output_path (str): Path to save the clipped raster.
    """
    with rasterio.open(raster_path) as src:
        window = from_bounds(*bounds, src.transform)
        kwargs = src.meta.copy()
        kwargs.update({
            'height': window.height,
            'width': window.width,
            'transform': rasterio.windows.transform(window, src.transform)
        })

        with rasterio.open(output_path, 'w', **kwargs) as dst:
            dst.write(src.read(window=window))

def latlon_to_utm(lat: float, lon: float) -> tuple:
    """
    Convert geographic coordinates (latitude, longitude) to UTM coordinates.

    Args:
        lat (float): Latitude in decimal degrees.
        lon (float): Longitude in decimal degrees.

    Returns:
        tuple: (easting, northing, utm_zone)
    """
    # Calculate the UTM zone number based on longitude
    utm_zone = int((lon + 180) / 6) + 1

    # Define the UTM projection string for the calculated zone (WGS84 datum)
    proj_str = f"+proj=utm +zone={utm_zone} +datum=WGS84 +units=m +no_defs"

    # Create a transformer object to convert from geographic (lat/lon) to UTM
    transformer = Transformer.from_crs("epsg:4326", proj_str, always_xy=True)

    # Perform the transformation: note that 'always_xy=True' means input is (lon, lat)
    easting, northing = transformer.transform(lon, lat)
    
    return easting, northing, utm_zone
