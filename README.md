# Mathematical Pattern Generator (Video Art)

A Python library for generating beautiful mathematical patterns and generative art. Create stunning visualizations of fractals, geometric patterns, wave interference, and parametric curves.

## Features

### 🌀 Fractal Patterns
- **Mandelbrot Set**: Classic fractal with infinite complexity
- **Julia Set**: Beautiful variations with different complex parameters
- **Burning Ship**: Unique fractal with ship-like structures

### 📐 Geometric Patterns
- **Spirals**: Archimedean, logarithmic, and Fermat spirals
- **Voronoi Diagrams**: Cell-based tessellations
- **Hexagonal Grids**: Perfect honeycomb patterns
- **Circular Waves**: Concentric circle patterns

### 🌊 Wave Patterns
- **Interference Patterns**: Multi-source wave interference
- **Moiré Effects**: Overlapping periodic structures
- **Standing Waves**: Modal vibration patterns
- **Ripple Effects**: Water-like ripple patterns
- **Wave Superposition**: Plane wave combinations

### 📈 Parametric Curves
- **Lissajous Figures**: Harmonic oscillation patterns
- **Rose Curves (Rhodonea)**: Flower-like mathematical curves
- **Hypotrochoid**: Spirograph-style patterns
- **Butterfly Curve**: Exotic mathematical butterfly

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chaebinkim25/video_art.git
cd video_art
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Generate All Patterns

Generate all available patterns with default settings:

```bash
python generate_patterns.py
```

This will create an `output` directory with all pattern images.

### Generate Specific Pattern

Generate a single pattern:

```bash
python generate_patterns.py --pattern mandelbrot
python generate_patterns.py --pattern spiral
python generate_patterns.py --pattern lissajous
```

### Custom Output Directory

Specify a custom output directory:

```bash
python generate_patterns.py --output my_art
```

### Custom Image Size

Generate patterns in custom resolution:

```bash
python generate_patterns.py --size 1920 1080  # Full HD
python generate_patterns.py --size 3840 2160  # 4K
```

### Combined Options

```bash
python generate_patterns.py --pattern julia --size 1920 1080 --output hd_art
```

## Using as a Library

You can also import and use the pattern generators in your own Python code:

```python
import numpy as np
import matplotlib.pyplot as plt
import fractals
import geometric
import waves
import parametric

# Generate a Mandelbrot fractal
pattern = fractals.mandelbrot(width=800, height=600, max_iter=100)
plt.imshow(pattern, cmap='hot')
plt.show()

# Generate an interference pattern
pattern = waves.interference_pattern(
    width=800, 
    height=600,
    sources=[(200, 300), (600, 300)],
    wavelength=20
)
plt.imshow(pattern, cmap='coolwarm')
plt.show()

# Generate a Lissajous curve
pattern = parametric.lissajous(
    width=800,
    height=600,
    a=5,
    b=6,
    delta=np.pi/4
)
plt.imshow(pattern, cmap='magma')
plt.show()
```

## API Reference

### Fractals Module (`fractals.py`)

#### `mandelbrot(width, height, max_iter, bounds)`
Generate Mandelbrot set fractal.
- `width`: Image width in pixels
- `height`: Image height in pixels
- `max_iter`: Maximum iterations (higher = more detail)
- `bounds`: (xmin, xmax, ymin, ymax) coordinate bounds

#### `julia(width, height, c, max_iter, bounds)`
Generate Julia set fractal.
- `c`: Complex parameter (try: -0.4+0.6j, 0.285+0.01j, -0.8+0.156j)

#### `burning_ship(width, height, max_iter, bounds)`
Generate Burning Ship fractal.

### Geometric Module (`geometric.py`)

#### `spiral(width, height, spiral_type, turns, thickness)`
Generate spiral patterns.
- `spiral_type`: 'archimedean', 'logarithmic', or 'fermat'
- `turns`: Number of spiral rotations
- `thickness`: Line thickness in pixels

