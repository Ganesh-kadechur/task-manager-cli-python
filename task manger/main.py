import os
import json

# Create tasks.json
if not os.path.exists("data/tasks.json"):
    with open("data/tasks.json", "w") as f:
        json.dump([], f)  # Save empty list



def load_tasks():
    if not os.path.exists("data/tasks.json"):
        return[]
    with open("data/tasks.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return[]



def save_tasks(tasks):
    with open("data/tasks.json", "w") as f:
        json.dump(tasks,f, indent=4)

def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    new_task = {
        "task": task_name,
        "due": due_date,
        "done": False
    }

    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print(" No tasks found.")
        return

    for index,task in enumerate(tasks,1):
        status = "task completed" if task["done"] else "task not completed"
        print(f"{index}. {task['task']} (Due: {task['due']})[{status}]")

def mark_task_done():
    tasks = load_tasks()

    if not tasks:
        print(" No tasks found to mark as done.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done:"))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print(f" Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter the valid task number.")


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("----------No tasks found to delete.----------")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete:"))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f" Task deleted! {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter the valid task number.")


def main():
    while True:
        print("Welcome to Task Manger!")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_done()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                exit()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()


