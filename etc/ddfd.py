import requests

integration_token = "secret_BRFpq7gEYhabxTWGsZLBR2D8XhPe5ybcnsWbpNlmfmK"
database_url = "ab2eb050-4446-4413-820a-e5acf4631f5a"

headers = {
    "Authorization": f"Bearer {integration_token}",
    "Content-Type": "application/json",
"Notion-Version": "2022-06-28",
}

response = requests.post(
    "https://api.notion.com/v1/databases",
    headers=headers,
    json={"database_id": database_url},
)

database_id = response.json().get("id")
print(f"Database ID: {database_id}")
print(response.json())
