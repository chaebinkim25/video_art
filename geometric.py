"""
Geometric Pattern Generation Module
Generates various geometric patterns including spirals and tessellations.
"""

import numpy as np
from typing import Tuple


def spiral(width: int = 800, height: int = 600,
           spiral_type: str = 'archimedean',
           turns: int = 10,
           thickness: float = 2.0) -> np.ndarray:
    """
    Generate spiral patterns.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        spiral_type: Type of spiral ('archimedean', 'logarithmic', 'fermat')
        turns: Number of spiral turns
        thickness: Line thickness
        
    Returns:
        2D numpy array representing the pattern
    """
    y, x = np.ogrid[:height, :width]
    cx, cy = width // 2, height // 2
    
    # Convert to polar coordinates
    r = np.sqrt((x - cx)**2 + (y - cy)**2)
    theta = np.arctan2(y - cy, x - cx)
    theta = (theta + np.pi) % (2 * np.pi)  # Normalize to [0, 2π]
    
    if spiral_type == 'archimedean':
        # r = a + b * theta
        expected_r = (theta / (2 * np.pi)) * (min(width, height) / 4) * (turns / 10)
    elif spiral_type == 'logarithmic':
        # r = a * e^(b * theta)
        b = 0.2
        expected_r = 10 * np.exp(b * theta * turns / 10)
    elif spiral_type == 'fermat':
        # r = a * sqrt(theta)
        expected_r = np.sqrt(theta * turns) * (min(width, height) / 20)
    else:
        expected_r = (theta / (2 * np.pi)) * (min(width, height) / 4) * (turns / 10)
    
    # Create the spiral pattern
    pattern = np.abs(r - expected_r) < thickness
    return pattern.astype(float)


def voronoi_cells(width: int = 800, height: int = 600,
                  num_points: int = 50,
                  seed: int = 42) -> np.ndarray:
    """
    Generate Voronoi cell pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        num_points: Number of Voronoi seed points
        seed: Random seed for reproducibility
        
    Returns:
        2D numpy array representing the pattern
    """
    np.random.seed(seed)
    points = np.random.rand(num_points, 2) * [width, height]
    
    y, x = np.ogrid[:height, :width]
    coords = np.stack([x, y], axis=-1)
    
    # Calculate distances to all points
    distances = np.zeros((height, width, num_points))
    for i, point in enumerate(points):
        distances[:, :, i] = np.sqrt((coords[:, :, 0] - point[0])**2 + 
                                     (coords[:, :, 1] - point[1])**2)
    
    # Assign each pixel to nearest point
    cells = np.argmin(distances, axis=2)
    return cells


def hexagonal_grid(width: int = 800, height: int = 600,
                   hex_size: float = 30.0) -> np.ndarray:
    """
    Generate hexagonal grid pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        hex_size: Size of each hexagon
        
    Returns:
        2D numpy array representing the pattern
    """
    y, x = np.ogrid[:height, :width]
    
    # Hexagonal tiling coordinates
    sqrt3 = np.sqrt(3)
    q = (x * 2/3) / hex_size
    r = (-x / 3 + sqrt3/3 * y) / hex_size
    
    # Round to nearest hex
    cube_x = q
    cube_z = r
    cube_y = -cube_x - cube_z
    
    rx = np.round(cube_x)
    ry = np.round(cube_y)
    rz = np.round(cube_z)
    
    x_diff = np.abs(rx - cube_x)
    y_diff = np.abs(ry - cube_y)
    z_diff = np.abs(rz - cube_z)
    
    mask_x = (x_diff > y_diff) & (x_diff > z_diff)
    mask_y = y_diff > z_diff
    
    rx = np.where(mask_x, -ry - rz, rx)
    
    # Create pattern based on hex coordinates
    pattern = (rx + ry) % 3
    return pattern


def circular_waves(width: int = 800, height: int = 600,
                   num_waves: int = 20,
                   center: Tuple[float, float] = None) -> np.ndarray:
    """
    Generate circular wave pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        num_waves: Number of concentric circles
        center: Center point (x, y), defaults to image center
        
    Returns:
        2D numpy array representing the pattern
    """
    if center is None:
        center = (width / 2, height / 2)
    
    y, x = np.ogrid[:height, :width]
    r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    
    max_r = np.sqrt(width**2 + height**2) / 2
    pattern = np.sin(r * num_waves * 2 * np.pi / max_r)
    
    return pattern
