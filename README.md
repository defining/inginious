# INGInious – Exemples d’exercices et guide de création

Ce dépôt GitHub a pour objectif de **centraliser, documenter et partager des exemples d’exercices INGInious**, ainsi qu’un **guide pas à pas** pour en créer de nouveaux.

👉 **Ce dépôt est volontairement perfectible** :  
il est destiné à être **amélioré, enrichi et corrigé par chacun** (assistants, enseignants, contributeurs).  
Toute contribution est la bienvenue (nouveaux exercices, corrections, améliorations du guide, bonnes pratiques, etc.).

---

## 🎯 Objectifs du dépôt

- Fournir un **point de départ clair** pour comprendre la structure d’un exercice INGInious
- Mettre à disposition des **exemples concrets fonctionnels**
- Faciliter l’**onboarding des nouveaux assistants**
- Harmoniser les pratiques entre exercices
- Servir de **base collaborative** pour les cours utilisant INGInious

---

## 📁 Structure du dépôt

### `exemples/`

Ce dossier contient :

- ✅ **Tous les fichiers nécessaires à la création d’un nouvel exercice INGInious**
- ✅ **Des exercices réels**, créés par les **assistants de l’UCLouvain – Saint-Louis**
- ✅ Une structure reproductible que vous pouvez **copier-coller** pour démarrer un nouvel exercice

Chaque sous-dossier correspond à **un exercice complet**, prêt à être importé ou recréé dans INGInious.

---

## 🛠️ Créer un exercice INGInious – Guide pas à pas

### 1️⃣ Accéder à INGInious

1. Aller sur 👉 https://inginious.info.ucl.ac.be/
2. Se connecter avec son compte
3. Dans le menu de gauche, cliquer sur **« Mes cours »**
4. Sélectionner le cours souhaité  
   _(ex. : **Fondements de l’informatique de gestion**)_
5. Cliquer sur **« Administration du cours »**
6. Aller dans **« Exercices »**

---

### 2️⃣ Créer un nouvel exercice

1. À côté de la liste des exercices, cliquer sur l’icône **☰ (menu burger)**
2. Sélectionner **« Ajouter des exercices »**
3. Donner un **titre**
4. Cliquer sur **« Créer un nouvel exercice »**
5. Cliquer sur **« Appliquer les changements »**

---

### 3️⃣ Éditer l’exercice

Cliquer sur l’exercice nouvellement créé, puis sur **« Éditer l’exercice »**.

---

## ⚙️ Onglets et paramètres importants

### 🧩 Onglet : *Paramètres de base*

- Nom de l’auteur (assistant / enseignant)
- Énoncé général de l’exercice
- L’énoncé est rédigé en **Markdown**

---

### 🧪 Onglet : *Environnement*

- **Type d’environnement** : `Conteneur standard`
- **Environnement de correction** : `Default`
- **Temps d’expiration** : `300 secondes`

---

### ❓ Onglet : *Sous-problèmes*

1. Dans **« Nouvel identifiant de problème »**, entrer : q1
2. Cliquer sur **« Ajouter »**
3. Cliquer sur le sous-problème créé (`q1`)
4. Définir :
- Le **titre de la question**
- L’**énoncé spécifique**
- Le **langage** (ex. : Python)

👉 C’est aussi ici que l’on configure le **message affiché juste avant que l’étudiant écrive son code**.

---

### 📂 Onglet : *Fichiers de l’exercice*

Un exercice minimal contient **au moins 4 fichiers** organisés comme suit :

```
/
├── run
├── src/
│   ├── Templates/
│   │   └── q
│   ├── TestQ.py
│   └── CorrQ.py
```

Détail des fichiers :

- `run`  
  Fichier situé **à la racine (`/`)**, utilisé par INGInious pour lancer la correction.

- `q`  
  Fichier template situé dans :
  ```
  /src/Templates/q
  ```
  C’est le fichier dans lequel l’étudiant écrit son code.

- `TestQ.py`  
  Fichier contenant les **tests unitaires**, situé dans :
  ```
  /src/
  ```

- `CorrQ.py`  
  Fichier contenant la **solution de référence**, utilisé par les tests, situé dans le même dossier que les tests.

Une fois tous les fichiers ajoutés ou modifiés, cliquer sur :

➡️ **« Appliquer les changements »**

---

## 👁️ Accessibilité de l’exercice

Après avoir créé et configuré l’exercice :

1. Revenir dans le menu **« Exercices »** (colonne de gauche)
2. Retrouver l’exercice dans la liste
3. Cliquer sur **« Paramètres de l’exercice »**
4. Dans la section **Accessibilité**, choisir :
   - **Toujours** → l’exercice est visible en permanence
   - **Personnalisé** → visibilité contrôlée par dates

⚠️ **Étape essentielle** :  
Si l’accessibilité n’est pas configurée, l’exercice peut rester invisible pour les étudiants.

---

## 📁 Dossier `exemples/`

Le dossier `exemples/` contient tous les fichiers nécessaires à la création d’un exercice type INGInious

Chaque sous-dossier correspond à **un exercice indépendant**, prêt à servir de modèle.

---
