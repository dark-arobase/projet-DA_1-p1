```mermaid
classDiagram
    class Question {
        - texte
        - options[]
        - bonneReponse
        + verifierReponse()
    }

    class Quiz {
        - listeQuestions[]
        - score
        - difficulte
        + demarrer()
        + afficherQuestion()
        + calculerScore()
    }

    class Partie {
        - quiz
        - joueur
        - score
        + jouer()
        + finir()
    }

    class BanqueQuestions {
        - toutesQuestions[]
        + ajouterQuestion()
        + supprimerQuestion()
        + modifierQuestion()
    }

    Partie --> Quiz
    Quiz --> Question
    Quiz --> BanqueQuestions
```


```mermaid
graph TD
    Joueur -->|Choisir catégorie/difficulté| Systeme
    Joueur -->|Jouer une partie| Systeme
    Joueur -->|Répondre aux questions| Systeme
    Joueur -->|Voir score final| Systeme
    Admin -->|Ajouter/Modifier/Supprimer questions| Systeme
```
```mermaid
sequenceDiagram
    Joueur->>Systeme: Sélectionner réponse
    Systeme->>Systeme: Vérifier réponse
    Systeme->>Joueur: Afficher feedback correct/incorrect
    Systeme->>Systeme: Passer à la question suivante
```
```mermaid
sequenceDiagram
    Systeme->>Systeme: Calculer score final
    Systeme->>Joueur: Afficher score final et nombre de bonnes réponses
    Joueur->>Systeme: Rejouer ou retour à l'accueil
```

``````mermaid
flowchart TD
    A[Début du Quiz] --> B{Sélectionner la difficulté}
    B -->|Facile| C[Charger questions faciles]
    B -->|Moyen| D[Charger questions moyennes]
    B -->|Difficile| E[Charger questions difficiles]
    C --> F[Afficher question 1]
    D --> F
    E --> F
    F --> G{Réponse correcte?}
    G -->|Oui| H[Incrémenter score]
    G -->|Non| I[Afficher bonne réponse]
    H --> J{Plus de questions?}
    I --> J
    J -->|Oui| F
    J -->|Non| K[Afficher score final]
    K --> L[Fin du Quiz]
```