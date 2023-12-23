from st_pages import add_page_title
from PIL import Image
import time
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline



@st.cache_data
def load_lottie(url):
    return url

st_lottie(load_lottie("https://lottie.host/14d97a04-78ef-4451-8215-911d8c1d0170/crBJh6TV0c.json"),key="lottie1")

st.markdown("# 系统综述界面")

st.subheader('系统介绍')
with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
        #st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json", height=300, key='lottie2')
        st_lottie(load_lottie("https://lottie.host/727056b6-8b9d-4c48-bc0e-3b3160d20a2d/GkEGY0XOfd.json"), width=400,height=400, key='lottie2',quality="high")
    with col2:
       st.write("##### 欢迎来到北京工业大学建工材料监控系统!")
       st.write("###### 在我国，建筑工程在城市化建设中占据着越来越重要的作用。"
                "而建筑工程材料检测手段对整体建筑工程来讲非常关键，认识到建筑材料检测对建筑行业以及社会经济体制的发展具有良好的复制作用。")
st.divider()

st.subheader('系统功能')
with st.container():

       st.write("欢迎来到北京工业大学建工材料监控系统！")
       st.image("./assets/photo/description2.png")
st.divider()

st.subheader('操作流程')
with st.container():
    with st.spinner(text="Building line"):
        with open('timeline.json', "r",encoding='utf-8') as f:
            data = f.read()
            timeline(data, height=500)
st.divider()

st.subheader('网站设计')
with st.container():
    col1,col2=st.columns(2)
    with col1:
        st.image("./assets/photo/schoolsign2.png", width=490)
    with col2:
        st.image("./assets/photo/logo.png", width=510)