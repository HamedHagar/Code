
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="Generate Daimond Photo", layout="centered")
st.title("🧱 Generate Daimond Photo")

mode = st.radio("اختيار الوضع:", ["من لوجو", "من تدرج لوني"])
size = st.slider("عدد المربعات:", 10, 500, 100)

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.axis('off')

if mode == "From Logo":
    uploaded_file = st.file_uploader("Upload (PNG أو JPG)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("L")  # grayscale logo
        image = image.resize((size, size))
        pixels = np.array(image)

        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                brightness = pixels[i, j] / 255
                color = str(brightness)
                x, y = j, -i
                diamond = plt.Polygon(
                    [[x, y + 0.5], [x + 0.5, y], [x, y - 0.5], [x - 0.5, y]],
                    color=color,
                    edgecolor=None
                )
                ax.add_patch(diamond)

elif mode == "من تدرج لوني":
    colormap = st.selectbox("اختر نظام الألوان:", [
        "viridis", "plasma", "inferno", "magma", "cividis", "cool", "hot", "spring", "summer", "autumn"
    ])
    cmap = plt.get_cmap(colormap)
    for i in range(size):
        for j in range(size):
            value = 1 - (i / size)
            color = cmap(value)
            x, y = j, -i
            diamond = plt.Polygon(
                [[x, y + 0.5], [x + 0.5, y], [x, y - 0.5], [x - 0.5, y]],
                color=color,
                edgecolor=None
            )
            ax.add_patch(diamond)

plt.xlim(-1, size + 1)
plt.ylim(-size - 1, 1)
plt.gca().invert_yaxis()
plt.tight_layout()

st.pyplot(fig)

# === Download image button ===
buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=300)
buffer.seek(0)
st.download_button(
    label="💾 تحميل الصورة النهائية",
    data=buffer,
    file_name="diamond_pattern_from_logo_or_gradient.png",
    mime="image/png"
)
