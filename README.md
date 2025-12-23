# video_art

A generative art video creator using NumPy and MoviePy. Creates beautiful particle flow field animations in classic generative art style.

## Features

- **Flow Field Animation**: Particles move through dynamically generated flow fields
- **Particle Trails**: Smooth fading trails create organic patterns
- **Customizable**: Adjust resolution, particle count, duration, and FPS
- **Pure NumPy**: All mathematics handled with NumPy for performance
- **MoviePy Rendering**: High-quality video output

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the script to generate a 10-second generative art video:

```bash
python generative_art.py
```

### Customization

Edit the parameters in `generative_art.py` to customize the output:

```python
create_generative_art_video(
    output_filename='generative_art.mp4',  # Output file name
    width=1280,                             # Video width
    height=720,                             # Video height
    num_particles=1000,                     # Number of particles
    fps=30,                                 # Frames per second
    duration=10                             # Duration in seconds
)
```

## How It Works

The script implements a particle flow field system:

1. **Initialization**: Particles are randomly distributed across the canvas
2. **Flow Field**: A mathematical flow field is generated using sine/cosine functions
3. **Particle Movement**: Each particle follows the flow field direction
4. **Trail Rendering**: Historical positions create fading trails
5. **Video Export**: MoviePy renders frames into an MP4 video

## Requirements

- Python 3.7+
- NumPy >= 1.21.0
- MoviePy >= 1.0.3

## License

GNU General Public License v3.0