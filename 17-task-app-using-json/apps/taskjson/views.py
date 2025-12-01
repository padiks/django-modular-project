import json
import os
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime
# from django.utils import timezone

# Define the path to the JSON file
TASKS_FILE = os.path.join(settings.MEDIA_ROOT, 'tasks.json')

# Ensure the JSON file exists
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)  # Initialize with an empty list

# Read tasks from the JSON file
def read_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Write tasks to the JSON file
def write_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Index view to list all tasks
def index(request):
    # Get logged-in user's primary group
    user_groups = request.user.groups.values_list('name', flat=True)
    user_group = user_groups[0] if user_groups else None

    tasks = read_tasks()  # Get tasks from the JSON file

    # Format the created_at field for each task
    for task in tasks:
        created = task.get("created_at", "")

        if isinstance(created, str):
            # Remove milliseconds if present
            cleaned = created.split(".")[0]

            try:
                # Convert string to datetime (ISO format: 2025-12-01T14:20:55)
                dt = datetime.strptime(cleaned, "%Y-%m-%dT%H:%M:%S")
                # Format as: 1 December 2025
                task["created_at"] = dt.strftime("%-d %B %Y")
            except ValueError:
                # If parsing fails, leave original
                task["created_at"] = created

    return render(request, 'taskjson/index.html', {
        'title': 'Task using JSON',
        'json_file': tasks,        # Pass the tasks as context to the template
        'user_group': user_group,  # Pass user group to the template
    })


# Add new task (Create)
def create_task(request):
    # Check if the user is in the 'Admin' group
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to add tasks.")
        return redirect('taskjson:index')

    if request.method == "POST":
        task_name = request.POST.get('task', '')
        if task_name:
            tasks = read_tasks()
            new_task = {
                "id": len(tasks) + 1,  # Increment the ID
                "task": task_name,
                "completed": False,
                "created_at": datetime.now().isoformat()  # Add creation timestamp
            }
            tasks.append(new_task)
            write_tasks(tasks)
            return redirect('taskjson:index')  # Redirect to the task list

    return render(request, 'taskjson/create_task.html', {
        'title': 'Add New Task'
    })

# Edit an existing task (Update)
def edit_task(request, task_id):
    # Check if the user is in the 'Admin' group
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to edit tasks.")
        return redirect('taskjson:index')

    tasks = read_tasks()

    # Find the task by ID (search manually, not using get_object_or_404)
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        messages.error(request, "Task not found.")
        return redirect('taskjson:index')  # Redirect back to the task list if not found

    if request.method == "POST":
        task['task'] = request.POST.get('task', task['task'])
        task['completed'] = 'completed' in request.POST  # Mark as completed if checked
        write_tasks(tasks)
        return redirect('taskjson:index')  # Redirect to the task list

    return render(request, 'taskjson/edit_task.html', {
        'title': 'Edit Task',
        'task': task
    })

# Delete a specific task (Delete)
def delete_task(request, task_id):
    # Check if the user is in the 'Admin' group
    if not (request.user.is_superuser or request.user.groups.filter(name='Admin').exists()):
        messages.warning(request, "You do not have permission to delete tasks.")
        return redirect('taskjson:index')

    tasks = read_tasks()

    # Find the task by ID (search manually, not using get_object_or_404)
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        messages.error(request, "Task not found.")
        return redirect('taskjson:index')  # Redirect back to the task list if not found

    tasks.remove(task)  # Remove the task from the list
    write_tasks(tasks)
    return redirect('taskjson:index')  # Redirect to the task list
