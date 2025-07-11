# TP Projet Final - Module de Gestion de Tâches

## Contexte du projet

Vous allez développer **TaskManager**, un module complet de gestion de tâches avec toutes les bonnes pratiques vues en cours :

- Tests unitaires et d'intégration
- Mocking des dépendances externes
- Organisation professionnelle du code
- Couverture de code et rapports
- Intégration continue

---

## Objectifs pédagogiques

- ✅ **Synthèse des concepts** : Appliquer tous les types de tests vus en cours
- ✅ **Projet réaliste** : Développer un module utilisable en conditions réelles
- ✅ **Autonomie** : Prendre des décisions techniques et les justifier
- ✅ **Qualité** : Atteindre des standards professionnels (95%+ couverture)

---

## Phase 1 : Analyse et conception

### Étape 1 : Comprendre le besoin

**Fonctionnalités requises :**
- Créer, modifier, supprimer des tâches
- Organiser les tâches par projet et priorité
- Marquer les tâches comme terminées
- Sauvegarder et charger depuis un fichier JSON
- Générer des statistiques sur les tâches
- Envoyer des notifications par email (simulé)

**Questions d'analyse :**
1. Quelles sont les entités principales ? (Tâche, Projet, Gestionnaire)
2. Quelles dépendances externes identifiez-vous ?
3. Quels cas d'erreur faut-il prévoir ?
4. Comment organiser le code pour faciliter les tests ?

---

### Étape 2 : Concevoir l'architecture

**Proposez une structure de projet en remplissant ce squelette :**

```text
task_manager_project/
├── src/
│   └── task_manager/
│       ├── __init__.py
│       ├── ????????.py # À définir : entité principale
│       ├── ????????.py # À définir : gestionnaire
│       └── ????????.py # À définir : services externes
├── tests/
│   ├── __init__.py
│   ├── test_???????.py # Tests unitaires
│   ├── test_???????.py # Tests d'intégration
│   └── fixtures/
│       └── sample_data.json
├── .github/workflows/
├── requirements.txt
└── ???????? # Autres fichiers nécessaires
```

**Mission :** Définissez les noms des fichiers et justifiez vos choix.

---

## Phase 2 : Développement dirigé

### Étape 3 : Implémenter l'entité Task

Créez `src/task_manager/task.py` en suivant ces spécifications :

```python
from datetime import datetime
from enum import Enum

class Priority(Enum):
    # TODO: Définissez les priorités (LOW, MEDIUM, HIGH, URGENT)
    pass

class Status(Enum):
    # TODO: Définissez les statuts (TODO, IN_PROGRESS, DONE, CANCELLED)
    pass

class Task:
    """Une tâche avec toutes ses propriétés"""

    def __init__(self, title, description="", priority=Priority.MEDIUM):
        # TODO: Validez les paramètres
        # - title non vide
        # - priority est bien une Priority
        # TODO: Initialisez les attributs
        # - id unique (utilisez time.time() ou uuid)
        # - created_at avec datetime.now()
        # - status à TODO par défaut
        # - project_id à None
        pass

    def mark_completed(self):
        # TODO: Changez le statut à DONE
        # TODO: Ajoutez completed_at avec datetime.now()
        pass

    def update_priority(self, new_priority):
        # TODO: Validez et mettez à jour la priorité
        pass

    def assign_to_project(self, project_id):
        # TODO: Assignez la tâche à un projet
        pass

    def to_dict(self):
        # TODO: Retournez un dictionnaire pour la sérialisation JSON
        # Gérez la conversion des Enum et datetime
        pass

    @classmethod
    def from_dict(cls, data):
        # TODO: Créez une Task depuis un dictionnaire
        # Gérez la conversion des string vers Enum et datetime
        pass
```

**Indices de développement :**
- Utilisez `time.time()` pour l'ID unique
- `datetime.now().isoformat()` pour sérialiser les dates
- `datetime.fromisoformat()` pour désérialiser
- `Priority[priority_name]` pour convertir string → Enum

---

### Étape 4 : Implémenter le gestionnaire de tâches

Créez `src/task_manager/manager.py` :

