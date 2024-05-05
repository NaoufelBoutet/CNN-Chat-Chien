import streamlit as st
from home import home_page
import streamlit as st
from PIL import Image
import io
from predictionpage import upload_and_predict_page
from cnnexplain import cnn_explanation



def main():
    st.set_page_config(page_title="CNN Application", page_icon="🧠")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Pages", ["Page d'accueil", "Upload & Predict", "Explication CNN"])

    if page == "Page d'accueil":
        home_page()
    elif page == "Upload & Predict":
        upload_and_predict_page()
    elif page == "Explication CNN":
        cnn_explanation()
   



main()