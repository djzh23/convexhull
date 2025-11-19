"""
Script to create demo GIFs for both convex hull algorithms.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'FindingConvexHullImplementierung'))

import numpy as np
import matplotlib.pyplot as plt
import imageio
from GrahamScan import right_turn
from JarvisMarch import ccw


def create_graham_scan_gif(num_points=30, output_file='demo_graham_scan.gif'):
    """Create a GIF showing the Graham Scan algorithm."""
    # Set random seed for reproducibility
    np.random.seed(42)
    points = [(np.random.randint(-300, 300), np.random.randint(-300, 300)) 
              for _ in range(num_points)]
    
    points.sort()
    points = np.array(points)
    
    frames = []
    l_upper = [points[0], points[1]]
    
    # Upper hull
    for i in range(2, len(points)):
        l_upper.append(points[i])
        while len(l_upper) > 2 and not right_turn(l_upper[-1], l_upper[-2], l_upper[-3]):
            del l_upper[-2]
        l = np.array(l_upper)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(l[:, 0], l[:, 1], 'b-', linewidth=2)
        ax.plot(points[:, 0], points[:, 1], ".r", markersize=8)
        ax.axis('off')
        ax.set_title('Graham Scan - Upper Hull', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        fig.canvas.draw()
        # Convert figure to numpy array
        buf = fig.canvas.buffer_rgba()
        frame = np.asarray(buf)
        frames.append(frame)
        plt.close(fig)
    
    # Lower hull
    l_lower = [points[-1], points[-2]]
    for i in range(len(points) - 3, -1, -1):
        l_lower.append(points[i])
        while len(l_lower) > 2 and not right_turn(l_lower[-1], l_lower[-2], l_lower[-3]):
            del l_lower[-2]
        l = np.array(l_upper + l_lower)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(l[:, 0], l[:, 1], 'b-', linewidth=2)
        ax.plot(points[:, 0], points[:, 1], ".r", markersize=8)
        ax.axis('off')
        ax.set_title('Graham Scan - Lower Hull', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        fig.canvas.draw()
        # Convert figure to numpy array
        buf = fig.canvas.buffer_rgba()
        frame = np.asarray(buf)
        frames.append(frame)
        plt.close(fig)
    
    # Final hull
    del l_lower[0]
    del l_lower[-1]
    l = l_upper + l_lower
    l = np.array(l)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    # Close the polygon
    closed_hull = np.vstack([l, l[0]])
    ax.plot(closed_hull[:, 0], closed_hull[:, 1], 'b-', linewidth=2)
    ax.plot(points[:, 0], points[:, 1], ".r", markersize=8)
    ax.axis('off')
    ax.set_title('Graham Scan - Final Convex Hull', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    fig.canvas.draw()
    # Convert figure to numpy array
    buf = fig.canvas.buffer_rgba()
    frame = np.asarray(buf)
    frames.append(frame)
    plt.close(fig)
    
    # Save GIF (convert RGBA to RGB)
    frames_rgb = [frame[:, :, :3] for frame in frames]
    imageio.mimsave(output_file, frames_rgb, duration=0.5, loop=0)
    print(f"GIF saved: {output_file}")


def create_jarvis_march_gif(num_points=30, output_file='demo_jarvis_march.gif'):
    """Create a GIF showing the Jarvis March algorithm."""
    # Set random seed for reproducibility
    np.random.seed(42)
    points = np.array([(np.random.randint(0, 300), np.random.randint(0, 300)) 
                      for _ in range(num_points)])
    
    frames = []
    n = len(points)
    hull = [None] * n
    
    # Find leftmost point
    leftmost_idx = np.where(points[:, 0] == np.min(points[:, 0]))[0][0]
    point_on_hull = points[leftmost_idx]
    
    i = 0
    while True:
        hull[i] = point_on_hull
        endpoint = points[0]
        for j in range(1, n):
            if ((endpoint[0] == point_on_hull[0] and endpoint[1] == point_on_hull[1]) or
                    not ccw(points[j], hull[i], endpoint)):
                endpoint = points[j]
        i += 1
        point_on_hull = endpoint
        current_hull = np.array([hull[k] for k in range(n) if hull[k] is not None])
        
        # Create frame
        fig, ax = plt.subplots(figsize=(8, 8))
        if len(current_hull) > 1:
            ax.plot(current_hull[:, 0], current_hull[:, 1], 'b-', linewidth=2)
        ax.plot(points[:, 0], points[:, 1], ".r", markersize=8)
        ax.axis('off')
        ax.set_title('Jarvis March (Gift Wrapping)', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        fig.canvas.draw()
        # Convert figure to numpy array
        buf = fig.canvas.buffer_rgba()
        frame = np.asarray(buf)
        frames.append(frame)
        plt.close(fig)
        
        if endpoint[0] == hull[0][0] and endpoint[1] == hull[0][1]:
            break
    
    # Final frame with closed polygon
    while hull[-1] is None:
        del hull[-1]
    hull = np.array(hull)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    closed_hull = np.vstack([hull, hull[0]])
    ax.plot(closed_hull[:, 0], closed_hull[:, 1], 'b-', linewidth=2)
    ax.plot(points[:, 0], points[:, 1], ".r", markersize=8)
    ax.axis('off')
    ax.set_title('Jarvis March - Final Convex Hull', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    fig.canvas.draw()
    # Convert figure to numpy array
    buf = fig.canvas.buffer_rgba()
    frame = np.asarray(buf)
    frames.append(frame)
    plt.close(fig)
    
    # Save GIF (convert RGBA to RGB)
    frames_rgb = [frame[:, :, :3] for frame in frames]
    imageio.mimsave(output_file, frames_rgb, duration=0.5, loop=0)
    print(f"GIF saved: {output_file}")


if __name__ == '__main__':
    print("Creating demo GIFs...")
    create_graham_scan_gif(30, 'demo_graham_scan.gif')
    create_jarvis_march_gif(30, 'demo_jarvis_march.gif')
    print("Done!")

