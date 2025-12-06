"""
Parametric Curve Pattern Generation Module
Generates patterns based on parametric equations.
"""

import numpy as np
from typing import Tuple


def lissajous(width: int = 800, height: int = 600,
              a: int = 3, b: int = 4,
              delta: float = np.pi/2,
              num_points: int = 10000,
              thickness: float = 2.0) -> np.ndarray:
    """
    Generate Lissajous curve pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        a: Frequency of x oscillation
        b: Frequency of y oscillation
        delta: Phase difference
        num_points: Number of points to sample
        thickness: Line thickness
        
    Returns:
        2D numpy array representing the pattern
    """
    t = np.linspace(0, 2 * np.pi, num_points)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    
    # Scale to image dimensions
    x = ((x + 1) / 2 * (width - 40) + 20).astype(int)
    y = ((y + 1) / 2 * (height - 40) + 20).astype(int)
    
    # Create image
    pattern = np.zeros((height, width))
    
    # Draw curve with thickness
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        if 0 <= xi < width and 0 <= yi < height:
            # Add thickness around each point
            y_range = slice(max(0, yi - int(thickness)), min(height, yi + int(thickness) + 1))
            x_range = slice(max(0, xi - int(thickness)), min(width, xi + int(thickness) + 1))
            pattern[y_range, x_range] = 1
    
    return pattern


def rose_curve(width: int = 800, height: int = 600,
               n: int = 5, d: int = 4,
               num_points: int = 10000,
               thickness: float = 2.0) -> np.ndarray:
    """
    Generate rose curve (rhodonea) pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        n: Numerator of petal count factor
        d: Denominator of petal count factor
        num_points: Number of points to sample
        thickness: Line thickness
        
    Returns:
        2D numpy array representing the pattern
    """
    t = np.linspace(0, 2 * np.pi * d, num_points)
    k = n / d
    r = np.cos(k * t)
    
    # Convert to Cartesian
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    # Scale to image dimensions
    scale = min(width, height) * 0.4
    x = (x * scale + width / 2).astype(int)
    y = (y * scale + height / 2).astype(int)
    
    # Create image
    pattern = np.zeros((height, width))
    
    # Draw curve with thickness
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        if 0 <= xi < width and 0 <= yi < height:
            y_range = slice(max(0, yi - int(thickness)), min(height, yi + int(thickness) + 1))
            x_range = slice(max(0, xi - int(thickness)), min(width, xi + int(thickness) + 1))
            pattern[y_range, x_range] = 1
    
    return pattern


def hypotrochoid(width: int = 800, height: int = 600,
                 R: float = 100, r: float = 50, d: float = 70,
                 num_points: int = 10000,
                 thickness: float = 2.0) -> np.ndarray:
    """
    Generate hypotrochoid (spirograph) pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        R: Radius of fixed circle
        r: Radius of rolling circle
        d: Distance of pen point from center of rolling circle
        num_points: Number of points to sample
        thickness: Line thickness
        
    Returns:
        2D numpy array representing the pattern
    """
    t = np.linspace(0, 2 * np.pi * r / np.gcd(int(R), int(r)), num_points)
    
    x = (R - r) * np.cos(t) + d * np.cos((R - r) / r * t)
    y = (R - r) * np.sin(t) - d * np.sin((R - r) / r * t)
    
    # Scale to image dimensions
    max_val = max(np.abs(x).max(), np.abs(y).max())
    scale = min(width, height) * 0.4 / max_val
    x = (x * scale + width / 2).astype(int)
    y = (y * scale + height / 2).astype(int)
    
    # Create image
    pattern = np.zeros((height, width))
    
    # Draw curve with thickness
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        if 0 <= xi < width and 0 <= yi < height:
            y_range = slice(max(0, yi - int(thickness)), min(height, yi + int(thickness) + 1))
            x_range = slice(max(0, xi - int(thickness)), min(width, xi + int(thickness) + 1))
            pattern[y_range, x_range] = 1
    
    return pattern


def butterfly_curve(width: int = 800, height: int = 600,
                   num_points: int = 10000,
                   thickness: float = 2.0) -> np.ndarray:
    """
    Generate butterfly curve pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        num_points: Number of points to sample
        thickness: Line thickness
        
    Returns:
        2D numpy array representing the pattern
    """
    t = np.linspace(0, 12 * np.pi, num_points)
    
    # Butterfly curve equation
    r = np.exp(np.sin(t)) - 2 * np.cos(4 * t) + np.sin((2 * t - np.pi) / 24)**5
    
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    # Scale to image dimensions
    max_val = max(np.abs(x).max(), np.abs(y).max())
    scale = min(width, height) * 0.3 / max_val
    x = (x * scale + width / 2).astype(int)
    y = (y * scale + height / 2).astype(int)
    
    # Create image
    pattern = np.zeros((height, width))
    
    # Draw curve with thickness
    for i in range(len(x)):
        xi, yi = x[i], y[i]
        if 0 <= xi < width and 0 <= yi < height:
            y_range = slice(max(0, yi - int(thickness)), min(height, yi + int(thickness) + 1))
            x_range = slice(max(0, xi - int(thickness)), min(width, xi + int(thickness) + 1))
            pattern[y_range, x_range] = 1
    
    return pattern
