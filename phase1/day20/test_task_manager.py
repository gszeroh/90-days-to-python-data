"""
Day 20: Mini-Project — CLI Task Manager (Tests)

Run with:
    pytest phase1/day20/test_task_manager.py -v
"""

import json
from datetime import date, timedelta

import pytest

from task_manager import Task, TaskManager, TaskNotFoundError


# === Task Creation Tests ===


class TestTaskCreation:
    """Tests for the Task dataclass."""

    def test_create_task_defaults(self):
        """A task created with only a title gets sensible defaults."""
        task = Task(title="Buy groceries")
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.priority == "medium"
        assert task.due_date is None
        assert task.completed is False
        assert len(task.id) == 36  # UUID4 format

    def test_create_task_all_fields(self):
        """All fields can be set explicitly."""
        task = Task(
            title="Deploy app",
            description="Push v2.0 to production",
            priority="high",
            due_date="2025-12-31",
        )
        assert task.title == "Deploy app"
        assert task.description == "Push v2.0 to production"
        assert task.priority == "high"
        assert task.due_date == "2025-12-31"

    def test_invalid_priority_raises(self):
        """An invalid priority string raises ValueError."""
        with pytest.raises(ValueError, match="Invalid priority"):
            Task(title="Bad task", priority="urgent")

    def test_invalid_due_date_raises(self):
        """A malformed date string raises ValueError."""
        with pytest.raises(ValueError, match="Invalid due_date"):
            Task(title="Bad date", due_date="not-a-date")

    def test_priority_is_normalised(self):
        """Priority input is lowered and stripped."""
        task = Task(title="Test", priority="  HIGH  ")
        assert task.priority == "high"

    def test_overdue_detection(self):
        """A past due date on an incomplete task is detected as overdue."""
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        task = Task(title="Late task", due_date=yesterday)
        assert task.is_overdue is True

    def test_completed_task_not_overdue(self):
        """A completed task is never overdue, even with a past due date."""
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        task = Task(title="Done task", due_date=yesterday, completed=True)
        assert task.is_overdue is False

    def test_no_due_date_not_overdue(self):
        """A task without a due date is never overdue."""
        task = Task(title="Sometime")
        assert task.is_overdue is False

    def test_short_id(self):
        """short_id() returns the first 8 characters of the UUID."""
        task = Task(title="X")
        assert task.short_id() == task.id[:8]

    def test_str_representation(self):
        """__str__ includes the short ID, status icon, and priority."""
        task = Task(title="Read book", priority="low")
        text = str(task)
        assert task.short_id() in text
        assert "Read book" in text
        assert "LOW" in text

    def test_to_dict_and_from_dict_round_trip(self):
        """A task can be serialised and deserialised without data loss."""
        original = Task(
            title="Round-trip",
            description="Test serialisation",
            priority="high",
            due_date="2025-06-15",
        )
        rebuilt = Task.from_dict(original.to_dict())
        assert rebuilt.title == original.title
        assert rebuilt.description == original.description
        assert rebuilt.priority == original.priority
        assert rebuilt.due_date == original.due_date
        assert rebuilt.id == original.id
        assert rebuilt.created_at == original.created_at


# === TaskManager Tests ===


