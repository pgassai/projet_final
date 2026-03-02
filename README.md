# Projet Final – Réduction de Dimension & Docker

**Contexte**

Ce projet a pour objectif de simuler un projet collaboratif de data science en utilisant Git/GitHub pour le développement en équipe, avec gestion des branches, commits et fusions vers la branche principale *main*.

Chaque étudiant développe une méthode de réduction de dimension dans une branche dédiée (PCA, t-SNE ou UMAP), puis les contributions sont intégrées dans main.
Le projet est ensuite conteneurisé avec Docker afin de permettre l’exécution d’un script comparant les différentes méthodes.

├── data/
│   └── dataset.csv
│
├── notebooks/
│   ├── pca.ipynb
│   ├── tsne.ipynb
│   └── umap.ipynb
│
├── outputs/
│   ├── pca_2d.csv
│   ├── tsne_2d.csv
│   └── umap_2d.csv
│
├── evaluate.py
├── Dockerfile
└── README.md
