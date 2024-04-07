import json
import src.to_day
import src.fetch_database_entries

def main():
    
    data = src.fetch_database_entries.main()
    data_json = json.loads(data)
    to_day_symbol = src.to_day.main()[0:3]

    def get_tasks_for_day(data, day):
        tasks = []
        for item in data:
            task_name = item["Task"]
            checkboxes = item["Checkboxes"]
            if day.capitalize() in checkboxes:
                tasks.append((task_name, checkboxes[day.capitalize()]))
        return tasks

    tasks = get_tasks_for_day(data_json, to_day_symbol)
    if tasks:
        print(f"Tasks for {to_day_symbol.capitalize()}:")
        for task_name, value in tasks:
            print(f"Task Name: {task_name}, Value: {value}")
    else:
        print(f"No tasks found for {to_day_symbol.capitalize()}")


if __name__ == "__main__":
    main()