import time
from streamlit_cropper import st_cropper
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from st_vizzu import *
import pandas as pd
from streamlit_card import card
import base64

@st.cache_data
def load_lottie(url):
    return url

uploaded_file = st.sidebar.file_uploader(label='上传图片', type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox(label="裁剪图片实时更新", value=True)
box_color = st.sidebar.color_picker(label="裁剪框颜色", value='#0000FF')
aspect_choice = st.sidebar.radio(label="裁剪框比例", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
    "2:3": (2, 3),
    "Free": None
}
button1 = st.sidebar.button("开始图像复原", key="button1")
aspect_ratio = aspect_dict[aspect_choice]

col1, col2 = st.columns([1,2])

with col1:
    st_lottie(load_lottie("https://lottie.host/290c5745-77ad-4337-9987-18f08051ade3/UAuUZwy3wl.json"),height=185, key='lottie1')

with col2:
    st.image("./assets/photo/schoolsign2.png", width=650)

st.markdown("# 烟粒检测界面")

with open('assets/photo/factory_smoke.jpg', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")

col1, col2 = st.columns(2)

with col1:
    hasClicked = card(
      title="烟粒检测",
      text="Smoke particle detection",
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
              "background-color": "rgba(255, 255, 244, 255)"  # <- make the image not dimmed anymore

             }
          }
    )
with col2:
    st.write("###### 烟粒检测功能界面。")

def predict_codeReconition(cropped_img):
    from torchvision import transforms
    from torchvision.models import AlexNet
    import json
    import torch

    data_transform = transforms.Compose(  # 定义图片预处理函数，用来对载入图片进行预处理操作
        [transforms.Resize((224, 224)),
         transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])  # 标准化处理

    img = data_transform(cropped_img)
    img = torch.unsqueeze(img, dim=0)
    try:
        json_path = './class_indices.json'  # 包含了类别标签和索引的对应关系
        json_file = open(json_path, "r")
        class_indict = json.load(json_file)
    except Exception as e:
        print(e)
        exit(-1)

    model = AlexNet(num_classes=5)
    weights_path = "./AlexNet.pth"
    ckpt = torch.load(weights_path)  # 加载该路径下的权重文件ckpt

    try:
        model.load_state_dict(ckpt)
    except RuntimeError as e:
        print('Ignoring "' + str(e) + '"')

    model.eval()  # 代码将模型设置为评估模式

    with torch.no_grad():  # 使用torch.no_grad()上下文来关闭梯度计算，以提高执行效率
        output = torch.squeeze(model(img))  # 将图片通过model正向传播，得到输出，将输入进行压缩，将batch维度压缩掉，得到最终输出（out）
        predict = torch.softmax(output, dim=0)  # 经过softmax处理后，就变成概率分布的形式了
        predict_cla = torch.argmax(predict).numpy()  # 通过argmax方法，得到概率最大的处所对应的索引

    #print(class_indict[str(predict_cla)], predict[predict_cla].item())

    return class_indict[str(predict_cla)], predict[predict_cla].item()


st.markdown(
    "### 请上传一张照片:frame_with_picture:"
)
with st.container():
    st.write("#### 上传图片")

    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert('RGB')
        if not realtime_update:
            st.write("裁剪完后请双击来保存图片")

        cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                 aspect_ratio=aspect_ratio)

        col1, col2 = st.columns(2)

        with col1:
                st.write("#### 被检测图像")

                st.image(cropped_img, width=450)
                #st.image('./assets/description.png',width=600)
        with col2:
            st.write("#### 烟粒检测结果")
            if button1:
                if uploaded_file is None:
                    st.error('请先上传一张图片！')
                    st_lottie(load_lottie("https://lottie.host/2a5e9877-b889-42e2-bb68-aa8141f53ab7/imZr1xbQOy.json"), height=200,key='lottie2', loop=False)
                else:
                    with st.status("加载图像中...", expanded=True) as status:
                        time.sleep(5)
                        st.write("正在进行烟粒检测...")
                        time.sleep(3)
                        st.write("正在进行准确率判断...")
                        time.sleep(3)
                        status.update(label="运行完成！", state=None, expanded=False)

                    output1,output2 = predict_codeReconition(cropped_img)
                    st.markdown(
                        "### 烟粒检测结果:100::"
                    )
                    st.write(output1)
                    st.markdown(
                        "### 识别准确率:100::"
                    )
                    st.write(f'{round(output2,3)*100}%')

                    st.success('画质评价成功!')
                    st_lottie(load_lottie("https://lottie.host/df388a60-5850-4dbd-9101-9376360fb317/fCFnGi32zD.json"), height=200,key='lottie3', loop=False)

st.divider()  # 👈 Draws a horizontal rule

# Load Data
df = pd.read_csv("assets/data/music_data.csv", index_col=0)
# Create ipyvizzu Object with the DataFrame
obj = create_vizzu_obj(df)

# Preset plot usage. Preset plots works directly with DataFrames.
bar_obj = bar_chart(df,
            x = "Kinds",
            y = "Popularity",
            title= "1.Using preset plot function `bar_chart()`"
            )

# Animate with defined arguments
anim_obj = beta_vizzu_animate( bar_obj,
    x = "Genres",
    y =  ["Popularity", "Kinds"],
    title = "Animate with beta_vizzu_animate () function",
    label= "Popularity",
    color="Genres",
    legend="color",
    sort="byValue",
    reverse=True,
    align="center",
    split=False,
)

# Animate with general dict based arguments
_dict = {"size": {"set": "Popularity"},
    "geometry": "circle",
    "coordSystem": "polar",
    "title": "Animate with vizzu_animate () function",
    }
anim_obj2 = vizzu_animate(anim_obj,_dict)

# Visualize within Streamlit
with st.container(): # Maintaining the aspect ratio
    st.button("重新加载动画")
    vizzu_plot(anim_obj2)


with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")