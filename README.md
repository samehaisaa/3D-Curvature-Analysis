# 3D Curvature Analysis

## Description
Ce projet vise à calculer et visualiser différentes courbures d'objets 3D en utilisant des techniques basées sur des maillages et des bibliothèques comme VTK. Les types de courbures supportés incluent :
- **Courbure de Gauss** : Indique les variations locales de la surface.
- **Courbure Moyenne** : Représente la courbure globale d'une zone donnée.
- **Courbure Maximale et Minimale** : Déduites des courbures principales.

## Fonctionnalités
Le programme propose les options suivantes via une interface CLI :
1. Calculer la **Courbure de Gauss** : Identifie les zones convexes et concaves.
2. Calculer la **Courbure Moyenne** : Visualise la forme globale.
3. Calculer la **Courbure Maximale** : Met en évidence les sommets les plus courbés.
4. Calculer la **Courbure Minimale** : Analyse les zones moins courbées.
5. Quitter le programme.

## Dépendances
- **VTK (Visualization Toolkit)** pour la gestion des maillages et des calculs.
- **C++ Standard Library** pour l'implémentation.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/samehaisaa/3D-Curvature-Analysis.git