class TestTaskManagerCRUD:
    """Tests for add, complete, and delete operations."""

    @pytest.fixture()
    def manager(self):
        """Return a fresh TaskManager with no file backing."""
        return TaskManager(filepath="unused.json")

    def test_add_task(self, manager):
        """Adding a task increases the count and returns the new Task."""
        task = manager.add_task("Write tests")
        assert len(manager) == 1
        assert task.title == "Write tests"

    def test_add_task_empty_title_raises(self, manager):
        """An empty title is rejected with ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.add_task("   ")

    def test_complete_task(self, manager):
        """Completing a task sets completed=True and returns True."""
        task = manager.add_task("Do laundry")
        assert manager.complete_task(task.id) is True
        assert task.completed is True

    def test_complete_already_done(self, manager):
        """Completing an already-complete task returns False."""
        task = manager.add_task("Already done")
        manager.complete_task(task.id)
        assert manager.complete_task(task.id) is False

    def test_complete_task_short_id(self, manager):
        """A task can be completed using only the first 8 chars."""
        task = manager.add_task("Short ID test")
        assert manager.complete_task(task.short_id()) is True

    def test_delete_task(self, manager):
        """Deleting a task removes it from the list."""
        task = manager.add_task("Temporary")
        manager.delete_task(task.id)
        assert len(manager) == 0

    def test_delete_nonexistent_raises(self, manager):
        """Deleting a missing ID raises TaskNotFoundError."""
        with pytest.raises(TaskNotFoundError):
            manager.delete_task("nonexistent-id")

    def test_complete_nonexistent_raises(self, manager):
        """Completing a missing ID raises TaskNotFoundError."""
        with pytest.raises(TaskNotFoundError):
            manager.complete_task("nonexistent-id")


# === Search & Filter Tests ===


class TestSearchAndFilter:
    """Tests for search_tasks, filter_by_priority, filter_by_status."""

    @pytest.fixture()
    def manager(self):
        """Return a manager pre-loaded with sample tasks."""
        mgr = TaskManager(filepath="unused.json")
        mgr.add_task("Buy milk", description="From the corner store", priority="low")
        mgr.add_task("Write report", description="Q2 sales figures", priority="high")
        mgr.add_task("Fix bug #42", description="Null pointer in parser", priority="high")
        mgr.add_task("Buy eggs", priority="low")
        done = mgr.add_task("Old task", priority="medium")
        mgr.complete_task(done.id)
        return mgr

    def test_search_by_keyword(self, manager):
        """Searching for 'buy' returns both 'Buy' tasks (case-insensitive)."""
        results = manager.search_tasks("buy")
        assert len(results) == 2

    def test_search_regex(self, manager):
        """Regex patterns work in search (e.g. '#\\d+')."""
        results = manager.search_tasks(r"#\d+")
        assert len(results) == 1
        assert "bug" in results[0].title.lower()

    def test_search_invalid_regex(self, manager):
        """An invalid regex raises ValueError, not re.error."""
        with pytest.raises(ValueError, match="Invalid search pattern"):
            manager.search_tasks("[invalid")

    def test_search_no_results(self, manager):
        """Searching for a non-matching keyword returns an empty list."""
        assert manager.search_tasks("zzzzz") == []

    def test_filter_by_priority(self, manager):
        """Filtering by 'high' returns only high-priority tasks."""
        results = manager.filter_by_priority("high")
        assert len(results) == 2
        assert all(t.priority == "high" for t in results)

    def test_filter_by_status_pending(self, manager):
        """Filtering by status=False returns incomplete tasks."""
        results = manager.filter_by_status(completed=False)
        assert all(not t.completed for t in results)
        assert len(results) == 4

    def test_filter_by_status_completed(self, manager):
        """Filtering by status=True returns completed tasks."""
        results = manager.filter_by_status(completed=True)
        assert len(results) == 1
        assert results[0].title == "Old task"

    def test_get_overdue_tasks(self, manager):
        """get_overdue_tasks returns only past-due incomplete tasks."""
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        manager.add_task("Overdue item", due_date=yesterday)
        overdue = manager.get_overdue_tasks()
        assert len(overdue) == 1
        assert overdue[0].title == "Overdue item"


# === Persistence Tests ===


class TestPersistence:
    """Tests for save_to_file / load_from_file using pytest tmp_path."""

    def test_save_and_load(self, tmp_path):
        """Tasks survive a save → new manager → load cycle."""
        filepath = str(tmp_path / "tasks.json")
        mgr = TaskManager(filepath=filepath)
        mgr.add_task("Persist me", priority="high", due_date="2025-12-31")
        mgr.add_task("Me too", description="important")
        mgr.save_to_file()

        mgr2 = TaskManager(filepath=filepath)
        mgr2.load_from_file()
        assert len(mgr2) == 2
        assert mgr2.tasks[0].title == "Persist me"
        assert mgr2.tasks[0].priority == "high"
        assert mgr2.tasks[1].description == "important"

    def test_load_missing_file(self, tmp_path):
        """Loading from a non-existent file leaves the list empty."""
        filepath = str(tmp_path / "does_not_exist.json")
        mgr = TaskManager(filepath=filepath)
        mgr.load_from_file()
        assert len(mgr) == 0

    def test_load_invalid_json(self, tmp_path):
        """Loading corrupted JSON raises json.JSONDecodeError."""
        filepath = tmp_path / "bad.json"
        filepath.write_text("{not valid json!!!")
        mgr = TaskManager(filepath=str(filepath))
        with pytest.raises(json.JSONDecodeError):
            mgr.load_from_file()

    def test_saved_file_is_valid_json(self, tmp_path):
        """The saved file can be parsed by the standard json module."""
        filepath = str(tmp_path / "tasks.json")
        mgr = TaskManager(filepath=filepath)
        mgr.add_task("JSON check")
        mgr.save_to_file()

        with open(filepath, encoding="utf-8") as fh:
            data = json.load(fh)
        assert isinstance(data, list)
        assert data[0]["title"] == "JSON check"

    def test_completed_status_persists(self, tmp_path):
        """Marking a task complete is preserved after save/load."""
        filepath = str(tmp_path / "tasks.json")
        mgr = TaskManager(filepath=filepath)
        task = mgr.add_task("Complete me")
        mgr.complete_task(task.id)
        mgr.save_to_file()

        mgr2 = TaskManager(filepath=filepath)
        mgr2.load_from_file()
        assert mgr2.tasks[0].completed is True
