"""
Wave-based Pattern Generation Module
Generates interference patterns, moiré effects, and wave superposition.
"""

import numpy as np
from typing import Tuple, List


def interference_pattern(width: int = 800, height: int = 600,
                        sources: List[Tuple[float, float]] = None,
                        wavelength: float = 20.0) -> np.ndarray:
    """
    Generate wave interference pattern from multiple point sources.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        sources: List of (x, y) coordinates for wave sources
        wavelength: Wavelength of the waves
        
    Returns:
        2D numpy array representing the pattern
    """
    if sources is None:
        # Default to two sources creating classic interference
        sources = [(width * 0.3, height * 0.5), (width * 0.7, height * 0.5)]
    
    y, x = np.ogrid[:height, :width]
    pattern = np.zeros((height, width))
    
    for sx, sy in sources:
        r = np.sqrt((x - sx)**2 + (y - sy)**2)
        pattern += np.sin(2 * np.pi * r / wavelength)
    
    return pattern


def moire_pattern(width: int = 800, height: int = 600,
                 freq1: float = 20.0,
                 freq2: float = 21.0,
                 angle1: float = 0.0,
                 angle2: float = 5.0) -> np.ndarray:
    """
    Generate moiré pattern from overlapping periodic structures.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        freq1: Frequency of first pattern
        freq2: Frequency of second pattern
        angle1: Angle of first pattern in degrees
        angle2: Angle of second pattern in degrees
        
    Returns:
        2D numpy array representing the pattern
    """
    y, x = np.ogrid[:height, :width]
    
    # First pattern
    angle1_rad = np.radians(angle1)
    pattern1 = np.sin(2 * np.pi * (x * np.cos(angle1_rad) + y * np.sin(angle1_rad)) / freq1)
    
    # Second pattern
    angle2_rad = np.radians(angle2)
    pattern2 = np.sin(2 * np.pi * (x * np.cos(angle2_rad) + y * np.sin(angle2_rad)) / freq2)
    
    # Combine patterns
    return pattern1 * pattern2


def standing_waves(width: int = 800, height: int = 600,
                   modes: Tuple[int, int] = (3, 4)) -> np.ndarray:
    """
    Generate standing wave pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        modes: (nx, ny) mode numbers for the standing wave
        
    Returns:
        2D numpy array representing the pattern
    """
    y, x = np.ogrid[:height, :width]
    nx, ny = modes
    
    pattern = np.sin(nx * np.pi * x / width) * np.sin(ny * np.pi * y / height)
    return pattern


def ripple_effect(width: int = 800, height: int = 600,
                 num_ripples: int = 5,
                 decay: float = 0.01) -> np.ndarray:
    """
    Generate ripple effect pattern.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        num_ripples: Number of ripple rings
        decay: Amplitude decay factor
        
    Returns:
        2D numpy array representing the pattern
    """
    y, x = np.ogrid[:height, :width]
    cx, cy = width / 2, height / 2
    r = np.sqrt((x - cx)**2 + (y - cy)**2)
    
    # Create ripples with decay
    pattern = np.sin(2 * np.pi * num_ripples * r / max(width, height))
    pattern *= np.exp(-decay * r)
    
    return pattern


def wave_superposition(width: int = 800, height: int = 600,
                      directions: List[float] = None,
                      wavelength: float = 30.0) -> np.ndarray:
    """
    Generate pattern from superposition of plane waves.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        directions: List of wave directions in degrees
        wavelength: Wavelength of the waves
        
    Returns:
        2D numpy array representing the pattern
    """
    if directions is None:
        directions = [0, 60, 120]  # Three-way symmetry
    
    y, x = np.ogrid[:height, :width]
    pattern = np.zeros((height, width))
    
    for angle in directions:
        angle_rad = np.radians(angle)
        k_x = np.cos(angle_rad) * 2 * np.pi / wavelength
        k_y = np.sin(angle_rad) * 2 * np.pi / wavelength
        pattern += np.sin(k_x * x + k_y * y)
    
    return pattern
