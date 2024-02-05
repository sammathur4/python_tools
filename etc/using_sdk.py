import os
from notion_client import Client
NOTION_TOKEN = "secret_BRFpq7gEYhabxTWGsZLBR2D8XhPe5ybcnsWbpNlmfmK"
notion = Client(auth="secret_BRFpq7gEYhabxTWGsZLBR2D8XhPe5ybcnsWbpNlmfmK")


from pprint import pprint

list_users_response = notion.users.me()
pprint(list_users_response)

