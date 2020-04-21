import xlrd     #module have to be installed via pip

#file location
loc = "file_location"

workbook = xlrd.open_workbook(loc)

sheet = workbook.sheet_by_index(0)


number = input()

for row in range(sheet.nrows):
    if sheet.cell_value(row, 2) == number:
        print(sheet.cell_value(row, 0), end = '     ')
        print(sheet.cell_value(row, 1), end = '     ')
        print(sheet.cell_value(row, 2), end = '     ')
        print(sheet.cell_value(row, 3), end = '     ')
        print(sheet.cell_value(row, 4), end = '     ')
        print(sheet.cell_value(row, 5), end = '     ')
        print(sheet.cell_value(row, 6), end = '     ')
        print(sheet.cell_value(row, 7), end = '     ')
        print(sheet.cell_value(row, 8), end = '     ')
        print(sheet.cell_value(row, 9), end = '     ')
        print(sheet.cell_value(row, 10))
