import json
import requests

# Replace these variables with your own values
DATABASE_ID = "2ffff1977b6945c79af87e16731f3855"
INTEGRATION_TOKEN = "secret_iZRQg1cmxIr9uNRLlabO0zRQSzORXlQWK4ckuuOEEKF"

# Endpoint for retrieving database entries
DATABASE_URL = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": f"Bearer {INTEGRATION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"  # Current API version
}

def fetch_database_entries():
    response = requests.post(DATABASE_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

def main():
    
    results = []

    # Fetch database entries
    database_entries = fetch_database_entries()
    if database_entries:
        for entry in database_entries:
            # Modify this part according to your database structure
            properties = entry.get("properties", {})
            title = properties.get("Task", {}).get("title", [{"plain_text": ""}])[0]["plain_text"]
            checkboxes = {day: properties['checkbox'] for day, properties in entry['properties'].items() if day != 'Task'}
            
            # Print or process your data here
            # print(f"Task: {title}, Checkboxes: {checkboxes}")

            # Append data to results list
            results.append({"Task": title, "Checkboxes": checkboxes})
      
    else:
        print("No entries found in the database.")

    # Convert results to JSON and return
    return json.dumps(results)

if __name__ == "__main__":
    main()
