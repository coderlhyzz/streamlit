import streamlit as st
import streamlit_book as stb

st.set_page_config(
    page_title="建工材料监控系统",
    page_icon="./assets/photo/schoolsign.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
)

stb.set_book_config(menu_title="系统功能",
                    menu_icon="info-square",
                    options=[
                            "系统综述",
                            "画质评价",
                            "复原增强",
                            "烟粒检测",
                            "超标预警",
                            "火焰定位",
                            ],
                    paths=[
                          "Menus/Home.py",
                          "Menus/NRSS.py",
                          "Menus/Enhance.py",
                          "Menus/Evaluate.py",
                          "Menus/Warning.py",
                          "Menus/Fire.py",
                          ],

                    save_answers=False,
               )
