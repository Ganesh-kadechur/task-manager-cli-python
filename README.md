# Task Manager CLI

A command-line task management application built with Python.

## Features
- ✅ Add new tasks
- ✅ Mark tasks as complete
- ✅ Delete tasks
- ✅ List all tasks
- ✅ JSON file storage

## Installation
```bash
# Clone the repository
git clone https://github.com/Ganesh-kadechur/task-manager-cli-python.git

# Navigate to project directory
cd task-manager-cli-python

# Install dependencies (if any)
pip install -r requirements.txt

# Run the application
python main.py

# Add a new task
python main.py add "Complete Python project"

# List all tasks
python main.py list

# Mark task as complete
python main.py complete 1

# Delete a task
python main.py delete 1

task-manager-cli-python/
│
├── main.py              # Main application entry point
├── task_manager.py      # Core task management logic
├── tasks.json          # Task storage file
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
