# 🚀 Silence Orbital — Space Station Survival

> Jeu de survie en mode console, développé en Python orienté objet.  
> EPSI SN1 — Projet Transversal POO — Février/Mars 2026

---

## 🎮 Concept

Une station spatiale est envahie par des extraterrestres. Vous incarnez un équipage de **1 à 4 joueurs** qui doit survivre **15 jours** avant l'arrivée des secours.

Trois menaces simultanées à gérer :
- 👾 **Les aliens** qui attaquent le mur et les joueurs chaque round
- 🧱 **Le mur de sécurité** qui s'effrite à chaque attaque
- 💨 **L'oxygène** qui diminue inexorablement à chaque jour écoulé

---

## ⚙️ Installation et lancement

**Prérequis :** Python 3.8+, aucune dépendance externe.

```bash
# Cloner le projet
git clone <url-du-repo>
cd Silence_Orbital

# Lancer le jeu
python main.py
```

---

## 🕹️ Comment jouer

### 1. Choisir le nombre de joueurs (1 à 4)
Chaque joueur choisit un **nom** et une **classe** :

| Classe     | HP  | ATK | DEF | Soin passif |
|------------|-----|-----|-----|-------------|
| MEDIC      | 120 | 8   | 5   | 3 HP/tour   |
| ENGINEER   | 100 | 10  | 6   | 1 HP/tour   |
| SOLDIER    | 150 | 12  | 7   | 2 HP/tour   |

### 2. Chaque round, chaque joueur choisit une action

```
1. Ressources      → Améliorer une stat (attaque, défense, soin, mur, oxygène)
2. Attaquer        → Infliger des dégâts aux extraterrestres
3. Réparer le mur  → Restaurer les PV du mur de sécurité
4. Se soigner      → Récupérer des HP (repos)
```

> 💡 Les joueurs qui n'attaquent pas ce tour récupèrent automatiquement des HP en fin de round (soin passif).

### 3. Phase aliens
Après les joueurs, chaque alien attaque : **60% de chances** de viser le mur, **40%** de viser un joueur aléatoire.

### 4. Conditions de victoire / défaite

| Résultat  | Condition                                      |
|-----------|------------------------------------------------|
| ✅ Victoire | Survivre 15 rounds                            |
| ✅ Victoire | Éliminer tous les aliens                      |
| ❌ Défaite  | Le mur tombe à 0 HP                           |
| ❌ Défaite  | L'oxygène atteint 0%                          |
| ❌ Défaite  | Tout l'équipage est mort                      |

---

## 👾 Les ennemis

| Ennemi    | HP | ATK | Apparition                  |
|-----------|----|-----|-----------------------------|
| Parasite  | 20 | 4   | Rounds impairs (1, 3, 5...) |
| Dominant  | 60 | 12  | Tous les 5 rounds           |

Le nombre d'aliens spawnés est **proportionnel au nombre de joueurs** pour maintenir l'équilibre.

---

## 🏗️ Architecture du projet

```
Silence_Orbital/
├── main.py                  # Point d'entrée, intro animée, lancement
├── character/
│   ├── player.py            # Classes PlayerClass et Player
│   └── alien.py             # Classes Alien, Parasite, Dominant
├── station/
│   └── space_station.py     # Classe SpaceStation (mur + oxygène)
└── game/
    └── game.py              # Classe SpaceStationGame (moteur de jeu)
```

### Principes POO appliqués

- **Composition** : `Player` possède une `PlayerClass` (MEDIC, ENGINEER, SOLDIER) plutôt que d'en hériter, ce qui permet de modifier les stats en cours de partie sans toucher à l'archétype.
- **Héritage** : `Parasite` et `Dominant` héritent de `Alien` et ne redéfinissent que leurs stats et leur nom.
- **Encapsulation** : chaque objet gère son propre état via ses méthodes (`take_damage()`, `repair_wall()`, `loss_oxygen()`...).

---

## 🌿 Workflow Git

Le projet a été développé en binôme avec des branches nominatives :

```
main
├── Theo1.x    → développement côté Théo
└── Lola1.x    → développement côté Lola
```

Chaque fonctionnalité est développée sur une branche dédiée puis intégrée via **pull request** vers `main`.

---

## 🔭 Axes d'évolution envisagés

- **Persistance** : sauvegarde/reprise de partie via JSON ou SQLite
- **Interface Rich** : barres de vie animées, couleurs, tableaux en console
- **Sorts et équipements** : identité de classe plus marquée (notamment le Mage)
- **Équilibrage avancé** : ajustement fin des stats selon les retours de test

---

## 👥 Auteurs

Projet réalisé dans le cadre du cours de développement application objet Python — EPSI SN1.

Encadrant : **Geoffroy Ladrat** — geoffroy@gl-conseil.dev
