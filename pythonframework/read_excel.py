import xlrd


def get_data():
    workbook = xlrd.open_workbook(r"C:\Users\Lenovo\Desktop\Practice\TestData.xlsx")
    worksheet = workbook.sheet_by_name("Employee")
    rows = worksheet.get_rows()
    header = next(rows)
    data = []
    for row in rows:
        temp = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
        data.append(temp)
    return data
