import openpyxl
import json
##теперь создаем эксель файл
book=openpyxl.Workbook()
sheet=book.active

with open("all_data_dict.json") as file:
    data=json.load(file)


#Заголовки
sheet["A1"]="ТОВАР"
sheet["B1"]="ЦЕНА"
sheet["C1"]="ССЫЛКА"

row=2
for item in data:
    sheet[row][0].value=item
    sheet[row][1].value=data[item][1]
    sheet[row][2].value=data[item][0]
    row+=1
book.save("my_json_to_excel1.xlsx")
book.close()