```python
import json
from typing import List, Optional
from .task import Task, Priority, Status

class TaskManager:
    """Gestionnaire principal des tâches"""

    def __init__(self, storage_file="tasks.json"):
        # TODO: Initialisez la liste des tâches et le fichier de stockage
        pass

    def add_task(self, title, description="", priority=Priority.MEDIUM):
        # TODO: Créez et ajoutez une nouvelle tâche
        # TODO: Retournez l'ID de la tâche créée
        pass

    def get_task(self, task_id) -> Optional[Task]:
        # TODO: Trouvez une tâche par son ID
        pass

    def get_tasks_by_status(self, status: Status) -> List[Task]:
        # TODO: Filtrez les tâches par statut
        pass

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        # TODO: Filtrez les tâches par priorité
        pass

    def delete_task(self, task_id) -> bool:
        # TODO: Supprimez une tâche
        # TODO: Retournez True si trouvée et supprimée, False sinon
        pass

    def save_to_file(self, filename=None):
        # TODO: Sauvegardez toutes les tâches en JSON
        # TODO: Gérez les erreurs d'écriture
        pass

    def load_from_file(self, filename=None):
        # TODO: Chargez les tâches depuis JSON
        # TODO: Gérez le cas du fichier inexistant
        pass

    def get_statistics(self):
        # TODO: Retournez un dictionnaire avec :
        # - total_tasks
        # - completed_tasks
        # - tasks_by_priority (dict)
        # - tasks_by_status (dict)
        pass
```

---

### Étape 5 : Ajouter les services externes

Créez `src/task_manager/services.py` pour simuler les dépendances :

```python
import smtplib
from datetime import datetime

class EmailService:
    """Service d'envoi d'emails (à mocker dans les tests)"""

    def __init__(self, smtp_server="smtp.gmail.com", port=587):
        # TODO: Stockez la configuration SMTP
        pass

    def send_task_reminder(self, email, task_title, due_date):
        # TODO: Simulez l'envoi d'un email de rappel
        # TODO: Levez une exception si email invalide
        # TODO: Retournez True si succès
        pass

    def send_completion_notification(self, email, task_title):
        # TODO: Simulez l'envoi d'un email de confirmation
        pass

class ReportService:
    """Service de génération de rapports"""

    def generate_daily_report(self, tasks, date=None):
        # TODO: Générez un rapport quotidien
        # TODO: Utilisez datetime.now() si date=None
        # TODO: Retournez un dictionnaire avec les métriques du jour
        pass

    def export_tasks_csv(self, tasks, filename):
        # TODO: Exportez les tâches en CSV
        # TODO: Gérez les erreurs d'écriture
        pass
```

---

## Phase 3 : Tests unitaires

### Étape 6 : Tests de l'entité Task

Créez `tests/test_task.py` avec cette structure :

```python
import pytest
from datetime import datetime
from src.task_manager.task import Task, Priority, Status

class TestTaskCreation:
    """Tests de création de tâches"""

    def test_create_task_minimal(self):
        """Test création tâche avec paramètres minimaux"""
        # TODO: Créez une tâche avec juste un titre
        # TODO: Vérifiez tous les attributs par défaut
        pass

    def test_create_task_complete(self):
        """Test création tâche avec tous les paramètres"""
        # TODO: Créez une tâche avec titre, description, priorité
        # TODO: Vérifiez tous les attributs
        pass

    def test_create_task_empty_title_raises_error(self):
        """Test titre vide lève une erreur"""
        # TODO: Utilisez pytest.raises pour tester l'exception
        pass

    def test_create_task_invalid_priority_raises_error(self):
        """Test priorité invalide lève une erreur"""
        # TODO: Testez avec un mauvais type de priorité
        pass

class TestTaskOperations:
    """Tests des opérations sur les tâches"""

    def setup_method(self):
        """Fixture : tâche de test"""
        # TODO: Créez self.task pour les tests
        pass

    def test_mark_completed_changes_status(self):
        """Test marquage comme terminée"""
        # TODO: Marquez la tâche comme terminée
        # TODO: Vérifiez le changement de statut
        # TODO: Vérifiez que completed_at est défini
        pass

    def test_update_priority_valid(self):
        """Test mise à jour priorité valide"""
        # TODO: Changez la priorité
        # TODO: Vérifiez le changement
        pass

    def test_assign_to_project(self):
        """Test assignation à un projet"""
        # TODO: Assignez à un projet
        # TODO: Vérifiez l'assignation
        pass

class TestTaskSerialization:
    """Tests de sérialisation JSON"""

    def setup_method(self):
        # TODO: Créez une tâche complexe avec tous les attributs
        pass

    def test_to_dict_contains_all_fields(self):
        """Test conversion en dictionnaire"""
        # TODO: Convertissez en dict
        # TODO: Vérifiez que tous les champs sont présents
        # TODO: Vérifiez que les types sont sérialisables (str pour Enum/datetime)
        pass

    def test_from_dict_recreates_task(self):
        """Test recréation depuis dictionnaire"""
        # TODO: Convertissez en dict puis recréez
        # TODO: Vérifiez que les deux tâches sont équivalentes
        pass
```

