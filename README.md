# Task CLI Project

<<<<<<< HEAD
Project URL: https://github.com/your-username/task_cli


A simple CLI tool for managing tasks...

Project Page Url : https://github.com/Neo110Matrix/task_cli



A simple command-line task manager built with Python. This project allows you to create, update, delete, and manage tasks directly from your terminal.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as **in progress**
* Mark tasks as **done**
* List all tasks
* List tasks by status
* Persistent storage using JSON

---

## Installation
### Option 1: Using pip

create your virtual environment

pip install Neo-task-cli

task-cli list

### Option 2: Clone and Install

git clone https://github.com/YOUR_GITHUB_USERNAME/task-cli.git

cd task-cli

pip install -e


## Verify Installation

After installation, run:

task-cli

or

task-cli list

If the command works, the installation was successful.

## Usage

### Add a Task

task-cli add "Learn Python generators"

Example Output:

#OUTPUT
Task added successfully. ID: 1

### Update a Task

task-cli update 1 "Learn Python generators and decorators"

Example Output:

Task updated successfully.

### Delete a Task

task-cli delete 1

Example Output:

Task deleted successfully.

### Mark a Task as In Progress

task-cli mark-in-progress 1

Example Output:

Task marked as in progress.

### Mark a Task as Done

task-cli mark-done 1

Example Output:

Task marked as done.

### List All Tasks

task-cli list

Example Output:

ID          : 1
Description : Learn Python generators
Status      : done
Created At  : 22 Jun 2026 12:45 PM
Updated At  : 22 Jun 2026 01:10 PM

### List Only Completed Tasks

task-cli list done

### List Only Pending Tasks

task-cli list todo

### List Tasks In Progress

task-cli list in-progress

## Data Storage

Tasks are stored in a local JSON file.

Example:

json
[
    {
        "id": 1,
        "description": "Learn Python generators",
        "status": "done",
        "created_at": "2026-06-22T12:45:26",
        "updated_at": "2026-06-22T13:10:11"
    }
]

## Project Structure

task-cli/    
│    
├── main.py    
├── pyproject.toml    
├── README.md    
│                   
└── task_manager/    
            ├── __init__.py       
            ├── task_service.py            
            └── task.json            


## Technologies Used

* Python 3
* JSON
* pathlib
* datetime
* pip packaging
* pyproject.toml


## Future Improvements

* Task priorities
* Due dates
* Search functionality
* Categories and tags
* SQLite database support
* Export tasks to CSV


## Author

Arjun Jayakumar

GitHub: https://github.com/Neo110Matrix/task_cli
