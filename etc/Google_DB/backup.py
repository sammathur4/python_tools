import gspread
import pandas as pd
import arrow
from oauth2client.service_account import ServiceAccountCredentials
import io
from datetime import datetime, date

# Define the scope and credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "../../secrets/high-triode-283417-cdca1a47ea5e.json", scope
)
#
# # Authorize the client
# client = gspread.authorize(credentials)
#
# # Open the Google Spreadsheet by its title
# spreadsheet = client.open("Budget")
#
# # Select the first worksheet
# worksheet = spreadsheet.get_worksheet(4)
#
# # Get all values from the worksheet
# data = worksheet.get_all_values()
# df = pd.DataFrame(data[1:], columns=data[0])
#
# try:
#     # Get today's date
#     today = date.today()
#     spreadsheet_title, worksheet_index = "Budget", 4
#     # Open the Google Spreadsheet by its title
#     spreadsheet = client.open(spreadsheet_title)
#
#     # Select the worksheet by its index
#     worksheet = spreadsheet.get_worksheet(worksheet_index)
#
#     # Prompt user for data
#     date_input = input("Enter Date (DD/MM/YYYY): ")
#     # Check if the input is empty
#     if date_input:
#         try:
#             # Parse the input date if provided
#             user_date = datetime.strptime(date_input, "%d/%m/%Y").date()
#         except ValueError:
#             print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
#             exit()
#     else:
#         # If no input is provided, use today's date as default
#         user_date = today
#     user_date = user_date.strftime("%d/%m/%Y")
#     # Define categories and prompt user to choose a category number
#     categories = ["Bills", "Needs", "Wants", "Future You", "UnPlanned"]
#     print("Categories:")
#     for i, category in enumerate(categories, start=1):
#         print(f"{i}. {category}")
#
#     category_index = int(input("Enter the number corresponding to the category: ")) - 1
#     if not 0 <= category_index < len(categories):
#         print("Invalid category number. Please try again.")
#         exit()
#     category = categories[category_index]
#     item = input("Enter Item: ")
#     price = input("Enter Price: ")
#
#     # Append the data to the worksheet
#     worksheet.append_row([user_date, category, item, price])
#     print("Data added successfully.")
#
# except Exception as e:
#     print("An error occurred:", e)


class BudgetTracker:
    def __init__(self):
        # Define the scope and credentials
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "../../secrets/high-triode-283417-cdca1a47ea5e.json", scope
        )

        # Authorize the client
        self.client = gspread.authorize(credentials)

        # Open the Google Spreadsheet by its title
        self.spreadsheet = self.client.open("Budget")

        # Select the first worksheet
        self.worksheet = self.spreadsheet.get_worksheet(4)

    def _get_info(self):
        # Search for specific keywords in the  and print their corresponding rows
        keywords = [
            "Total Income",
            "Bills",
            "Needs",
            "Unplanned",
            "Total Expenditure",
            "Total Left",
        ]
        for keyword in keywords:
            cell = self.worksheet.find(keyword)
            row = cell.row
            data = self.worksheet.row_values(row)
            keyword_index = data.index(keyword)
            value = data[keyword_index]
            print(f"{keyword}: {data[-1]}")

    def add_data(self):
        try:
            # Get today's date
            today = date.today()

            # Prompt user for data
            date_input = input("Enter Date (DD/MM/YYYY): ")
            # Check if the input is empty
            if date_input:
                try:
                    # Parse the input date if provided
                    user_date = datetime.strptime(date_input, "%d/%m/%Y").date()
                except ValueError:
                    print(
                        "Invalid date format. Please enter the date in DD/MM/YYYY format."
                    )
                    return budget_tracker.add_multiple_data()
            else:
                # If no input is provided, use today's date as default
                user_date = today
            user_date = user_date.strftime("%d/%m/%Y")
            # Define categories and prompt user to choose a category number
            categories = ["Bills", "Needs", "Wants", "Future You", "UnPlanned"]
            print("Categories:")
            for i, category in enumerate(categories, start=1):
                print(f"{i}. {category}")

            category_index = (
                int(input("Enter the number corresponding to the category: ")) - 1
            )
            if not 0 <= category_index < len(categories):
                print("Invalid category number. Please try again.")
                return budget_tracker.add_multiple_data()
            category = categories[category_index]
            item = str(input("Enter Item: "))
            price = int(input("Enter Price: "))

            # Append the data to the worksheet
            self.worksheet.append_row([user_date, category, item, price])
            print("Data added successfully.")

        except Exception as e:
            print("An error occurred:", e)
            print("Please try again")
            budget_tracker.add_multiple_data()

    def add_multiple_data(self):
        record = True
        while record:
            self.add_data()
            cont = input("Do you want to add more data? (yes/no): ").lower()
            if not cont.startswith("y") or cont.startswith("n"):
                record = False
        if not record:
            print("Review The Expenses.", "\n")
            self._get_info()


# Usage:
# Create an instance of BudgetTracker
budget_tracker = BudgetTracker()
budget_tracker._get_info()

# Add multiple data entries without exiting the program
budget_tracker.add_multiple_data()
