import pytest
from unittest.mock import patch, Mock, mock_open
from src.task_manager.services import EmailService, ReportService
from src.task_manager.task import Task, Priority
from datetime import datetime

class TestEmailService:
    """Tests du service email avec mocks"""

    def setup_method(self):
        self.email_service = EmailService()

    @patch('src.task_manager.services.smtplib.SMTP')
    def test_send_task_reminder_success(self, mock_smtp):
        result = self.email_service.send_task_reminder("test@example.com", "Tâche", datetime.now())
        assert result is True

    def test_send_task_reminder_invalid_email(self):
        with pytest.raises(ValueError):
            self.email_service.send_task_reminder("bademail", "Tâche", datetime.now())

    def test_send_task_reminder_empty_email(self):
        with pytest.raises(ValueError):
            self.email_service.send_task_reminder("", "Tâche", datetime.now())

    def test_send_completion_notification_invalid_email(self):
        with pytest.raises(ValueError):
            self.email_service.send_completion_notification("bademail", "Tâche")

    def test_send_completion_notification_empty_email(self):
        with pytest.raises(ValueError):
            self.email_service.send_completion_notification("", "Tâche")

    def test_send_completion_notification_success(self):
        assert self.email_service.send_completion_notification("test@example.com", "Tâche") is True

    def test_send_task_reminder_none_email(self):
        with pytest.raises(ValueError):
            self.email_service.send_task_reminder(None, "Tâche", datetime.now())

    def test_send_completion_notification_none_email(self):
        with pytest.raises(ValueError):
            self.email_service.send_completion_notification(None, "Tâche")

class TestReportService:
    """Tests du service de rapports"""

    def setup_method(self):
        self.report_service = ReportService()
        self.tasks = [
            Task("T1", priority=Priority.LOW),
            Task("T2", priority=Priority.HIGH),
            Task("T3", priority=Priority.HIGH)
        ]
        self.tasks[1].mark_completed()

    @patch('src.task_manager.services.datetime')
    def test_generate_daily_report_fixed_date(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 1)
        report = self.report_service.generate_daily_report(self.tasks)
        assert report["date"].startswith("2024-01-01")
        assert report["total"] == 3
        assert report["completed"] == 1
        assert report["by_priority"]["LOW"] == 1
        assert report["by_priority"]["HIGH"] == 2

    def test_generate_daily_report_empty(self):
        report = self.report_service.generate_daily_report([])
        assert report["total"] == 0
        assert report["completed"] == 0
        assert isinstance(report["by_priority"], dict)

    @patch('builtins.open', new_callable=mock_open)
    def test_export_tasks_csv(self, mock_file):
        self.report_service.export_tasks_csv(self.tasks, "tasks.csv")
        mock_file.assert_called_with("tasks.csv", "w", newline="")

    @patch('builtins.open', new_callable=mock_open)
    def test_export_tasks_csv_success(self, mock_file):
        self.report_service.export_tasks_csv(self.tasks, "test.csv")
        mock_file.assert_called_with("test.csv", "w", newline="")

    @patch('builtins.open', side_effect=IOError("Erreur écriture"))
    def test_export_tasks_csv_ioerror(self, mock_file):
        with pytest.raises(IOError):
            self.report_service.export_tasks_csv(self.tasks, "badfile.csv")

    @patch('builtins.open', side_effect=Exception("fail"))
    def test_export_tasks_csv_raises_ioerror(self, mock_file):
        with pytest.raises(IOError):
            self.report_service.export_tasks_csv(self.tasks, "test.csv")

def test_email_service_init():
    service = EmailService("smtp.test.com", 123)
    assert service.smtp_server == "smtp.test.com"
    assert service.port == 123

def test_report_service_init():
    service = ReportService()
    assert isinstance(service, ReportService)

def test_generate_daily_report_task_without_priority_status():
    class Dummy: pass
    dummy = Dummy()
    report = ReportService().generate_daily_report([dummy])
    assert report["total"] == 1
    assert report["completed"] == 0

def test_export_tasks_csv_empty(tmp_path):
    file_path = tmp_path / "empty.csv"
    ReportService().export_tasks_csv([], str(file_path))
    assert file_path.exists() 