"""
Day 20: Mini-Project — CLI Task Manager (Solutions)

Reference implementations for the extension exercises in exercises.py.
"""

import copy
import csv
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import Optional

from task_manager import Task, TaskManager


# === Exercise 1: Add Categories / Tags ===

@dataclass
class TaggedTask(Task):
    """A Task that supports multiple tags (categories).

    Attributes:
        tags (list[str]): Zero or more string labels, e.g. ["work", "urgent"].

    Methods:
        add_tag(tag) -> None:
            Append *tag* (lowered, stripped) if not already present.
        remove_tag(tag) -> bool:
            Remove *tag* and return True, or return False if not found.
        has_tag(tag) -> bool:
            Return True if the task carries the given tag.

    The ``to_dict`` / ``from_dict`` round-trip must preserve tags.

    Examples:
        t = TaggedTask(title="Review PR", tags=["work", "code"])
        t.has_tag("work")        # True
        t.add_tag("urgent")
        t.remove_tag("code")     # True
    """

    tags: list = field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        tag = tag.lower().strip()
        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> bool:
        tag = tag.lower().strip()
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    def has_tag(self, tag: str) -> bool:
        return tag.lower().strip() in self.tags


def filter_by_tag(manager: TaskManager, tag: str) -> list:
    """Return all tasks in *manager* that carry the given tag."""
    tag = tag.lower().strip()
    return [
        t for t in manager.tasks
        if isinstance(t, TaggedTask) and t.has_tag(tag)
    ]


# === Exercise 2: Recurring Tasks ===

def create_recurring_tasks(
    manager: TaskManager,
    title: str,
    description: str = "",
    priority: str = "medium",
    recurrence: str = "daily",
    count: int = 7,
    start_date: Optional[str] = None,
) -> list:
    """Generate *count* tasks with due dates spaced by *recurrence*."""
    recurrence_map = {
        "daily": timedelta(days=1),
        "weekly": timedelta(weeks=1),
        "monthly": timedelta(days=30),
    }

    recurrence = recurrence.lower().strip()
    if recurrence not in recurrence_map:
        raise ValueError(
            f"Invalid recurrence '{recurrence}'. "
            f"Choose from: {', '.join(sorted(recurrence_map))}"
        )

    delta = recurrence_map[recurrence]
    current = (
        date.fromisoformat(start_date) if start_date else date.today()
    )

    created = []
    for i in range(1, count + 1):
        task = manager.add_task(
            title=f"{title} ({i}/{count})",
            description=description,
            priority=priority,
            due_date=current.isoformat(),
        )
        created.append(task)
        current += delta

    return created


# === Exercise 3: Task Statistics ===

def task_statistics(manager: TaskManager) -> dict:
    """Compute summary statistics for all tasks in *manager*."""
    total = len(manager.tasks)
    completed = sum(1 for t in manager.tasks if t.completed)
    pending = total - completed
    overdue = len(manager.get_overdue_tasks())

    completion_rate = (completed / total * 100.0) if total > 0 else 0.0

    priority_breakdown = {"low": 0, "medium": 0, "high": 0}
    for task in manager.tasks:
        if task.priority in priority_breakdown:
            priority_breakdown[task.priority] += 1

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
        "completion_rate": round(completion_rate, 1),
        "priority_breakdown": priority_breakdown,
    }


# === Exercise 4: Export to CSV ===

def export_to_csv(manager: TaskManager, filepath: str) -> int:
    """Export all tasks to a CSV file."""
    headers = [
        "id", "title", "description", "priority",
        "due_date", "completed", "created_at",
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        for task in manager.tasks:
            writer.writerow(task.to_dict())

    return len(manager.tasks)


# === Exercise 5: Undo Functionality ===

class UndoableTaskManager(TaskManager):
    """A TaskManager that supports undoing the last action.

    Maintains an internal history stack.  After each mutating operation
    (add, complete, delete) a snapshot is pushed.  Calling ``undo()``
    restores the previous state.

    Methods:
        undo() -> bool:
            Restore the task list to its state before the last mutating
            operation.  Return True on success, False if there is nothing
            to undo.

    Examples:
        um = UndoableTaskManager()
        um.add_task("One")
        um.add_task("Two")
        len(um)          # 2
        um.undo()        # True
        len(um)          # 1
        um.undo()        # True
        len(um)          # 0
        um.undo()        # False (nothing left to undo)
    """

    def __init__(self, filepath: str = "tasks.json"):
        super().__init__(filepath)
        self._history: list = []

    def _save_snapshot(self) -> None:
        """Push a deep copy of the current task list onto the history stack."""
        self._history.append(copy.deepcopy(self.tasks))

    def add_task(self, title, description="", priority="medium", due_date=None):
        self._save_snapshot()
        return super().add_task(title, description, priority, due_date)

    def complete_task(self, task_id):
        self._save_snapshot()
        return super().complete_task(task_id)

    def delete_task(self, task_id):
        self._save_snapshot()
        return super().delete_task(task_id)

    def undo(self) -> bool:
        if not self._history:
            return False
        self.tasks = self._history.pop()
        return True
