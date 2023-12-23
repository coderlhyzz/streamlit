import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import time
from streamlit_card import card
import base64



def NRSS(file):  # 画质评价算法
    import cv2
    import numpy as np
    from skimage.metrics import structural_similarity as compare_ssim

    image = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_GRAYSCALE)
    Ir = cv2.GaussianBlur(image, (7, 7), 0)

    x = cv2.Sobel(image, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(image, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)  # 转回uint8
    absY = cv2.convertScaleAbs(y)

    G = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    x = cv2.Sobel(Ir, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(Ir, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)  # 转回uint8
    absY = cv2.convertScaleAbs(y)

    Gr = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    (h, w) = G.shape
    G_blk_list = []
    Gr_blk_list = []
    sp = 6
    for i in range(sp):
        for j in range(sp):
            G_blk = G[int((i / sp) * h):int(((i + 1) / sp) * h), int((j / sp) * w):int(((j + 1) / sp) * w)]
            Gr_blk = Gr[int((i / sp) * h):int(((i + 1) / sp) * h), int((j / sp) * w):int(((j + 1) / sp) * w)]
            G_blk_list.append(G_blk)
            Gr_blk_list.append(Gr_blk)

    sum = 0
    for i in range(sp * sp):
        mssim = compare_ssim(G_blk_list[i], Gr_blk_list[i])
        sum = mssim + sum

    nrss = sum / (sp * sp * 1.0)

    return nrss


@st.cache_data
def load_lottie(url):
    return url


col1, col2 = st.columns([1, 2])

with col1:
    st_lottie(load_lottie("https://lottie.host/39579496-a625-4f8e-b97e-db60e6d5fa92/hQmgjnR8j6.json"), height=210,
              key='lottie1')

with col2:
    st.image("./assets/photo/schoolsign2.png", width=600)

st.markdown("# 画质评价界面")

with open('assets/photo/magnifying-glass.jpg', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")

col1, col2 = st.columns(2)

with col1:
    hasClicked = card(
      title="画质评价",
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

    st.write("###### 画质评价功能界面。")

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

    button1 = st.button("开始画质评价", key="button1")

    # st.image('./assets/description.png',width=600)
with col2:
    st.markdown(
        "### 画质评价分数:100::"
    )

    if button1:
        if uploaded_file is None:
            st.error('请先上传一张图片！')
            st_lottie(load_lottie("https://lottie.host/2a5e9877-b889-42e2-bb68-aa8141f53ab7/imZr1xbQOy.json"),
                      height=200, key='lottie2', loop=False)
        else:
            with st.spinner('正在运行中.....'):
                time.sleep(5)

            output = NRSS(file_contents)
            st.write(output)

            st.success('画质评价成功!')
            st_lottie(load_lottie("https://lottie.host/df388a60-5850-4dbd-9101-9376360fb317/fCFnGi32zD.json"),
                      height=200, key='lottie3', loop=False)
