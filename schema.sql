CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    task_priority INTEGER NOT NULL,
    task_date DATE NOT NULL,
    task_hour HOUR NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    status INTEGER NOT NULL DEFAULT (1)
);
