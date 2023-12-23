import streamlit as st
from PIL import Image
import base64
import time
from streamlit_lottie import st_lottie
from streamlit_card import card
from streamlit_image_comparison import image_comparison

@st.cache_data
def load_lottie(url):
    return url

def noise(img): #图片生成噪声点，用于复原增强模块的噪声图片的素材
    import numpy as np
    out = img
    rows, cols, chn = img.shape
    for i in range(50000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        out[x, y, :] = 255
    return out


col1, col2 = st.columns([1,2])

with col1:
    st_lottie(load_lottie("https://lottie.host/86b18307-f314-4b22-91b3-d654c7585d38/nHC9rlIeCD.json"),height=200, key='lottie1')

with col2:
    st.image("./assets/photo/schoolsign2.png", width=600)

st.markdown("# 复原增强界面")

with open('assets/photo/denoising.png', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")

col1, col2 = st.columns(2)

with col1:
    hasClicked = card(
      title="复原增强",
      text="Restoration enhancement",
      image=data,
      on_click=None,
      url=None,
      styles={
            "card": {
                "width": "500px",
                "height": "350px",
                "float" : "left",
                "margin-top":"-30px",
                "margin-left": "-40px",

            },
            "text": {
                "font-family": "STXingKai",
                "font-size":"36px",
              },
          "filter": {
              "background-color": "rgba(0, 0, 0, 0.5)"  # <- make the image not dimmed anymore

             }
          }
    )
with col2:
    st.write("###### 复原增强功能界面。")


image_comparison(
    img1='./assets/photo/ori_img.png',
    img2='./assets/photo/enhance_img.jpg',
    label1="复原前图像",
    label2="复原后图像",
    width=800,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)


def enhance(file): #图片复原增强算法
    import cv2
    import numpy as np
    # ori_img=cv2.imread(img_path)
    ori_img = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)
    # 中值滤波，中值滤波会取当前像素点及其周围临近像素点（一共有奇数个像素点）的像素值，将这些像素值排序，然后将位于中间位置的像素值作为当前像素点的像素值。
    result4 = cv2.medianBlur(ori_img, 3)
    return result4

st.markdown(
    "### 请上传一张照片:frame_with_picture:"
)
uploaded_file = st.file_uploader("",type=['jpg', 'png', 'jpeg'])

col1, col2 = st.columns(2)

with col1:
        st.write("#### 复原前图像")
        if uploaded_file is not None:

            st.image(uploaded_file, width=500, caption="image")
            file = uploaded_file.read()
        button1 = st.button("开始图像复原", key="button1")

with col2:
         st.write("#### 复原后图像")
         if button1:
             if uploaded_file is None:
                st.error('请先上传一张图片！')
                st_lottie(load_lottie("https://lottie.host/2a5e9877-b889-42e2-bb68-aa8141f53ab7/imZr1xbQOy.json"), height=200,key='lottie2', loop=False)
             else:
                with st.spinner('正在运行中.....'):
                    time.sleep(5)

                output=enhance(file)
                st.image(output, width=500, caption="image",channels="BGR")

                st.success('图像复原成功!')
                st_lottie(load_lottie("https://lottie.host/df388a60-5850-4dbd-9101-9376360fb317/fCFnGi32zD.json"), height=200,key='lottie3', loop=False)




