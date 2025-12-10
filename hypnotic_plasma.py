import cupy as cp  # standard import for GPU arrays
import numpy as np
from moviepy import VideoClip

# --- 4K Configuration ---
WIDTH, HEIGHT = 3840, 2160
DURATION = 222
FPS = 60

# Pre-calculate coordinate grids on the GPU once to save time
# We use 'cp' (CuPy) to allocate this memory on the Graphics Card
X_GPU, Y_GPU = cp.meshgrid(
    cp.linspace(-3, 3, WIDTH, dtype=cp.float32), 
    cp.linspace(-2, 2, HEIGHT, dtype=cp.float32)
)

def make_frame_gpu(t):
    """
    Calculates pixel values using GPU (CUDA) cores.
    """
    # All math here happens on the GPU
    # Note: We use float32 for speed; float64 is often unnecessary for video art
    
    # 1. The Math (executed on GPU)
    z1 = cp.sin(cp.sqrt(X_GPU**2 + Y_GPU**2) * 3 - t * 2)
    z2 = cp.cos(X_GPU * 3 + t)
    z3 = cp.sin((X_GPU + Y_GPU) * 2 - t)

    # 2. Color Mapping (executed on GPU)
    red = cp.sin(z1 + z2 + t)
    green = cp.cos(z1 + z3 - t)
    blue = cp.sin(z2 + z3 + t * 0.5)

    red = cp.clip(((red + 1) / 2), 0, 1) ** 0.8
    green = cp.clip(((green + 1) / 2), 0, 1) ** 0.8
    blue = cp.clip(((blue + 1) / 2), 0, 1) ** 0.8

    # 3. Stack and Convert
    # We stack the channels on the GPU first
    img_gpu = cp.dstack((
        ((red + 1) / 2 * 255).astype('uint8'),
        ((green + 1) / 2 * 255).astype('uint8'),
        ((blue + 1) / 2 * 255).astype('uint8')
    ))

    print(img_gpu.device)

    # 4. TRANSFER TO CPU (Critical Step)
    # MoviePy/FFmpeg runs on CPU, so we must pull the calculated frame back.
    return img_gpu.get() 

# --- Render ---
print(f"Rendering 4K GPU Art ({WIDTH}x{HEIGHT})...")
clip = VideoClip(make_frame_gpu).with_duration(DURATION)
clip.write_videofile("gpu_art_4k.mp4", fps=FPS, codec="libx264rgb", bitrate="50M", ffmpeg_params=["-threads", "16"])
print("Done!")
