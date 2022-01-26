import xlrd

loc = ("summary.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

a = []

for i in range(sheet.nrows):
    a.append(sheet.cell_value(i, 1))
print(*a, sep='\n')
# print(a)
