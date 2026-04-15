"""
Day 20: Mini-Project — CLI Task Manager

A fully-functional command-line task manager that demonstrates every major
concept from Phase 1 of the 90 Days to Python for Data Science curriculum.

Concepts used:
    - Variables & types (Day 2)
    - Strings & formatting (Day 3)
    - Control flow (Days 5-6)
    - Functions (Days 7-8)
    - Data structures (Days 9-10)
    - File I/O with JSON (Day 11)
    - Error handling (Day 12)
    - OOP & dataclasses (Days 14-16)
    - Iterators & generators (Day 17)
    - Regular expressions (Day 18)

Usage:
    python task_manager.py
    python task_manager.py --file my_tasks.json
"""

import json
import os
import re
import uuid
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from typing import Iterator, Optional


# === Task Model ===

@dataclass
class Task:
    """Represents a single task in the task manager.

    Attributes:
        id (str): Unique identifier (UUID4).
        title (str): Short summary of the task.
        description (str): Detailed description.
        priority (str): One of "low", "medium", or "high".
        due_date (Optional[str]): Target date in YYYY-MM-DD format, or None.
        completed (bool): Whether the task has been finished.
        created_at (str): ISO-8601 timestamp of creation.
    """

    title: str
    description: str = ""
    priority: str = "medium"
    due_date: Optional[str] = None
    completed: bool = False
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def __post_init__(self):
        """Validate fields after initialisation."""
        valid_priorities = {"low", "medium", "high"}
        self.priority = self.priority.lower().strip()
        if self.priority not in valid_priorities:
            raise ValueError(
                f"Invalid priority '{self.priority}'. "
                f"Choose from: {', '.join(sorted(valid_priorities))}"
            )
        if self.due_date is not None:
            try:
                datetime.strptime(self.due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError(
                    f"Invalid due_date '{self.due_date}'. Use YYYY-MM-DD format."
                )

    @property
    def is_overdue(self) -> bool:
        """Return True if the task is incomplete and past its due date."""
        if self.completed or self.due_date is None:
            return False
        return date.fromisoformat(self.due_date) < date.today()

    def to_dict(self) -> dict:
        """Serialise the task to a plain dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task from a dictionary (e.g. loaded from JSON)."""
        return cls(**data)

    def short_id(self) -> str:
        """Return the first 8 characters of the UUID for display."""
        return self.id[:8]

    def __str__(self) -> str:
        status = "✅" if self.completed else "❌"
        overdue = " ⚠️  OVERDUE" if self.is_overdue else ""
        due = f" | Due: {self.due_date}" if self.due_date else ""
        return (
            f"[{self.short_id()}] {status} {self.title} "
            f"({self.priority.upper()}){due}{overdue}"
        )


# === Custom Exceptions ===

class TaskNotFoundError(Exception):
    """Raised when a task ID cannot be found."""


# === Task Manager ===

class TaskManager:
    """Manages a collection of tasks with CRUD, search, and persistence.

    Attributes:
        tasks (list[Task]): In-memory list of tasks.
        filepath (str): Path to the JSON file used for persistence.

    Methods:
        add_task(title, ...) -> Task
        complete_task(task_id) -> bool
        delete_task(task_id) -> bool
        search_tasks(keyword) -> list[Task]
        filter_by_priority(priority) -> list[Task]
        filter_by_status(completed) -> list[Task]
        get_overdue_tasks() -> list[Task]
        save_to_file() -> None
        load_from_file() -> None
    """

    def __init__(self, filepath: str = "tasks.json"):
        self.filepath: str = filepath
        self.tasks: list = []

    # --- CRUD Operations ---

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: str = "medium",
        due_date: Optional[str] = None,
    ) -> Task:
        """Create a new task and add it to the collection.

        Args:
            title: Short summary (must not be empty).
            description: Optional detailed description.
            priority: "low", "medium", or "high".
            due_date: Optional target date (YYYY-MM-DD).

        Returns:
            The newly created Task.

        Raises:
            ValueError: If title is blank or priority is invalid.
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            due_date=due_date if due_date else None,
        )
        self.tasks.append(task)
        return task

    def _find_task(self, task_id: str) -> Task:
        """Look up a task by full or partial ID.

        Supports matching by the first 8 characters (short ID) for
        convenience at the command line.

        Raises:
            TaskNotFoundError: If no matching task is found.
        """
        for task in self.tasks:
            if task.id == task_id or task.id.startswith(task_id):
                return task
        raise TaskNotFoundError(f"No task found with ID starting with '{task_id}'.")

    def complete_task(self, task_id: str) -> bool:
        """Mark a task as completed.

        Returns:
            True if the task was updated, False if it was already complete.
        """
        task = self._find_task(task_id)
        if task.completed:
            return False
        task.completed = True
        return True

    def delete_task(self, task_id: str) -> bool:
        """Remove a task from the collection.

        Returns:
            True after successful deletion.

        Raises:
            TaskNotFoundError: If the ID does not match any task.
        """
        task = self._find_task(task_id)
        self.tasks.remove(task)
        return True

    # --- Search & Filter (iterators / generators) ---

    def _iter_matching(self, keyword: str) -> Iterator[Task]:
        """Yield tasks whose title or description matches *keyword* (regex)."""
        pattern = re.compile(keyword, re.IGNORECASE)
        for task in self.tasks:
            if pattern.search(task.title) or pattern.search(task.description):
                yield task

    def search_tasks(self, keyword: str) -> list:
        """Return tasks matching *keyword* in title or description.

        Uses regex for powerful pattern matching (e.g. ``"buy.*milk"``).
        """
        try:
            return list(self._iter_matching(keyword))
        except re.error as exc:
            raise ValueError(f"Invalid search pattern: {exc}")

    def filter_by_priority(self, priority: str) -> list:
        """Return tasks that match the given priority level."""
        priority = priority.lower().strip()
        return [t for t in self.tasks if t.priority == priority]

    def filter_by_status(self, completed: bool = False) -> list:
        """Return tasks filtered by completion status."""
        return [t for t in self.tasks if t.completed is completed]

    def get_overdue_tasks(self) -> list:
        """Return incomplete tasks whose due date has passed."""
        return [t for t in self.tasks if t.is_overdue]

    # --- Persistence (JSON file I/O) ---

    def save_to_file(self) -> None:
        """Write all tasks to the JSON file at *self.filepath*."""
        data = [task.to_dict() for task in self.tasks]
        with open(self.filepath, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)

    def load_from_file(self) -> None:
        """Load tasks from the JSON file, replacing the in-memory list.

        If the file does not exist, the task list is left empty.

        Raises:
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        self.tasks = [Task.from_dict(item) for item in data]

    # --- Utility ---

    def __len__(self) -> int:
        return len(self.tasks)

    def __repr__(self) -> str:
        return f"TaskManager(tasks={len(self.tasks)}, filepath='{self.filepath}')"


