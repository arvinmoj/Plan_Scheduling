def get_tasks_for_day(data, day):
    tasks = []
    for item in data:
        task_name = item["Task"]
        checkboxes = item["Checkboxes"]
        if day.capitalize() in checkboxes:
            tasks.append((task_name, checkboxes[day.capitalize()]))
    return tasks

data = [
    {"Task": "Task-3", "Checkboxes": {"Mon": False, "Sun": True, "Fri": False, "Tue": True, "Sat": False, "Wed": False, "Thu": True}},
    {"Task": "Task-2", "Checkboxes": {"Mon": True, "Sun": False, "Fri": False, "Tue": False, "Sat": True, "Wed": True, "Thu": False}},
    {"Task": "Task-1", "Checkboxes": {"Mon": True, "Sun": True, "Fri": True, "Tue": True, "Sat": True, "Wed": True, "Thu": True}}
]

day = "mon"  # Specify the day you want to get the values for, e.g., "mon", "tue", etc.

tasks = get_tasks_for_day(data, day)
if tasks:
    print(f"Tasks for {day.capitalize()}:")
    for task_name, value in tasks:
        print(f"Task Name: {task_name}, Value: {value}")
else:
    print(f"No tasks found for {day.capitalize()}")
