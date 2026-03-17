import numpy as np
import matplotlib.pyplot as plt
import imageio

# Create frames list
frames = []

# Video settings
width, height = 5, 6
n_frames = 120

# Create animation frames
for i in range(n_frames):
    fig, ax = plt.subplots(figsize=(3, 5))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 4)
    ax.set_facecolor("black")

    t = i / n_frames

    # Tulip petals (simple parametric tulip shape)
    theta = np.linspace(0, np.pi, 100)

    # Petal animation opening effect
    r = 1.2 * np.sin(theta) * (0.5 + t)

    x1 = r * np.cos(theta)
    y1 = r * np.sin(theta) + 1.5

    x2 = -r * np.cos(theta)
    y2 = r * np.sin(theta) + 1.5

    # Draw petals
    ax.fill(x1, y1, color="#ff4d6d")
    ax.fill(x2, y2, color="#ff4d6d")

    # Flower stem
    stem_y = np.linspace(0, 1.5, 50)
    ax.plot(np.zeros_like(stem_y), stem_y, color="green", linewidth=4)

    # Leaves
    leaf_x = np.linspace(0, 1, 30)
    leaf_y = 0.5 * np.sin(leaf_x * np.pi) + 0.5
    ax.fill(leaf_x - 0.8, leaf_y, color="green")

    ax.axis("off")

    # Save frame
    fig.canvas.draw()
    frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(frame)

    plt.close(fig)

# Save video
imageio.mimsave("tulip_love_animation.mp4", frames, fps=30)

print("✅ Tulip animation video created: tulip_love_animation.mp4")