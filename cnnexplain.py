import streamlit as st

def cnn_explanation():
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>Introduction aux Réseaux de Neurones Convolutifs (CNN)</h1>", unsafe_allow_html=True)
    

    st.title("Qu'est-ce qu'un CNN ?")
    st.write("Un réseau de neurones convolutif (CNN) est un type spécial de réseau de neurones artificiels, inspiré par la façon dont le cerveau des animaux, en particulier les chats et les humains, traite la vision. L'idée principale est que ces réseaux peuvent apprendre à extraire automatiquement des caractéristiques importantes des images.")

    st.title("Mais en fait un neurone, c'est quoi ?")
    st.write("Dans un CNN, chaque 'neurone' est en réalité une petite unité de traitement qui prend une partie de l'image en entrée et lui applique une fonction mathématique pour détecter des motifs spécifiques, comme des bords ou des textures.")

    st.title("Des couches de neurones ?")
    st.write("Les neurones sont organisés en couches. Les trois principales couches dans un CNN sont :")
    st.write("-La couche de convolution: Cette couche applique des filtres pour détecter des motifs dans l'image. Par exemple, un filtre pourrait détecter les bords d'un objet.")
    st.write("-La couche de pooling: Cette couche réduit la dimension de l'image en sélectionnant les pixels les plus importants. Cela aide à réduire le temps de calcul et à rendre le modèle plus robuste.")
    st.write("-La couche entièrement connectée: Cette couche prend les caractéristiques extraites par les couches précédentes et les utilise pour classer l'image dans différentes catégories, comme 'chien' ou 'chat'.")

    st.title("Mais comment fonctionnent-elles ?")

    st.write("Fonctionnement de la couche de convolution:")
    st.write("Chaque neurone dans la couche de convolution est connecté à une petite région de l'image d'entrée, appelée 'fenêtre de réception' ou 'filtre'. Le neurone applique une opération de multiplication et d'addition à tous les pixels dans sa fenêtre de réception (une unité de base dans une image numérique). Cela crée une 'carte d'activation' qui met en évidence les endroits de l'image où le motif représenté par le filtre est présent.")

    st.write("Utilité de la couche de pooling:")
    st.write("La couche de pooling réduit la dimension de la carte d'activation en sélectionnant les valeurs les plus importantes. Cela rend la représentation de l'image plus petite et plus facile à gérer pour les couches suivantes du réseau. Le pooling aide également à rendre la représentation invariante à de petites translations dans l'image (il permet de reconnaître un motif quel que soit son emplacement exact dans l'image).")

    st.write("Fonctionnement de la couche entièrement connectée:")
    st.write("Dans cette couche, chaque neurone est connecté à tous les neurones de la couche précédente. Cela permet au réseau de combiner les caractéristiques extraites des différentes parties de l'image pour prendre une décision globale sur ce qu'elle représente. Pendant l'entraînement, les poids de ces connexions sont ajustés pour minimiser l'erreur de prédiction.")

    st.write("Apprentissage et optimisation:")
    st.write("Pendant l'entraînement, le réseau utilise un algorithme d'optimisation, tel que la descente de gradient stochastique, pour ajuster ses poids afin de minimiser une fonction de perte. La fonction de perte mesure à quel point les prédictions du réseau sont éloignées des étiquettes réelles des images. En ajustant itérativement les poids du réseau pour minimiser cette perte sur un ensemble de données d'entraînement, le réseau apprend à mieux reconnaître les motifs dans les images.")



    st.title("Apprentissage du modèle")
    st.write("Pour que le CNN apprenne à reconnaître les chiens, on lui montre des milliers d'images étiquetées de chiens et de chats. Pendant l'entraînement, le réseau ajuste les poids des neurones pour minimiser les erreurs entre les prédictions et les étiquettes réelles.")

    st.title("Prédiction du modèle")
    st.write("Une fois que le CNN a été entraîné, on lui donne une nouvelle image et il utilise les poids qu'il a appris pour faire une prédiction sur ce qu'il voit dans l'image.")

    st.title("Evaluation du modèle")
    st.write("Enfin, on évalue les performances du CNN en regardant à quel point ses prédictions correspondent aux étiquettes réelles des images qu'il n'a jamais vues auparavant. Si le CNN fait des prédictions précises, cela signifie qu'il a appris à reconnaître les chiens et chats avec succès.")

    

    st.title("Conclusion")
    st.write("En résumé, les CNN fonctionnent en extrayant des caractéristiques des images à différentes échelles et en les combinant pour prendre des décisions de classification. Ils sont particulièrement efficaces pour la reconnaissance d'images en raison de leur capacité à apprendre des représentations hiérarchiques des données.")
    