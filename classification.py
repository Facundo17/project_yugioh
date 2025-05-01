import streamlit as st
#from PIL import Image
import base64
from io import BytesIO
import matplotlib.pyplot as plt
#import plotly.express as px
import pandas as pd
import requests

st.set_page_config(page_title="Demo YuGiOh! Classifier", page_icon="📷", layout="wide")

# .stAppDeployButton elimina el botón que aparece por defecto en la esquina superior derecha
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        .stAppDeployButton {display:none;}
    </style>
    """,
    unsafe_allow_html=True
)

def process_image(file):
    """Pasar la imagen al API

    Args:
        file (UploadedFile): La imagen de una carta

    Returns:
        JSONResponse: Devuelve el resultado si se procesó correctamente, caso contrario, un error
        content: { label, monster, confidence }
    """
    url = 'http://localhost:8000/predict/'
    file = { 'file': file.getvalue() }
    return requests.post(url, files=file)


def show_content():
    st.markdown("# 📸 Card Detection")
   
    st.subheader("🖼️ Image analysys")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        response = process_image(uploaded_file)
        print(response.content)
            
                 
show_content()