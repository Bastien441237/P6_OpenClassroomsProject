# 🐕 Classification d'Images à l'aide d'Algorithmes de Deep Learning

Bienvenue dans le repository du projet **Classification d'Images à l'aide d'Algorithmes de Deep Learning**. Ce projet vise à développer un algorithme capable de classifier les races de chiens à partir de photos, afin d'aider l'association de protection des animaux Le Refuge à gérer leur base de données d'images.

## 📚 Contexte du Projet

Vous êtes bénévole pour l'association Le Refuge et souhaitez les aider à classer les images de leurs pensionnaires. Leur base de données de pensionnaires commence à s'agrandir et ils n'ont pas toujours le temps de référencer les images des animaux qu'ils ont accumulées. L'objectif est de créer un algorithme capable de détecter la race du chien sur une photo pour accélérer leur travail d'indexation.

## 🎯 Objectifs du Projet

1. **Prétraitement des images** : Utiliser des techniques de whitening, equalization et de modification de la taille des images, ainsi que la data augmentation.
2. **Développement d'un modèle CNN personnalisé** : S'inspirer de réseaux CNN existants, entraîner un premier modèle, puis l'améliorer en optimisant certains hyperparamètres.
3. **Utilisation de modèle pré-entraînés avec ou sans transfer learning** : Adapter et réentraîner un réseau déjà existant pour la classification des races de chiens.
4. **Démonstration de la prédiction** : Créer une application locale (Streamlit) qui prend des images de chiens en entrée et retourne les races prédites.
5. **Déploiement en production** : Préparer la solution pour être déployée par les bénévoles de l'association.

## 📦 Livrables

1. **Notebook de prétraitement d'images** : Analyse et prétraitement des images.
2. **Notebook de création et d’entraînement du modèle CNN personnalisé** : Simulations des différentes valeurs des hyperparamètres et de data augmentation.
3. **Notebook d’entraînement des modèles avec Transfer Learning**.
4. **Programme de prédiction** : Exécution locale via API Streamlit pour prédire les races de chiens à partir des images.
5. **Support de présentation** : Présentation à destination du bénévole responsable de la base de données, incluant les étapes pour déployer la solution en production.

## 📂 Structure du Repository

```plaintext
├── Images/                                                             # Dossier contenant les données brutes
│   ├── Stanford_Dogs_Dataset/                                          # Images des chiens
├── Moreno_Bastien_1_notebook_pretraitement_032024.ipynb                # Prétraitement des images
├── Moreno_Bastien_2_notebook_model_perso_032024.ipynb                  # Création et entraînement du modèle CNN personnalisé
├── Moreno_Bastien_3_notebook_model_transfer_learning_032024.ipynb      # Entraînement des modèles avec Transfer Learning
├── Moreno_Bastien_4_programme_prediction_032024.py                     # Fichier de l'API Flask
├── Moreno_Bastien_5_programme_prediction_032024.py                     # Fichier de l'application Streamlit
├── Moreno_Bastien_6_presentation_032024.pdf                            # Support de présentation
├── index_to_class.pkl                                                  # Dictionnaire classe / index pour traduire les prédictions du modèle Xception
├── xception_model.h5                                                   # Modèle Xception
├── README.md                                                           # Ce fichier
```

## 🧑‍💻 Utilisation
### Prétraitement des Images
Pour prétraiter les images, exécutez le notebook `Moreno_Bastien_1_notebook_pretraitement_032024.ipynb`.

### Entraînement du modèle CNN personnalisé
Pour réentraîner ou optimiser le modèle personnalisé, exécutez le notebook `Moreno_Bastien_2_notebook_model_perso_032024.ipynb`.

### Entraînement avec Transfer Learning
Pour réentraîner ou optimiser les modèles pré-entraîner avec ou sans Transfer Learning, exécutez le notebook `Moreno_Bastien_3_notebook_model_transfer_learning_032024.ipynb`.

### Démonstration avec Streamlit
Pour exécuter l'application Streamlit, utilisez l'API Flask Backend : `Moreno_Bastien_4_programme_prediction_032024.py`.

```
python Moreno_Bastien_4_programme_prediction_032024.py
```

Puis exécutez `Moreno_Bastien_5_programme_prediction_032024.py`.

```
streamlit run Moreno_Bastien_5_programme_prediction_032024.py
```

## 👨‍💻 Auteur
Bastien Moreno - Data Scientist et passionné par l'analyse de données et le développement de modèles intelligents.\
Pour en savoir plus sur moi et mes projets, n'hésitez pas à me contacter via mon [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bastien-moreno441237/).
