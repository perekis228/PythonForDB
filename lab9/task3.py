import openpyxl
from openpyxl.chart import PieChart, Reference

workbook = openpyxl.load_workbook('lab9.xlsx')
sheet = workbook.active

pie = PieChart()
labels = Reference(sheet, min_col=3, min_row=16, max_row=18)
data = Reference(sheet, min_col=4, min_row=15, max_row=18)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.title = "Средняя зарплата"

sheet.add_chart(pie, "J1")

workbook.save('lab9.xlsx')
workbook.close()