#### `voronoi_cells(width, height, num_points, seed)`
Generate Voronoi diagram.
- `num_points`: Number of seed points
- `seed`: Random seed for reproducibility

#### `hexagonal_grid(width, height, hex_size)`
Generate hexagonal tiling.

#### `circular_waves(width, height, num_waves, center)`
Generate concentric circles.

### Waves Module (`waves.py`)

#### `interference_pattern(width, height, sources, wavelength)`
Generate wave interference.
- `sources`: List of (x, y) wave source positions
- `wavelength`: Wave wavelength in pixels

#### `moire_pattern(width, height, freq1, freq2, angle1, angle2)`
Generate moiré pattern.
- `freq1`, `freq2`: Pattern frequencies
- `angle1`, `angle2`: Pattern angles in degrees

#### `standing_waves(width, height, modes)`
Generate standing wave pattern.
- `modes`: (nx, ny) mode numbers

#### `ripple_effect(width, height, num_ripples, decay)`
Generate ripple pattern with decay.

#### `wave_superposition(width, height, directions, wavelength)`
Superpose plane waves.
- `directions`: List of angles in degrees

### Parametric Module (`parametric.py`)

#### `lissajous(width, height, a, b, delta, num_points, thickness)`
Generate Lissajous curve.
- `a`, `b`: Frequency ratios
- `delta`: Phase difference (0 to 2π)

#### `rose_curve(width, height, n, d, num_points, thickness)`
Generate rose curve.
- `n`, `d`: Petal count factor (n/d)

#### `hypotrochoid(width, height, R, r, d, num_points, thickness)`
Generate spirograph pattern.
- `R`: Fixed circle radius
- `r`: Rolling circle radius
- `d`: Pen distance from rolling circle center

#### `butterfly_curve(width, height, num_points, thickness)`
Generate butterfly curve.

## Examples

### Creating Custom Fractals

```python
import fractals
import matplotlib.pyplot as plt

# Zoom into Mandelbrot set
pattern = fractals.mandelbrot(
    width=1920,
    height=1080,
    max_iter=256,
    bounds=(-0.8, -0.4, -0.2, 0.2)  # Zoomed region
)

plt.figure(figsize=(16, 9))
plt.imshow(pattern, cmap='hot', interpolation='bilinear')
plt.axis('off')
plt.savefig('mandelbrot_zoom.png', dpi=150, bbox_inches='tight')
```

### Creating Custom Wave Patterns

```python
import waves

# Create interference from 4 sources in corners
sources = [(100, 100), (700, 100), (100, 500), (700, 500)]
pattern = waves.interference_pattern(
    width=800,
    height=600,
    sources=sources,
    wavelength=30
)
```

### Animating Patterns

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import parametric

fig, ax = plt.subplots(figsize=(8, 8))

def update(frame):
    ax.clear()
    delta = frame * np.pi / 30
    pattern = parametric.lissajous(800, 800, a=3, b=4, delta=delta)
    ax.imshow(pattern, cmap='magma')
    ax.axis('off')
    return ax,

ani = animation.FuncAnimation(fig, update, frames=60, interval=50)
ani.save('lissajous_animation.gif', writer='pillow', fps=20)
```

## Requirements

- Python 3.8+
- NumPy >= 1.24.0
- Matplotlib >= 3.7.0
- Pillow >= 10.0.0
- SciPy >= 1.10.0

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to:
- Add new pattern types
- Improve existing algorithms
- Add documentation and examples
- Report bugs or suggest features

## Gallery

Run `python generate_patterns.py` to see all patterns! The generated images showcase:
- Intricate fractal structures with infinite detail
- Harmonious geometric arrangements
- Beautiful wave interference effects
- Elegant parametric curves

Perfect for:
- Digital art and visualization
- Mathematical education
- Procedural texture generation
- Creative coding projects
- Generative art installations