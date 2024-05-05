import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Charger votre modèle
model = load_model("model04_augm25_epoch.h5")  # Assurez-vous de spécifier le bon chemin

def evaluate(img_fname):
    # Charger l'image avec les bonnes dimensions
    img = image.load_img(img_fname, target_size=(256, 256))
    # Convertir l'image en tableau numpy et normaliser les valeurs de pixel
    x = image.img_to_array(img) / 255.0
    # Ajouter une dimension supplémentaire pour correspondre à la forme attendue par le modèle
    x = np.expand_dims(x, axis=0)
    # Faire une prédiction avec le modèle
    preds = model.predict(x)
    # Afficher les probabilités et les noms de catégorie pour les 2 catégories
    print('Prédictions:', preds)
    # Calculer les pourcentages de prédiction
    percent_cat = preds[0][1] * 100
    percent_dog = preds[0][0] * 100
    # Formater les pourcentages de prédiction
    percent_cat_str = "{:.2f}".format(percent_cat)
    percent_dog_str = "{:.2f}".format(percent_dog)
    return percent_cat_str, percent_dog_str




def upload_and_predict_page():
    st.title("Page de chargement de l'image et de restitution des prédictions")
    
    uploaded_file = st.file_uploader("Choisissez une image ...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Image chargée.', use_column_width=True)
        prediction = evaluate(uploaded_file)
        if prediction[0] > prediction[1]:
                prediction=("C'est un Chat.")
        else:
                prediction=("C'est un Chien.")
        st.write("Prédiction:", prediction)
        percent_cat, percent_dog = evaluate(uploaded_file)
        st.write("Détails :")
        st.write("- Pourcentage de prédiction pour chat:", percent_cat, "%")
        st.write("- Pourcentage de prédiction pour chien:", percent_dog, "%")