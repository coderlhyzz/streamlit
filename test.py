# Streamlit Image-Comparison Component Example

import streamlit as st
from streamlit_image_comparison import image_comparison

# set page config
st.set_page_config(page_title="Image-Comparison Example", layout="centered")

# render image-comparison


image_comparison(
    img1="./assets/photo/r1.png",
    img2="./assets/photo/r0.png",
    label1="text1",
    label2="text1",
    width=700,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)