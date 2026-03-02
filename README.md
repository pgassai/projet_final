---
title: "Projet Final – Réduction de Dimension & Docker"
author: "GASSAI-LEPOMA Precy, GIMENEZ Marine, PICAVET Giovanni"
date: "`r Sys.Date()`"
output:
  html_document:
    toc: true
    toc_depth: 3
---

# 📊 Contexte du projet

Ce projet a pour objectif de simuler un projet collaboratif de data science en utilisant **Git/GitHub** pour gérer le développement via des branches, commits et fusions vers la branche principale `main`.

Chaque étudiant développe une méthode de réduction de dimension (PCA, t-SNE ou UMAP) dans une branche dédiée.  
Une fois les contributions fusionnées, le projet est conteneurisé avec **Docker** afin de permettre l’exécution d’un script comparant les différentes méthodes.

---

# 🎯 Objectifs

- Implémenter une méthode de réduction de dimension
- Projeter les données en 2D
- Visualiser les résultats
- Exporter les coordonnées 2D
- Comparer les méthodes via la métrique **trustworthiness**
- Dockeriser le projet pour assurer la reproductibilité

---

# 🗂 Structure du projet


---

# 🧠 I. Réduction de dimension

Chaque méthode a été développée dans une branche dédiée avec au moins deux commits.

Dans chaque notebook :

- Chargement et prétraitement des données
- Projection en 2 dimensions
- Visualisation 2D
- Rédaction d’une courte observation sur la structure obtenue
- Export des données réduites en 2D

## Méthodes implémentées

- PCA  
- t-SNE  
- UMAP  

---

# 📏 II. Comparaison des méthodes

Le script `evaluate.py` :

1. Charge les embeddings 2D exportés
2. Calcule la métrique **trustworthiness**
3. Compare les scores obtenus pour chaque méthode

## 🔎 Trustworthiness

La trustworthiness mesure la capacité d’une méthode de réduction de dimension à préserver les relations de voisinage locales :

- Valeur proche de **1** → bonne préservation de la structure locale
- Valeur faible → déformation importante des voisinages

---

# 🐳 III. Dockerisation

Un `Dockerfile` est présent à la racine du projet.

Le conteneur permet d’exécuter directement le script de comparaison.

Repository GitHub : https://github.com/pgassai/projet_final/
DockerHub : [Lien à insérer]

