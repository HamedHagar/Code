
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Change your picture into Daimonds", layout="centered")

st.title("🎨 Change your picture into Daimonds")

uploaded_file = st.file_uploader("ارفع صورة JPG أو PNG", type=["jpg", "png", "jpeg"])

resize_size = st.slider("درجة التجريد (عدد المربعات):", 10, 100, 50)

if uploaded_file:
    image = Image.open(uploaded_file).convert('L')
    image = image.resize((resize_size, resize_size))
    pixels = np.array(image)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.axis('off')

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

    plt.xlim(-1, pixels.shape[1] + 1)
    plt.ylim(-pixels.shape[0] - 1, 1)
    plt.gca().invert_yaxis()
    plt.tight_layout()

    st.pyplot(fig)
