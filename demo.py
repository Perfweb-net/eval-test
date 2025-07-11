#!/usr/bin/env python3
"""
Démonstration du module TaskManager
"""
from src.task_manager.manager import TaskManager
from src.task_manager.task import Priority, Status
from src.task_manager.services import EmailService

def main():
    print("=== Démonstration TaskManager ===\n")

    manager = TaskManager("demo_tasks.json")
    # Ajout de tâches
    id1 = manager.add_task("Tâche 1", "Description 1", Priority.LOW)
    id2 = manager.add_task("Tâche 2", "Description 2", Priority.HIGH)
    id3 = manager.add_task("Tâche 3", "Description 3", Priority.URGENT)

    # Marquer certaines comme terminées
    manager.get_task(id2).mark_completed()

    # Afficher les statistiques
    stats = manager.get_statistics()
    print("Statistiques :", stats)

    # Sauvegarder dans un fichier
    manager.save_to_file()
    print("Tâches sauvegardées dans demo_tasks.json")

    # Recharger et vérifier
    manager2 = TaskManager("demo_tasks.json")
    manager2.load_from_file()
    print("Tâches rechargées :", [t.title for t in manager2.tasks])

    print("Démo terminée avec succès !")

if __name__ == "__main__":
    main() 