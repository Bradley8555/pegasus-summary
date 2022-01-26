# import module
import openpyxl

# load excel with its path
wrkbk = openpyxl.load_workbook("../output.xlsx")

sh = wrkbk.active

# iterate through excel and display data
for row in sh.iter_rows(min_row=1, min_col=1, max_row=10, max_col=2):
    for cell in row:
        print(cell.value, end=" ")
    print()

