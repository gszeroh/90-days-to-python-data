# Day 20: Mini-Project — CLI Task Manager

## Overview
Congratulations — you've reached the **capstone project** of Phase 1! Over the
past 19 days you've learned variables, strings, control flow, functions, data
structures, file I/O, error handling, OOP, iterators, regular expressions, and
testing. Today you'll bring **all of those skills together** to build a
fully-functional **Command-Line Task Manager** application.

This is not a toy example. The project follows real-world patterns: data
modelling with classes, persistence via JSON files, input validation, search and
filtering, and automated tests. By the end of the day you will have a portfolio
piece that demonstrates your Phase 1 mastery.

---

## Project Requirements

| Feature | Description |
|---------|-------------|
| **Add tasks** | Create a task with title, description, priority, and optional due date |
| **List tasks** | Display all tasks in a formatted table |
| **Complete tasks** | Mark a task as done |
| **Delete tasks** | Remove a task permanently |
| **Save / Load** | Persist tasks to a JSON file and reload on startup |
| **Priority levels** | Low, Medium, High — with colour-coded display |
| **Due dates** | Optional due date with overdue detection |
| **Search** | Find tasks by keyword (regex-powered) |
| **Filter** | Filter by priority or completion status |

---

## Phase 1 Concepts Used

| Day | Concept | Where It Appears |
|-----|---------|------------------|
| 2 | Variables & Types | Task attributes, type conversions |
| 3 | Strings | Formatted display, input parsing |
| 5–6 | Control Flow | Menu loop, conditionals, validation |
| 7–8 | Functions | Helper utilities, menu handlers |
| 9–10 | Data Structures | Lists of tasks, dict serialisation |
| 11 | File I/O | JSON save / load |
| 12 | Error Handling | Input validation, file errors, custom exceptions |
| 14–16 | OOP | `Task` dataclass, `TaskManager` class |
| 17 | Iterators | Generator-based filtering |
| 18 | Regular Expressions | Keyword search across fields |
| 19 | Testing | Full pytest suite |

---

## Architecture

```
phase1/day20/
├── README.md              ← You are here
├── task_manager.py        ← Main application (Task, TaskManager, CLI)
├── test_task_manager.py   ← Automated tests (pytest)
├── exercises.py           ← Extension exercise stubs
└── solutions.py           ← Reference solutions for exercises
```

### Key Classes

```
Task (dataclass)
├── id: str               (UUID)
├── title: str
├── description: str
├── priority: str          ("low" | "medium" | "high")
├── due_date: Optional[str] (YYYY-MM-DD)
├── completed: bool
└── created_at: str        (ISO timestamp)

TaskManager
├── tasks: list[Task]
├── filepath: str
├── add_task(title, ...) -> Task
├── complete_task(task_id) -> bool
├── delete_task(task_id) -> bool
├── search_tasks(keyword) -> list[Task]
├── filter_by_priority(priority) -> list[Task]
├── filter_by_status(completed) -> list[Task]
├── get_overdue_tasks() -> list[Task]
├── save_to_file() -> None
└── load_from_file() -> None
```

---

## How to Run

### Start the application

```bash
python phase1/day20/task_manager.py
```

You will see an interactive menu:

```
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
----------------------------------------
Choose an option (1-9):
```

### Run the tests

```bash
pytest phase1/day20/test_task_manager.py -v
```

---

## Extension Ideas

After completing the base project, try extending it:

1. **Categories & Tags** — Add a `tags` field and filter by tag.
2. **Recurring Tasks** — Auto-create tasks on a daily/weekly schedule.
3. **Statistics Dashboard** — Show completion rate, overdue count, priority
   breakdown.
4. **CSV Export** — Export tasks to a spreadsheet-friendly CSV file.
5. **Undo Functionality** — Keep a history stack and undo the last action.

See `exercises.py` for guided stubs and `solutions.py` for reference
implementations.

---

## Key Takeaways

- A **mini-project** is the best way to solidify knowledge — you must make
  decisions about *which* tool to use, not just *how* to use it.
- **Dataclasses** reduce boilerplate when modelling domain objects.
- **JSON** is the simplest persistence format for structured data.
- **Regex search** is more powerful than basic `in` checks.
- **Generator-based filters** are memory-efficient and composable.
- **Automated tests** catch regressions before users do.
- **Error handling** turns a script into a robust application.

---

## Further Reading

- [Python `dataclasses` documentation](https://docs.python.org/3/library/dataclasses.html)
- [Python `json` module](https://docs.python.org/3/library/json.html)
- [Python `re` module](https://docs.python.org/3/library/re.html)
- [pytest documentation](https://docs.pytest.org/en/stable/)
- [Building CLI apps in Python (Real Python)](https://realpython.com/python-command-line-interfaces/)
