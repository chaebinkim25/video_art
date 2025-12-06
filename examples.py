#!/usr/bin/env python3
"""
Example script demonstrating how to use the mathematical pattern library.
This shows various ways to generate and customize patterns programmatically.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os

# Import pattern modules
import fractals
import geometric
import waves
import parametric


def example_1_basic_fractal():
    """Example 1: Generate a basic Mandelbrot fractal."""
    print("Example 1: Basic Mandelbrot fractal")
    
    pattern = fractals.mandelbrot(width=800, height=600, max_iter=100)
    
    plt.figure(figsize=(10, 8))
    plt.imshow(pattern, cmap='hot', interpolation='bilinear')
    plt.title('Mandelbrot Set', fontsize=16, color='white')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('output/example_1_mandelbrot.png', dpi=150, bbox_inches='tight', 
                facecolor='black')
    plt.close()
    print("  ✓ Saved: output/example_1_mandelbrot.png\n")


def example_2_custom_julia():
    """Example 2: Create multiple Julia sets with different parameters."""
    print("Example 2: Julia set variations")
    
    # Different complex constants create different Julia sets
    julia_params = [
        (-0.4 + 0.6j, 'Julia Set (c = -0.4 + 0.6i)'),
        (0.285 + 0.01j, 'Julia Set (c = 0.285 + 0.01i)'),
        (-0.8 + 0.156j, 'Julia Set (c = -0.8 + 0.156i)'),
        (-0.7269 + 0.1889j, 'Julia Set (c = -0.7269 + 0.1889i)')
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Julia Set Variations', fontsize=18, fontweight='bold')
    
    for (c, title), ax in zip(julia_params, axes.flat):
        pattern = fractals.julia(width=600, height=600, c=c, max_iter=100)
        ax.imshow(pattern, cmap='twilight', interpolation='bilinear')
        ax.set_title(title, fontsize=12)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('output/example_2_julia_variations.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_2_julia_variations.png\n")


def example_3_spiral_showcase():
    """Example 3: Showcase different spiral types."""
    print("Example 3: Spiral patterns")
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Mathematical Spirals', fontsize=18, fontweight='bold')
    
    spiral_types = [
        ('archimedean', 'Archimedean Spiral'),
        ('logarithmic', 'Logarithmic Spiral'),
        ('fermat', 'Fermat Spiral')
    ]
    
    for (spiral_type, title), ax in zip(spiral_types, axes):
        pattern = geometric.spiral(800, 600, spiral_type=spiral_type, 
                                  turns=15, thickness=2.0)
        ax.imshow(pattern, cmap='binary', interpolation='bilinear')
        ax.set_title(title, fontsize=14)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('output/example_3_spirals.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_3_spirals.png\n")


def example_4_interference():
    """Example 4: Multi-source wave interference."""
    print("Example 4: Wave interference patterns")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Wave Interference Patterns', fontsize=18, fontweight='bold')
    
    configurations = [
        ([(200, 300), (600, 300)], '2 Sources (Horizontal)'),
        ([(400, 150), (400, 450)], '2 Sources (Vertical)'),
        ([(200, 200), (600, 200), (400, 500)], '3 Sources (Triangle)'),
        ([(200, 200), (600, 200), (200, 500), (600, 500)], '4 Sources (Square)')
    ]
    
    for (sources, title), ax in zip(configurations, axes.flat):
        pattern = waves.interference_pattern(800, 600, sources=sources, wavelength=25)
        ax.imshow(pattern, cmap='coolwarm', interpolation='bilinear')
        ax.set_title(title, fontsize=12)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('output/example_4_interference.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_4_interference.png\n")


def example_5_lissajous_family():
    """Example 5: Lissajous curve family."""
    print("Example 5: Lissajous curves")
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Lissajous Curves (a:b ratios)', fontsize=18, fontweight='bold')
    
    params = [
        (1, 1, 0, '1:1'),
        (3, 2, np.pi/2, '3:2'),
        (3, 4, np.pi/2, '3:4'),
        (5, 4, np.pi/2, '5:4'),
        (5, 6, 0, '5:6'),
        (7, 5, np.pi/4, '7:5')
    ]
    
    for (a, b, delta, title), ax in zip(params, axes.flat):
        pattern = parametric.lissajous(600, 600, a=a, b=b, delta=delta, thickness=3)
        ax.imshow(pattern, cmap='magma', interpolation='bilinear')
        ax.set_title(f'a={a}, b={b} ({title})', fontsize=12)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('output/example_5_lissajous.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_5_lissajous.png\n")


def example_6_rose_curves():
    """Example 6: Rose curve patterns."""
    print("Example 6: Rose curves")
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Rose Curves (Rhodonea)', fontsize=18, fontweight='bold')
    
    params = [
        (3, 1, '3 petals'),
        (5, 1, '5 petals'),
        (7, 1, '7 petals'),
        (4, 1, '4 petals'),
        (6, 1, '6 petals'),
        (8, 1, '8 petals')
    ]
    
    for (n, d, title), ax in zip(params, axes.flat):
        pattern = parametric.rose_curve(600, 600, n=n, d=d, thickness=2)
        ax.imshow(pattern, cmap='spring', interpolation='bilinear')
        ax.set_title(title, fontsize=12)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('output/example_6_roses.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_6_roses.png\n")


def example_7_custom_colormap():
    """Example 7: Using custom colormaps."""
    print("Example 7: Custom colormaps")
    
    # Create a custom colormap
    colors = ['#000033', '#000055', '#0066FF', '#00FFFF', '#FFFF00', '#FF6600', '#FF0000']
    n_bins = 256
    cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)
    
    pattern = fractals.mandelbrot(width=1200, height=800, max_iter=150,
                                  bounds=(-2.5, 1.0, -1.0, 1.0))
    
    plt.figure(figsize=(14, 10))
    plt.imshow(pattern, cmap=cmap, interpolation='bilinear')
    plt.title('Mandelbrot Set with Custom Colormap', fontsize=18, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('output/example_7_custom_colormap.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_7_custom_colormap.png\n")


def example_8_combined_patterns():
    """Example 8: Combining multiple patterns."""
    print("Example 8: Combined patterns")
    
    # Create base patterns
    wave1 = waves.wave_superposition(800, 600, directions=[0, 60, 120], wavelength=40)
    wave2 = geometric.circular_waves(800, 600, num_waves=30)
    
    # Combine patterns
    combined = wave1 * 0.5 + wave2 * 0.5
    
    plt.figure(figsize=(12, 9))
    plt.imshow(combined, cmap='twilight', interpolation='bilinear')
    plt.title('Combined Wave Patterns', fontsize=18, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('output/example_8_combined.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("  ✓ Saved: output/example_8_combined.png\n")


def main():
    """Run all examples."""
    os.makedirs('output', exist_ok=True)
    
    print("\n" + "="*60)
    print("Mathematical Pattern Generation Examples")
    print("="*60 + "\n")
    
    example_1_basic_fractal()
    example_2_custom_julia()
    example_3_spiral_showcase()
    example_4_interference()
    example_5_lissajous_family()
    example_6_rose_curves()
    example_7_custom_colormap()
    example_8_combined_patterns()
    
    print("="*60)
    print("All examples completed successfully!")
    print("Check the 'output' directory for generated images.")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
