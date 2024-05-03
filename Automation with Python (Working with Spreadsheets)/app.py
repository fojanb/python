import openpyxl
from colors import CYAN,MAGENTA,BRIGHT_YELLOW,RESET
# Read an excel file from the current directory on your local machine.
# sample_data_all = SampleData.xlsx with all of the sheets inside of it.
sample_data_all = openpyxl.load_workbook("SampleData.xlsx")
# Select the desired 'sheet' we want to work on it.
# SampleData.xlsx = {"Instructions":[], "SalesOrders":[] , "MyLinks":[]}.
SalesOrders = sample_data_all["SalesOrders"]
products_per_rep = {}
for product_row in range(SalesOrders.max_row - 1) :
    rep = SalesOrders.cell(product_row + 2,3).value;
    if rep in products_per_rep:
        products_per_rep[rep] = products_per_rep[rep] + 1
    else:
        # Adding new rep to products_per_rep
        products_per_rep[rep] = 1
print("-------------- ✿ --------------")
print(MAGENTA + "\n1- List each buyer(rep) with respective product count" + BRIGHT_YELLOW + "\nAns: "+ CYAN + f"{products_per_rep}\n" + RESET)
print("-------------- ✿ --------------")
print(MAGENTA + "\n2- How many buyer(rep) in the excel sheet?" + BRIGHT_YELLOW + "\nAns: " + CYAN + f"{len(products_per_rep)}\n" + RESET)
print("-------------- ✿ --------------")
# 3 - Sort the byuers list alphabetically
print(MAGENTA + "\n3- Sort the byuers list alphabetically" + BRIGHT_YELLOW + "\nAns: "+ CYAN + f"{5}\n" + RESET)



