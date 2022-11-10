# Importing required libraries
import pygsheets as pyg
import pandas as pd 
import os

#set working directory
pwd = os.getcwd()
#os.chdir(pwd)

# Create the Client
# Enter the name of the downloaded KEYS 
# file in service_account_file
client = pyg.authorize(service_account_file=pwd+"\DBT module\Sheets test keys\pygsheets-pandas-dbt-test-353a16742b53.json")
  
# Sample command to verify successful
# authorization of pygsheets
# Prints the names of the spreadsheet
# shared with or owned by the service 
# account
#print(client.spreadsheet_titles())

#assign name of spreadsheet
dbt_sheet = "pygsheets-pandas-dbt-test-sheet"

# opens a spreadsheet by its name/title
spreadsheet = client.open(dbt_sheet)
  
# opens a worksheet by its name/title
worksheet = spreadsheet.worksheet("title", "Sheet1")
  
# Now, let's add data to our worksheet
  
# Creating the first column
worksheet.cell("A1").set_text_format("bold", True).value = "Item"
  
# if updating multiple values, the data
# should be in a matrix format
worksheet.update_values("A2:A6", [["Pencil"], ["Eraser"], 
                                ["Sharpener"], ["Ruler"], 
                                ["Pen"]])  # Adding row values
  
# Similarly, creating the second column
worksheet.cell("B1").set_text_format("bold", True).value = "Price"
worksheet.update_values("B2:B6", [[5], [3], [5], [15], [10]])
  
# Creating a basic bar chart
worksheet.add_chart(("A2", "A6"), [("B2", "B6")], "Shop")