**Consignes d'implémentation :**
- Un test = une seule vérification logique
- Noms de tests explicites : `test_what_when_expected`
- Utilisez les fixtures (`setup_method`) pour éviter la duplication
- Testez tous les cas d'erreur avec `pytest.raises`

---

### Étape 7 : Tests du gestionnaire avec mocks

Créez `tests/test_manager.py` :

```python
import pytest
from unittest.mock import patch, mock_open
import json
from src.task_manager.manager import TaskManager
from src.task_manager.task import Task, Priority, Status

class TestTaskManagerBasics:
    """Tests basiques du gestionnaire"""

    def setup_method(self):
        """Fixture : gestionnaire de test"""
        # TODO: Créez self.manager avec un fichier temporaire
        pass

    def test_add_task_returns_id(self):
        """Test ajout tâche retourne un ID"""
        # TODO: Ajoutez une tâche
        # TODO: Vérifiez que l'ID est retourné
        # TODO: Vérifiez que la tâche est dans la liste
        pass

    def test_get_task_existing(self):
        """Test récupération tâche existante"""
        # TODO: Ajoutez une tâche
        # TODO: Récupérez-la par ID
        # TODO: Vérifiez les propriétés
        pass

    def test_get_task_nonexistent_returns_none(self):
        """Test récupération tâche inexistante"""
        # TODO: Cherchez une tâche avec un ID bidon
        # TODO: Vérifiez que None est retourné
        pass

class TestTaskManagerFiltering:
    """Tests de filtrage des tâches"""

    def setup_method(self):
        """Fixture : gestionnaire avec plusieurs tâches"""
        self.manager = TaskManager("test_tasks.json")
        # TODO: Ajoutez 3-4 tâches avec différents statuts/priorités
        pass

    def test_get_tasks_by_status(self):
        """Test filtrage par statut"""
        # TODO: Filtrez les tâches TODO
        # TODO: Vérifiez le nombre et les propriétés
        pass

    def test_get_tasks_by_priority(self):
        """Test filtrage par priorité"""
        # TODO: Filtrez les tâches HIGH priority
        # TODO: Vérifiez le résultat
        pass

class TestTaskManagerPersistence:
    """Tests de sauvegarde/chargement avec mocks"""

    def setup_method(self):
        self.manager = TaskManager("test_tasks.json")
        # TODO: Ajoutez quelques tâches de test
        pass

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_to_file_success(self, mock_json_dump, mock_file):
        """Test sauvegarde réussie"""
        # TODO: Appelez save_to_file()
        # TODO: Vérifiez que le fichier est ouvert en écriture
        # TODO: Vérifiez que json.dump est appelé
        pass

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('json.load')
    def test_load_from_file_success(self, mock_json_load, mock_file):
        """Test chargement réussi"""
        # TODO: Configurez mock_json_load pour retourner des données de test
        # TODO: Appelez load_from_file()
        # TODO: Vérifiez que les tâches sont chargées
        pass

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_from_nonexistent_file(self, mock_file):
        """Test chargement fichier inexistant"""
        # TODO: Appelez load_from_file()
        # TODO: Vérifiez que ça ne plante pas
        # TODO: Vérifiez que la liste reste vide
        pass
```

---

### Étape 8 : Tests d'intégration et services

Créez `tests/test_services.py` :

```python
import pytest
from unittest.mock import patch, Mock
from src.task_manager.services import EmailService, ReportService
from src.task_manager.task import Task, Priority

class TestEmailService:
    """Tests du service email avec mocks"""

    def setup_method(self):
        self.email_service = EmailService()

    @patch('src.task_manager.services.smtplib.SMTP')
    def test_send_task_reminder_success(self, mock_smtp):
        """Test envoi rappel réussi"""
        # TODO: Configurez le mock SMTP
        # TODO: Appelez send_task_reminder
        # TODO: Vérifiez que l'email est "envoyé"
        pass

    def test_send_task_reminder_invalid_email(self):
        """Test envoi avec email invalide"""
        # TODO: Testez avec un email sans @
        # TODO: Vérifiez qu'une exception est levée
        pass

class TestReportService:
    """Tests du service de rapports"""

    def setup_method(self):
        self.report_service = ReportService()
        # TODO: Créez une liste de tâches de test
        pass

    @patch('src.task_manager.services.datetime')
    def test_generate_daily_report_fixed_date(self, mock_datetime):
        """Test génération rapport avec date fixe"""
        # TODO: Configurez mock_datetime pour une date fixe
        # TODO: Générez le rapport
        # TODO: Vérifiez la structure du rapport
        pass

    @patch('builtins.open', new_callable=mock_open)
    def test_export_tasks_csv(self, mock_file):
        """Test export CSV"""
        # TODO: Exportez les tâches
        # TODO: Vérifiez que le fichier est ouvert
        # TODO: Vérifiez qu'il y a bien écriture
        pass
```

