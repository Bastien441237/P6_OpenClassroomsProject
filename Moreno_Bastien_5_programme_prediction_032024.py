import streamlit as st
from PIL import Image
import requests

st.title("API pour prédire la race d'un chien via une image")

upload = st.file_uploader("Charger l'image du chien :", type=['png', 'jpeg', 'jpg'])

c1, c2 = st.columns(2)

if upload:
    files = {"file": upload.getvalue()}

    req = requests.post("http://127.0.0.1:8080/predict", files=files)
    
    if req.status_code == 200:
        resultat = req.json()
        pred_label = resultat['prediction']['label']
        pred_proba = resultat['prediction']['probability']
        
        c1.image(Image.open(upload))
        c2.write(f"Ce chien est un {pred_label} à {pred_proba*100:.2f}% !")
    else:
        st.error("Une erreur s'est produite lors de la prédiction.")