# === CLI Helpers ===

PRIORITY_COLOURS = {
    "high": "\033[91m",    # red
    "medium": "\033[93m",  # yellow
    "low": "\033[92m",     # green
}
RESET = "\033[0m"


def coloured_priority(priority: str) -> str:
    """Wrap a priority label with ANSI colour codes."""
    colour = PRIORITY_COLOURS.get(priority, "")
    return f"{colour}{priority.upper()}{RESET}"


def print_tasks(tasks: list, heading: str = "Tasks") -> None:
    """Pretty-print a list of tasks to the terminal."""
    if not tasks:
        print("\n  (no tasks to display)\n")
        return
    print(f"\n  {heading} ({len(tasks)})")
    print("  " + "-" * 60)
    for task in tasks:
        status = "✅" if task.completed else "❌"
        overdue_flag = " ⚠️  OVERDUE" if task.is_overdue else ""
        due_str = f" | Due: {task.due_date}" if task.due_date else ""
        pri = coloured_priority(task.priority)
        print(
            f"  [{task.short_id()}] {status} {task.title} "
            f"({pri}){due_str}{overdue_flag}"
        )
        if task.description:
            print(f"             {task.description}")
    print()


def get_input(prompt: str, required: bool = False) -> str:
    """Read a line of user input, optionally requiring a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("  ⚠ This field is required.")


def get_priority() -> str:
    """Prompt the user for a valid priority level."""
    while True:
        pri = input("  Priority (low/medium/high) [medium]: ").strip().lower()
        if pri == "":
            return "medium"
        if pri in {"low", "medium", "high"}:
            return pri
        print("  ⚠ Please enter low, medium, or high.")


def get_due_date() -> Optional[str]:
    """Prompt for an optional due date in YYYY-MM-DD format."""
    while True:
        raw = input("  Due date (YYYY-MM-DD or blank): ").strip()
        if raw == "":
            return None
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("  ⚠ Invalid date format. Use YYYY-MM-DD.")


# === CLI Menu ===

MENU = """
========================================
       📋  CLI Task Manager  📋
