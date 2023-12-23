import streamlit as st
from streamlit_lottie import st_lottie
from st_pages import add_page_title



col1, col2 = st.columns([1,2])

with col1:
    st_lottie("https://lottie.host/decff995-08fb-4846-8ba7-8f194b038392/OAfky5Mxr8.json",height=190, key='lottie1')

with col2:
    st.image("./assets/photo/schoolsign2.png", width=600)

st.markdown("# 超标预警界面")

