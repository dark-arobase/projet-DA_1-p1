Yuppiquiz/
├── data/                             # Données de quiz, utilisateurs, etc.
│   ├── utilisateurs.csv
│   ├── quiz.csv
│   ├── questions.json
│   └── scores.json
│
├── src/
│   └── yuppiquiz/
│       ├── __main__.py              # Point d'entrée si on exécute le module
│       ├── __init__.py
│       ├── ui_main.py              # Lancement de l’interface
│       ├── accueil.py              # Interface d’accueil utilisateur
│       ├── connexion.py            # Interface de connexion
│       ├── inscription.py          # Interface d’inscription
│       ├── gestion_quiz.py         # Logique liée aux quiz
│       └── bd.py                   # Lecture/écriture des fichiers (CSV/JSON)
│
├── .gitignore
├── LICENSE                         # (MIT, GPL, etc.)
├── pyproject.toml                  # Configuration de projet (poetry ou setuptools)
├── README.md
└── structure.bash                  # Script pour générer cette structure