========================================
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Search Tasks
6. Filter by Priority
7. Filter by Status
8. Show Overdue Tasks
9. Save & Quit
----------------------------------------"""


def run_cli(manager: Optional[TaskManager] = None) -> None:
    """Run the interactive command-line interface.

    Args:
        manager: An optional pre-configured TaskManager (useful for testing).
                 If None a default manager is created and loaded from disk.
    """
    if manager is None:
        manager = TaskManager()
        try:
            manager.load_from_file()
            if manager.tasks:
                print(f"  Loaded {len(manager)} task(s) from {manager.filepath}.")
        except json.JSONDecodeError:
            print("  ⚠ Could not parse tasks file — starting with empty list.")

    while True:
        print(MENU)
        choice = input("Choose an option (1-9): ").strip()

        # --- 1. Add Task ---
        if choice == "1":
            print("\n  --- Add New Task ---")
            title = get_input("  Title: ", required=True)
            description = get_input("  Description: ")
            priority = get_priority()
            due = get_due_date()
            try:
                task = manager.add_task(title, description, priority, due)
                print(f"\n  ✅ Task added: {task}")
            except ValueError as exc:
                print(f"\n  ⚠ Error: {exc}")

        # --- 2. List Tasks ---
        elif choice == "2":
            print_tasks(manager.tasks, heading="All Tasks")

        # --- 3. Complete Task ---
        elif choice == "3":
            print_tasks(manager.filter_by_status(completed=False), "Pending Tasks")
            task_id = get_input("  Enter task ID to complete: ", required=True)
            try:
                if manager.complete_task(task_id):
                    print("  ✅ Task marked as complete!")
                else:
                    print("  ℹ️  Task was already complete.")
            except TaskNotFoundError as exc:
                print(f"  ⚠ {exc}")

        # --- 4. Delete Task ---
        elif choice == "4":
            print_tasks(manager.tasks, "All Tasks")
            task_id = get_input("  Enter task ID to delete: ", required=True)
            try:
                manager.delete_task(task_id)
                print("  ✅ Task deleted.")
            except TaskNotFoundError as exc:
                print(f"  ⚠ {exc}")

        # --- 5. Search Tasks ---
        elif choice == "5":
            keyword = get_input("  Search keyword (regex supported): ", required=True)
            try:
                results = manager.search_tasks(keyword)
                print_tasks(results, f"Search results for '{keyword}'")
            except ValueError as exc:
                print(f"  ⚠ {exc}")

        # --- 6. Filter by Priority ---
        elif choice == "6":
            priority = get_priority()
            results = manager.filter_by_priority(priority)
            print_tasks(results, f"Priority: {priority.upper()}")

        # --- 7. Filter by Status ---
        elif choice == "7":
            status = input("  Show (p)ending or (c)ompleted? [p]: ").strip().lower()
            completed = status.startswith("c")
            label = "Completed" if completed else "Pending"
            results = manager.filter_by_status(completed)
            print_tasks(results, f"{label} Tasks")

        # --- 8. Overdue Tasks ---
        elif choice == "8":
            results = manager.get_overdue_tasks()
            print_tasks(results, "Overdue Tasks")

        # --- 9. Save & Quit ---
        elif choice == "9":
            try:
                manager.save_to_file()
                print(f"\n  💾 Saved {len(manager)} task(s) to {manager.filepath}.")
            except OSError as exc:
                print(f"\n  ⚠ Could not save: {exc}")
            print("  Goodbye! 👋\n")
            break

        else:
            print("  ⚠ Invalid option. Please choose 1-9.")


# === Entry Point ===

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CLI Task Manager")
    parser.add_argument(
        "--file",
        default="tasks.json",
        help="Path to the JSON file for task storage (default: tasks.json)",
    )
    args = parser.parse_args()

    mgr = TaskManager(filepath=args.file)
    run_cli(mgr)
