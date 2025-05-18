import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# === SETTINGS ===
INPUT_IMAGE = 'your_image.jpg'  # Change this to your image file
RESIZE_DIM = (50, 50)  # Smaller = more abstract, bigger = more detailed

# === LOAD IMAGE ===
image = Image.open(INPUT_IMAGE).convert('L')  # Convert to grayscale
image = image.resize(RESIZE_DIM)
pixels = np.array(image)

# === SETUP PLOT ===
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.axis('off')

# === DRAW DIAMOND GRID ===
for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        brightness = pixels[i, j] / 255  # Normalize to [0, 1]
        color = str(brightness)  # Grayscale color
        x, y = j, -i  # Flip y for top-down drawing

        diamond = plt.Polygon(
            [[x, y + 0.5], [x + 0.5, y], [x, y - 0.5], [x - 0.5, y]],
            color=color,
            edgecolor=None
        )
        ax.add_patch(diamond)

plt.xlim(-1, pixels.shape[1] + 1)
plt.ylim(-pixels.shape[0] - 1, 1)
plt.gca().invert_yaxis()

# === SAVE OR SHOW ===
plt.tight_layout()
plt.savefig('output_diamond.png', dpi=300)
plt.show()
