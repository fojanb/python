import openpyxl
from colors import CYAN,MAGENTA,RESET
# Read an excel file from the current directory on your local machine.
# sample_data_all = SampleData.xlsx with all of the sheets inside of it.
sample_data_all = openpyxl.load_workbook("SampleData.xlsx")
# Select the desired 'sheet' we want to work on it.
# SampleData.xlsx = {"Instructions":[], "SalesOrders":[] , "MyLinks":[]}.
SalesOrders = sample_data_all["SalesOrders"]
products_per_supplier = {}
for product_row in range(SalesOrders.max_row - 1) :
    rep = SalesOrders.cell(product_row + 2,3).value;
    if rep in products_per_supplier:
        products_per_supplier[rep] = products_per_supplier[rep] + 1
    else:
        # Adding new rep
        products_per_supplier[rep] = 1
    print(CYAN + f"{rep} : " + MAGENTA + f"{products_per_supplier[rep]}" + RESET)
# List each buyer(rep) with respective product count
# print(CYAN + f"\n{products_per_supplier}\n" + RESET)