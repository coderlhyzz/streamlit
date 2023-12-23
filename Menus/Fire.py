import streamlit as st
from streamlit_lottie import st_lottie
import time
from streamlit_card import card
import base64


@st.cache_data
def load_lottie(url):
    return url


col1, col2 = st.columns([1, 2])

with col1:
    st_lottie(load_lottie("https://lottie.host/029f8489-270a-40cc-8346-e8df0b8b6ee5/yeaJsKYJMk.json"), height=210,
              key='lottie1')

with col2:
    st.image("./assets/photo/schoolsign2.png", width=600)

st.markdown("# 火焰定位界面")

with open('assets/photo/fire.jpg', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")

col1, col2 = st.columns(2)

with col1:
    hasClicked = card(
      title="火焰定位",
      text="Image quality evaluation",
      image=data,
      on_click=None,
      url=None,
        styles={
            "card": {
                "width": "450px",
                "height": "350px",
                "float": "left",
                "margin-top": "-30px",
                "margin-left": "-40px",

            },
            "text": {
                "font-family": "STXingKai",
                "font-size": "36px",
            },
            "filter": {
                "background-color": "rgba(255, 255, 244, 255)"  # <- make the image not dimmed anymore

            }
        }
    )
with col2:

    st.write("###### 火焰定位功能界面。")

st.divider()

st.markdown(
    "### 请上传一张照片:frame_with_picture:"
)

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)

with col1:
    st.write("#### 图像")
    if uploaded_file is not None:
        st.image(uploaded_file, width=500, caption="image")
        file_contents = uploaded_file.read()

    button1 = st.button("开始火焰定位", key="button1")

    # st.image('./assets/description.png',width=600)
with col2:
    st.write("#### 定位后图像")
    if button1:
        if uploaded_file is None:
            st.error('请先上传一张图片！')
            st_lottie(load_lottie("https://lottie.host/2a5e9877-b889-42e2-bb68-aa8141f53ab7/imZr1xbQOy.json"),
                      height=200, key='lottie2', loop=False)
        else:
            with st.spinner('正在运行中.....'):
                time.sleep(5)

       #     output = enhance(file)
            st.image("./assets/photo/located_fire.png", width=500, caption="image", channels="BGR")

            st.success('图像复原成功!')
            st_lottie(load_lottie("https://lottie.host/df388a60-5850-4dbd-9101-9376360fb317/fCFnGi32zD.json"),
                      height=200, key='lottie3', loop=False)

