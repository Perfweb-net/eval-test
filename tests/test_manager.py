import pytest
from unittest.mock import patch, mock_open
import json
from src.task_manager.manager import TaskManager
from src.task_manager.task import Task, Priority, Status

class TestTaskManagerBasics:
    """Tests basiques du gestionnaire"""

    def setup_method(self):
        self.manager = TaskManager("test_tasks.json")

    def test_add_task_returns_id(self):
        task_id = self.manager.add_task("Titre", "Desc", Priority.HIGH)
        assert isinstance(task_id, str)
        assert self.manager.get_task(task_id) is not None

    def test_get_task_existing(self):
        task_id = self.manager.add_task("Titre")
        task = self.manager.get_task(task_id)
        assert task is not None
        assert task.title == "Titre"

    def test_get_task_nonexistent_returns_none(self):
        assert self.manager.get_task("fakeid") is None

    def test_delete_task_success(self):
        task_id = self.manager.add_task("Titre")
        assert self.manager.delete_task(task_id) is True
        assert self.manager.get_task(task_id) is None

    def test_delete_task_failure(self):
        assert self.manager.delete_task("inexistant") is False

    def test_get_statistics(self):
        self.manager.add_task("T1", priority=Priority.LOW)
        self.manager.add_task("T2", priority=Priority.HIGH)
        self.manager.get_task(self.manager.tasks[1].id).mark_completed()
        stats = self.manager.get_statistics()
        assert stats["total_tasks"] >= 2
        assert "completed_tasks" in stats
        assert "tasks_by_priority" in stats
        assert "tasks_by_status" in stats

class TestTaskManagerFiltering:
    """Tests de filtrage des tâches"""

    def setup_method(self):
        self.manager = TaskManager("test_tasks.json")
        self.manager.add_task("T1", priority=Priority.LOW)
        t2 = self.manager.add_task("T2", priority=Priority.HIGH)
        t3 = self.manager.add_task("T3", priority=Priority.HIGH)
        task2 = self.manager.get_task(t2)
        task2.status = Status.DONE
        task3 = self.manager.get_task(t3)
        task3.status = Status.IN_PROGRESS

    def test_get_tasks_by_status(self):
        todos = self.manager.get_tasks_by_status(Status.TODO)
        assert all(t.status == Status.TODO for t in todos)

    def test_get_tasks_by_priority(self):
        highs = self.manager.get_tasks_by_priority(Priority.HIGH)
        assert all(t.priority == Priority.HIGH for t in highs)

    def test_get_tasks_by_status_empty(self):
        manager = TaskManager()
        assert manager.get_tasks_by_status(Status.TODO) == []

    def test_get_tasks_by_priority_empty(self):
        manager = TaskManager()
        assert manager.get_tasks_by_priority(Priority.LOW) == []

class TestTaskManagerPersistence:
    """Tests de sauvegarde/chargement avec mocks"""

    def setup_method(self):
        self.manager = TaskManager("test_tasks.json")
        self.manager.add_task("T1")
        self.manager.add_task("T2", priority=Priority.HIGH)

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_to_file_success(self, mock_json_dump, mock_file):
        self.manager.save_to_file()
        mock_file.assert_called_with("test_tasks.json", "w")
        assert mock_json_dump.called

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('json.load')
    def test_load_from_file_success(self, mock_json_load, mock_file):
        mock_json_load.return_value = [Task("T1").to_dict()]
        self.manager.load_from_file()
        assert len(self.manager.tasks) == 1
        assert self.manager.tasks[0].title == "T1"

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_from_nonexistent_file(self, mock_file):
        self.manager.load_from_file()
        assert self.manager.tasks == [] 

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file_ioerror(self, mock_file):
        mock_file.side_effect = IOError("Erreur écriture")
        with pytest.raises(IOError):
            self.manager.save_to_file()

    @patch('builtins.open', new_callable=mock_open)
    def test_load_from_file_json_error(self, mock_file):
        mock_file.return_value.__enter__.return_value.read.return_value = '{bad json}'
        with pytest.raises(IOError):
            self.manager.load_from_file()

    @patch('builtins.open', side_effect=OSError("Erreur générique"))
    def test_load_from_file_oserror(self, mock_file):
        with pytest.raises(IOError):
            self.manager.load_from_file()

    @patch('builtins.open', new_callable=mock_open, read_data='{"bad": "data"}')
    @patch('json.load')
    def test_load_from_file_bad_task_data(self, mock_json_load, mock_file):
        # Simule un dict qui ne correspond pas à la structure attendue par Task.from_dict
        mock_json_load.return_value = [{"bad": "data"}]
        with pytest.raises(Exception):
            self.manager.load_from_file()

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump', side_effect=Exception("fail"))
    def test_save_to_file_raises_ioerror(self, mock_json_dump, mock_file):
        with pytest.raises(IOError):
            self.manager.save_to_file()

    @patch('builtins.open', new_callable=mock_open, read_data='notjson')
    def test_load_from_file_corrupted(self, mock_file):
        with pytest.raises(IOError):
            self.manager.load_from_file()

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch('json.load', side_effect=Exception("fail"))
    def test_load_from_file_raises_ioerror(self, mock_json_load, mock_file):
        with pytest.raises(IOError):
            self.manager.load_from_file()

    def test_delete_task_nonexistent(self):
        assert self.manager.delete_task("notfound") is False 

    def test_delete_task_twice(self):
        task_id = self.manager.add_task("T4")
        assert self.manager.delete_task(task_id) is True
        assert self.manager.delete_task(task_id) is False

    def test_save_to_file_with_filename(self, tmp_path):
        file_path = tmp_path / "custom.json"
        self.manager.save_to_file(str(file_path))
        assert file_path.exists()

    def test_load_from_file_with_filename(self, tmp_path):
        file_path = tmp_path / "custom.json"
        self.manager.save_to_file(str(file_path))
        new_manager = TaskManager(str(file_path))
        new_manager.load_from_file()
        assert len(new_manager.tasks) == len(self.manager.tasks) 