#!/usr/bin/env python3
"""
Mathematical Pattern Generator
Generate various mathematical patterns for generative art.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os
from typing import Optional
import argparse

# Import pattern generation modules
import fractals
import geometric
import waves
import parametric


def save_pattern(pattern: np.ndarray, filename: str, cmap: str = 'viridis', 
                output_dir: str = 'output') -> None:
    """
    Save a pattern to an image file.
    
    Args:
        pattern: 2D numpy array representing the pattern
        filename: Output filename
        cmap: Matplotlib colormap name
        output_dir: Output directory
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    plt.figure(figsize=(10, 8))
    plt.imshow(pattern, cmap=cmap, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filepath, dpi=150, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(f"Saved: {filepath}")


def generate_all_patterns(output_dir: str = 'output', size: tuple = (800, 600)) -> None:
    """
    Generate all available mathematical patterns.
    
    Args:
        output_dir: Directory to save output images
        size: (width, height) tuple for image dimensions
    """
    width, height = size
    
    print("Generating mathematical patterns...")
    
    # Fractal patterns
    print("\n=== Fractal Patterns ===")
    pattern = fractals.mandelbrot(width, height, max_iter=100)
    save_pattern(pattern, 'fractal_mandelbrot.png', cmap='hot', output_dir=output_dir)
    
    pattern = fractals.julia(width, height, c=-0.4+0.6j, max_iter=100)
    save_pattern(pattern, 'fractal_julia.png', cmap='twilight', output_dir=output_dir)
    
    pattern = fractals.burning_ship(width, height, max_iter=100)
    save_pattern(pattern, 'fractal_burning_ship.png', cmap='inferno', output_dir=output_dir)
    
    # Geometric patterns
    print("\n=== Geometric Patterns ===")
    pattern = geometric.spiral(width, height, spiral_type='archimedean', turns=15)
    save_pattern(pattern, 'geometric_spiral_archimedean.png', cmap='binary', output_dir=output_dir)
    
    pattern = geometric.spiral(width, height, spiral_type='logarithmic', turns=8)
    save_pattern(pattern, 'geometric_spiral_logarithmic.png', cmap='binary', output_dir=output_dir)
    
    pattern = geometric.spiral(width, height, spiral_type='fermat', turns=10)
    save_pattern(pattern, 'geometric_spiral_fermat.png', cmap='binary', output_dir=output_dir)
    
    pattern = geometric.voronoi_cells(width, height, num_points=50)
    save_pattern(pattern, 'geometric_voronoi.png', cmap='tab20', output_dir=output_dir)
    
    pattern = geometric.hexagonal_grid(width, height, hex_size=30)
    save_pattern(pattern, 'geometric_hexagonal.png', cmap='Set3', output_dir=output_dir)
    
    pattern = geometric.circular_waves(width, height, num_waves=30)
    save_pattern(pattern, 'geometric_circular_waves.png', cmap='twilight', output_dir=output_dir)
    
    # Wave patterns
    print("\n=== Wave Patterns ===")
    pattern = waves.interference_pattern(width, height, wavelength=25)
    save_pattern(pattern, 'waves_interference.png', cmap='coolwarm', output_dir=output_dir)
    
    pattern = waves.moire_pattern(width, height, freq1=20, freq2=21, angle2=5)
    save_pattern(pattern, 'waves_moire.png', cmap='gray', output_dir=output_dir)
    
    pattern = waves.standing_waves(width, height, modes=(5, 7))
    save_pattern(pattern, 'waves_standing.png', cmap='seismic', output_dir=output_dir)
    
    pattern = waves.ripple_effect(width, height, num_ripples=8, decay=0.005)
    save_pattern(pattern, 'waves_ripple.png', cmap='ocean', output_dir=output_dir)
    
    pattern = waves.wave_superposition(width, height, directions=[0, 60, 120], wavelength=40)
    save_pattern(pattern, 'waves_superposition.png', cmap='viridis', output_dir=output_dir)
    
    # Parametric curves
    print("\n=== Parametric Curves ===")
    pattern = parametric.lissajous(width, height, a=3, b=4, delta=np.pi/2)
    save_pattern(pattern, 'parametric_lissajous_3_4.png', cmap='magma', output_dir=output_dir)
    
    pattern = parametric.lissajous(width, height, a=5, b=6, delta=0)
    save_pattern(pattern, 'parametric_lissajous_5_6.png', cmap='plasma', output_dir=output_dir)
    
    pattern = parametric.rose_curve(width, height, n=7, d=4)
    save_pattern(pattern, 'parametric_rose_7_4.png', cmap='spring', output_dir=output_dir)
    
    pattern = parametric.rose_curve(width, height, n=5, d=3)
    save_pattern(pattern, 'parametric_rose_5_3.png', cmap='summer', output_dir=output_dir)
    
    pattern = parametric.hypotrochoid(width, height, R=100, r=50, d=70)
    save_pattern(pattern, 'parametric_hypotrochoid.png', cmap='autumn', output_dir=output_dir)
    
    pattern = parametric.butterfly_curve(width, height)
    save_pattern(pattern, 'parametric_butterfly.png', cmap='cool', output_dir=output_dir)
    
    print(f"\n✓ All patterns generated successfully in '{output_dir}' directory!")


def main():
    """Main entry point for the pattern generator."""
    parser = argparse.ArgumentParser(
        description='Generate mathematical patterns for generative art',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Generate all patterns
  %(prog)s --output my_art          # Save to 'my_art' directory
  %(prog)s --size 1920 1080         # Generate in Full HD resolution
  %(prog)s --pattern mandelbrot     # Generate only Mandelbrot fractal
        """
    )
    
    parser.add_argument('--output', '-o', default='output',
                       help='Output directory (default: output)')
    parser.add_argument('--size', '-s', nargs=2, type=int, default=[800, 600],
                       metavar=('WIDTH', 'HEIGHT'),
                       help='Image size in pixels (default: 800 600)')
    parser.add_argument('--pattern', '-p', choices=[
        'mandelbrot', 'julia', 'burning_ship',
        'spiral', 'voronoi', 'hexagonal', 'circular_waves',
        'interference', 'moire', 'standing', 'ripple', 'superposition',
        'lissajous', 'rose', 'hypotrochoid', 'butterfly'
    ], help='Generate a specific pattern only')
    
    args = parser.parse_args()
    width, height = args.size
    
    if args.pattern:
        print(f"Generating {args.pattern} pattern...")
        
        # Generate specific pattern
        if args.pattern == 'mandelbrot':
            pattern = fractals.mandelbrot(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='hot', output_dir=args.output)
        elif args.pattern == 'julia':
            pattern = fractals.julia(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='twilight', output_dir=args.output)
        elif args.pattern == 'burning_ship':
            pattern = fractals.burning_ship(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='inferno', output_dir=args.output)
        elif args.pattern == 'spiral':
            pattern = geometric.spiral(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='binary', output_dir=args.output)
        elif args.pattern == 'voronoi':
            pattern = geometric.voronoi_cells(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='tab20', output_dir=args.output)
        elif args.pattern == 'hexagonal':
            pattern = geometric.hexagonal_grid(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='Set3', output_dir=args.output)
        elif args.pattern == 'circular_waves':
            pattern = geometric.circular_waves(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='twilight', output_dir=args.output)
        elif args.pattern == 'interference':
            pattern = waves.interference_pattern(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='coolwarm', output_dir=args.output)
        elif args.pattern == 'moire':
            pattern = waves.moire_pattern(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='gray', output_dir=args.output)
        elif args.pattern == 'standing':
            pattern = waves.standing_waves(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='seismic', output_dir=args.output)
        elif args.pattern == 'ripple':
            pattern = waves.ripple_effect(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='ocean', output_dir=args.output)
        elif args.pattern == 'superposition':
            pattern = waves.wave_superposition(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='viridis', output_dir=args.output)
        elif args.pattern == 'lissajous':
            pattern = parametric.lissajous(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='magma', output_dir=args.output)
        elif args.pattern == 'rose':
            pattern = parametric.rose_curve(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='spring', output_dir=args.output)
        elif args.pattern == 'hypotrochoid':
            pattern = parametric.hypotrochoid(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='autumn', output_dir=args.output)
        elif args.pattern == 'butterfly':
            pattern = parametric.butterfly_curve(width, height)
            save_pattern(pattern, f'{args.pattern}.png', cmap='cool', output_dir=args.output)
        
        print(f"✓ Pattern saved to '{args.output}' directory!")
    else:
        # Generate all patterns
        generate_all_patterns(output_dir=args.output, size=(width, height))


if __name__ == '__main__':
    main()
