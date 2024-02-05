import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date
import pandas as pd

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "high-triode-283417-cdca1a47ea5e.json", scope
)


class BudgetTracker:
    def __init__(self):
        # Define the scope and credentials
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "high-triode-283417-cdca1a47ea5e.json", scope
        )

        # Authorize the client
        self.client = gspread.authorize(credentials)

        # Open the Google Spreadsheet by its title
        self.spreadsheet = self.client.open("Budget")
        print("Worksheets in the spreadsheet:")
        worksheets = self.spreadsheet.worksheets()
        ws_index = None
        for index, worksheet in enumerate(worksheets):
            print(f"{index}. {worksheet.title}")
            if worksheet.title == "Feb Expense":
                ws_index = index
        print()
        self.worksheet = self.spreadsheet.get_worksheet(ws_index)

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

    def amount_spend(self):
        user_date = date.today()
        user_date = user_date.strftime("%d/%m/%Y")
        # Calculate total spent for the day and print
        cell_list = self.worksheet.findall(user_date)
        total_spent = 0
        for cell in cell_list:
            row_values = self.worksheet.row_values(cell.row)
            total_spent += float(row_values[-1])  # Assuming price is the last column
        print(f"Total amount spent on {user_date}: Rs {total_spent}")

    def total_spent_per_item(self):
        # Initialize a dictionary to store total money spent per item
        total_spent_per_item = {}

        # Get all the data from the worksheet
        all_data = self.worksheet.get_all_values()

        # Find the index of the header row (assuming it's always in row 6)
        header_row_index = 5

        # Iterate through each row starting from the header row
        for row_index in range(header_row_index + 1, len(all_data)):
            row = all_data[row_index]

            try:
                # Extract data from the row
                date, category, item, price = row[:4]  # Consider only columns A to D

                # Skip rows where price is empty or not a valid number
                if not price.strip() or not price.strip().isdigit():
                    continue

                # Check if the item is already in the dictionary, if not, initialize it with 0
                if item not in total_spent_per_item:
                    total_spent_per_item[item] = 0

                # Add the price to the total spent for the item
                total_spent_per_item[item] += float(price)
            except ValueError:
                print(f"Skipping invalid row: {row}")

        # Print item name and total money spent on it
        for item, total_spent in total_spent_per_item.items():
            print(f"{item}, Rs {total_spent}")


# Usage:
# Create an instance of BudgetTracker
budget_tracker = BudgetTracker()
# # Add multiple data entries without exiting the program
budget_tracker.add_multiple_data()
