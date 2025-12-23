"""
Fractal Pattern Generation Module
Generates various fractal patterns including Mandelbrot and Julia sets.
"""

import numpy as np
from typing import Tuple


def mandelbrot(width: int = 800, height: int = 600, 
               max_iter: int = 100, 
               bounds: Tuple[float, float, float, float] = (-2.5, 1.0, -1.0, 1.0)) -> np.ndarray:
    """
    Generate a Mandelbrot set fractal.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        max_iter: Maximum number of iterations
        bounds: (xmin, xmax, ymin, ymax) coordinate bounds
        
    Returns:
        2D numpy array representing the fractal
    """
    xmin, xmax, ymin, ymax = bounds
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    
    Z = np.zeros_like(C, dtype=complex)
    M = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        M[mask] = i
    
    return M


def julia(width: int = 800, height: int = 600,
          c: complex = -0.4 + 0.6j,
          max_iter: int = 100,
          bounds: Tuple[float, float, float, float] = (-2.0, 2.0, -1.5, 1.5)) -> np.ndarray:
    """
    Generate a Julia set fractal.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        c: Complex constant parameter
        max_iter: Maximum number of iterations
        bounds: (xmin, xmax, ymin, ymax) coordinate bounds
        
    Returns:
        2D numpy array representing the fractal
    """
    xmin, xmax, ymin, ymax = bounds
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    M = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c
        M[mask] = i
    
    return M


def burning_ship(width: int = 800, height: int = 600,
                 max_iter: int = 100,
                 bounds: Tuple[float, float, float, float] = (-2.0, 1.0, -2.0, 1.0)) -> np.ndarray:
    """
    Generate a Burning Ship fractal.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        max_iter: Maximum number of iterations
        bounds: (xmin, xmax, ymin, ymax) coordinate bounds
        
    Returns:
        2D numpy array representing the fractal
    """
    xmin, xmax, ymin, ymax = bounds
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    
    Z = np.zeros_like(C, dtype=complex)
    M = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = (np.abs(Z[mask].real) + 1j * np.abs(Z[mask].imag))**2 + C[mask]
        M[mask] = i
    
    return M
