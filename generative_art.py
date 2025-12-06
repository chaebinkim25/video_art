#!/usr/bin/env python3
"""
Generative Art Video Creator
Creates classic generative art animations using NumPy and MoviePy.

This script generates a particle flow field animation - a classic generative art style
where particles move through a dynamically generated flow field creating organic patterns.
"""

import numpy as np
from moviepy import VideoClip


class FlowFieldArt:
    """Creates a flow field generative art animation."""
    
    def __init__(self, width=1280, height=720, num_particles=1000, fps=30, duration=10):
        """
        Initialize the flow field art generator.
        
        Args:
            width: Video width in pixels
            height: Video height in pixels
            num_particles: Number of particles in the animation
            fps: Frames per second
            duration: Video duration in seconds
        """
        self.width = width
        self.height = height
        self.num_particles = num_particles
        self.fps = fps
        self.duration = duration
        
        # Initialize particle positions randomly
        self.particles = np.random.rand(num_particles, 2) * [width, height]
        
        # Initialize particle velocities
        self.velocities = np.zeros((num_particles, 2))
        
        # Color array for particles (HSV-like)
        self.colors = np.random.rand(num_particles, 3) * 255
        
        # Particle history for trails
        self.history = []
        self.max_history = 20
        
    def flow_field(self, x, y, t):
        """
        Calculate flow field direction at given position and time.
        
        Args:
            x: X coordinate
            y: Y coordinate
            t: Time
            
        Returns:
            Angle in radians for flow direction
        """
        # Classic Perlin-noise-like flow field using sine waves
        scale = 0.005
        time_scale = 0.5
        
        angle = (
            np.sin(x * scale + t * time_scale) * 
            np.cos(y * scale - t * time_scale) * 
            np.pi * 2
        )
        
        return angle
    
    def update_particles(self, t):
        """
        Update particle positions based on flow field.
        
        Args:
            t: Current time
        """
        # Calculate flow field angles for each particle
        angles = self.flow_field(self.particles[:, 0], self.particles[:, 1], t)
        
        # Update velocities based on flow field
        speed = 2.0
        self.velocities[:, 0] = np.cos(angles) * speed
        self.velocities[:, 1] = np.sin(angles) * speed
        
        # Update positions
        self.particles += self.velocities
        
        # Wrap particles around edges
        self.particles[:, 0] = self.particles[:, 0] % self.width
        self.particles[:, 1] = self.particles[:, 1] % self.height
        
        # Store history for trails
        self.history.append(self.particles.copy())
        if len(self.history) > self.max_history:
            self.history.pop(0)
    
    def make_frame(self, t):
        """
        Generate a single frame at time t.
        
        Args:
            t: Time in seconds
            
        Returns:
            RGB frame as numpy array
        """
        # Create black background
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        # Update particle positions
        self.update_particles(t)
        
        # Draw particle trails with fading effect
        for i, hist_particles in enumerate(self.history):
            alpha = (i + 1) / len(self.history)  # Fade factor
            
            for j, (x, y) in enumerate(hist_particles):
                x_int, y_int = int(x), int(y)
                
                # Bounds checking
                if 0 <= x_int < self.width and 0 <= y_int < self.height:
                    # Draw particle with fading trail
                    color = self.colors[j] * alpha
                    frame[y_int, x_int] = color.astype(np.uint8)
                    
                    # Draw small circle around particle for better visibility
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            nx, ny = x_int + dx, y_int + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height:
                                current_color = frame[ny, nx]
                                new_color = np.minimum(current_color + color * 0.3, 255)
                                frame[ny, nx] = new_color.astype(np.uint8)
        
        return frame


def create_generative_art_video(
    output_filename='generative_art.mp4',
    width=1280,
    height=720,
    num_particles=1000,
    fps=30,
    duration=10
):
    """
    Create a generative art video and save it to file.
    
    Args:
        output_filename: Output video filename
        width: Video width in pixels
        height: Video height in pixels
        num_particles: Number of particles
        fps: Frames per second
        duration: Video duration in seconds
    """
    print(f"Initializing generative art with {num_particles} particles...")
    art = FlowFieldArt(width, height, num_particles, fps, duration)
    
    print(f"Creating {duration}s video at {width}x{height} @ {fps}fps...")
    video = VideoClip(art.make_frame, duration=duration)
    
    print(f"Rendering video to {output_filename}...")
    video.write_videofile(
        output_filename,
        fps=fps,
        codec='libx264',
        audio=False,
        preset='medium'
    )
    
    print(f"✓ Video saved to {output_filename}")


if __name__ == "__main__":
    # Create a 10-second generative art video
    create_generative_art_video(
        output_filename='generative_art.mp4',
        width=1280,
        height=720,
        num_particles=1000,
        fps=30,
        duration=10
    )
