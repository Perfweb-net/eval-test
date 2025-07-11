import smtplib
from datetime import datetime
import csv

class EmailService:
    """Service d'envoi d'emails (à mocker dans les tests)"""

    def __init__(self, smtp_server="smtp.gmail.com", port=587):
        self.smtp_server = smtp_server
        self.port = port

    def send_task_reminder(self, email, task_title, due_date):
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Email invalide")
        # Simulation d'envoi
        return True

    def send_completion_notification(self, email, task_title):
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Email invalide")
        # Simulation d'envoi
        return True

class ReportService:
    """Service de génération de rapports"""

    def generate_daily_report(self, tasks, date=None):
        date = date or datetime.now()
        total = len(tasks)
        completed = len([t for t in tasks if getattr(t, 'status', None) and t.status.name == 'DONE'])
        by_priority = {}
        for t in tasks:
            p = getattr(t, 'priority', None)
            if p:
                by_priority[p.name] = by_priority.get(p.name, 0) + 1
        return {
            "date": date.isoformat(),
            "total": total,
            "completed": completed,
            "by_priority": by_priority
        }

    def export_tasks_csv(self, tasks, filename):
        try:
            with open(filename, "w", newline="") as csvfile:
                fieldnames = ["id", "title", "description", "priority", "created_at", "status", "project_id", "completed_at"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for t in tasks:
                    writer.writerow(t.to_dict())
        except Exception as e:
            raise IOError(f"Erreur lors de l'export CSV : {e}") 