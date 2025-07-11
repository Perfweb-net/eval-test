# TaskManager

## Présentation

TaskManager est un module Python complet de gestion de tâches, conçu pour illustrer les bonnes pratiques de tests, d’organisation et d’automatisation logicielle. Il permet de créer, organiser, filtrer, sauvegarder et charger des tâches, de générer des rapports et d’envoyer des notifications (mockées).

---

## Fonctionnalités principales
- Créer, modifier, supprimer des tâches
- Organiser les tâches par priorité et projet
- Marquer les tâches comme terminées
- Sauvegarder/charger les tâches au format JSON
- Générer des statistiques et des rapports quotidiens
- Envoyer des notifications par email (simulation/mock)

---

## Structure du projet
```
├── src/
│   └── task_manager/
│       ├── __init__.py
│       ├── task.py         # Entité principale (Task, Priority, Status)
│       ├── manager.py      # Gestionnaire de tâches
│       └── services.py     # Services externes (Email, Rapport)
├── tests/
│   ├── test_task.py        # Tests unitaires Task
│   ├── test_manager.py     # Tests unitaires/integration Manager
│   ├── test_services.py    # Tests unitaires/integration Services
├── demo.py                 # Script de démonstration
├── requirements.txt        # Dépendances
├── Makefile                # Commandes de build/test/lint/coverage
├── pytest.ini              # Configuration Pytest
└── .github/workflows/      # CI/CD GitHub Actions
```

---

## Installation

1. **Cloner le dépôt**
```sh
git clone <url-du-repo>
cd <nom-du-repo>
```
2. **Installer les dépendances**
```sh
make install
```

---

## Utilisation

### Exemple minimal (dans un script Python)
```python
from src.task_manager.manager import TaskManager
from src.task_manager.task import Priority

manager = TaskManager()
id1 = manager.add_task("Ma tâche", "Description", Priority.HIGH)
manager.get_task(id1).mark_completed()
manager.save_to_file()
```

### Lancer la démonstration
```sh
python3 demo.py
```

---

## Exemples de tests

- **Lancer tous les tests**
  ```sh
  make test
  ```
- **Lancer les tests unitaires**
  ```sh
  make test-unit
  ```
- **Lancer les tests d’intégration**
  ```sh
  make test-integration
  ```
- **Vérifier la couverture**
  ```sh
  make coverage
  # Ouvre htmlcov/index.html pour un rapport détaillé
  ```
- **Vérifier la syntaxe**
  ```sh
  make lint
  ```

---

## Couverture & Qualité
- Couverture de code : **100%** sur tout le module (`make coverage`)
- Linting syntaxique : `make lint`
- CI/CD : GitHub Actions (tests, lint, coverage à chaque push/PR)

---

## Mocking & Tests avancés
- Les dépendances externes (fichiers, email, date) sont **mockées** dans les tests pour garantir l’isolation et la rapidité.
- Les tests couvrent tous les cas d’erreur, de succès, et les cas limites.

---

## CI/CD
- Le workflow `.github/workflows/test.yml` automatise :
  - L’installation des dépendances
  - Le lint
  - Les tests (unitaires & intégration)
  - La couverture de code

---

## Contact
Pour toute question ou suggestion, contactez :
- **Auteur** : [Pierre]
- **Email** : [pierre.saugues@free.fr]

---

Bon développement et bonne gestion de vos tâches ! 🚀 