---

## Phase 4 : Qualité et automatisation

### Étape 9 : Configuration des outils

Créez ces fichiers de configuration :

#### pytest.ini

```ini
[tool:pytest]
testpaths = tests
addopts = -v --tb=short --disable-warnings
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow running tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

#### requirements.txt

```
# Production (aucune pour ce projet)
# Développement
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.0.0
```

#### Makefile

```
# - install : installer les dépendances
# - test : lancer les tests
# - test-unit : seulement les tests unitaires
# - test-integration : seulement les tests d'intégration
# - coverage : couverture avec rapport HTML
# - clean : nettoyer les fichiers temporaires
# - lint : vérification syntaxique
# - all : séquence complète
```

### Étape 10 : Atteindre 95% de couverture

1. Générez le rapport initial :

```sh
pytest --cov=src/task_manager --cov-report=html --cov-report=term-missing
```

2. Analysez les résultats :
   - Quelles lignes ne sont pas testées ?
   - Quels cas d'erreur manquent ?
   - Y a-t-il du code mort ?

3. Ajoutez les tests manquants :
   - Tests d'exceptions pour chaque validation
   - Tests des cas limites (listes vides, valeurs nulles)
   - Tests des méthodes utilitaires

**Objectif :** 95%+ de couverture sur tout le module

### Étape 11 : CI/CD avec GitHub Actions

Créez `.github/workflows/test.yml` :

```yaml
name: Tests et Qualité
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]

    steps:
      - uses: actions/checkout@v3

      - name: Setup Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      # TODO: Étape installation dépendances
      # TODO: Étape tests unitaires
      # TODO: Étape tests d'intégration
      # TODO: Étape couverture de code
      # TODO: Upload des résultats vers Codecov (optionnel)
```

---

## Phase 5 : Démonstration et validation

### Étape 12 : Créer des cas d'usage

Créez `demo.py` pour démontrer votre module :

```python
#!/usr/bin/env python3
"""
Démonstration du module TaskManager
"""
from src.task_manager.manager import TaskManager
from src.task_manager.task import Priority, Status
from src.task_manager.services import EmailService

def main():
    print("=== Démonstration TaskManager ===\n")

    # TODO: Créez un gestionnaire
    # TODO: Ajoutez plusieurs tâches avec différentes priorités
    # TODO: Marquez certaines comme terminées
    # TODO: Affichez les statistiques
    # TODO: Sauvegardez dans un fichier
    # TODO: Rechargez et vérifiez

    print("Démo terminée avec succès !")

if __name__ == "__main__":
    main()
```

### Étape 13 : Tests d'acceptation

Vérifiez que votre module répond aux exigences :

- **Fonctionnalités** : Toutes les fonctions requises sont implémentées
- **Tests** : Couverture ≥ 95% avec tests unitaires et d'intégration
- **Mocks** : Dépendances externes correctement mockées
- **Organisation** : Structure professionnelle du projet
- **Automatisation** : Tests et couverture automatisés
- **CI/CD** : GitHub Actions fonctionnel
- **Documentation** : README complet avec exemples
- **Démonstration** : Script demo.py montrant les fonctionnalités

---

## Critères d'évaluation

| Critère         | Poids | Détail                                              |
|-----------------|-------|-----------------------------------------------------|
| Fonctionnalités | 25%   | Toutes les fonctions implémentées et fonctionnelles  |
| Tests unitaires | 30%   | Couverture ≥95%, cas d'erreur, fixtures             |
| Mocking         | 20%   | Services externes mockés, tests isolés              |
| Organisation    | 15%   | Structure claire, nommage, configuration            |
| Automatisation  | 10%   | Makefile, CI/CD, rapports                           |

**Bonus possibles**
- Tests de performance sur de grandes listes
- Interface en ligne de commande (CLI)
- Export vers d'autres formats (XML, Excel)
- Tests de sécurité (injection, validation)

---

## Livrables attendus

1. **Code source** : Module complet dans `src/`
2. **Tests** : Suite de tests dans `tests/` avec 95%+ couverture
3. **Configuration** : Fichiers de config (`pytest.ini`, `Makefile`, etc.)
4. **CI/CD** : Workflow GitHub Actions fonctionnel
5. **Documentation** : README avec instructions d'installation et usage
6. **Démonstration** : Script `demo.py` montrant les fonctionnalités

---

**Deadline :** [À définir par l'enseignant]

---

Bon développement ! Ce projet synthétise toutes vos compétences en tests et qualité logicielle ! 🚀 