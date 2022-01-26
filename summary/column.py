import openpyxl
wb = openpyxl.load_workbook('trash/summary.xlsx')
sheet = wb.sheet_by_index(0)
ws = wb['sheet1']

summary = []
for s in summary:
    summary.append(s.value)
print(summary)
