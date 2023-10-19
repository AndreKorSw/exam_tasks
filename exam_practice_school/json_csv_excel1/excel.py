import xlsxwriter
from web_scrapper2_learning import array


def writer(parametr):
    workbook = xlsxwriter.Workbook(r'C:\Users\andre\Documents\web_scrap2.xlsx')
    worksheet = workbook.add_worksheet("товар")

    row = 0
    col = 0

    worksheet.set_column("A:A", 20)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 50)
    worksheet.set_column("D:D", 50)

    for item in parametr():
        worksheet.write(row, col, item[0])
        worksheet.write(row, col+1, item[1])
        worksheet.write(row, col+2, item[2])
        worksheet.write(row, col+3, item[3])
        row += 1
    workbook.close()
writer(array)