import os
from notion_client import Client


from pprint import pprint

list_users_response = notion.users.me()
pprint(list_users_response)

