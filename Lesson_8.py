
'''Дописать функцию так, чтобы она возвращала None в случае если ключа
нет, а не генерировала исключение (для реализации используем
исключения)'''
dict_ = {
    'марафон': 'гонка бегунов длиной около 26 миль',
    'персона': 'человек',
    'бежал': 'бежать в прошедшем времени'
         }
key = 'марафон2'
def func(dict_, key):
    try: 
        dict_[key]
    except KeyError:
        print('Ошибка после KeyError')
        return None
    print(dict_[key])
    return dict_[key]
func(dict_, key)


'''Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл. Затем 
открыть файл на редактирование и дозаписать оставшиеся 2 строки. В итогом
файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.'''

string1 = input()
string2 = input()
string3 = input()
string4 = input()
with open("lists.txt", "w") as file:
    file.write(string1 + "\n")
    file.write(string2 + "\n")
with open("lists.txt", "a") as file:
    file.write(string3 + "\n")
    file.write(string4 + "\n")


'''3. Создать словарь в качестве ключа которого будет 6-ти значное число (id), ав
качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
Сделать около 5-6 элементов словаря. Записать данный словарь на диск в }50п-файл.'''
import json
data = {
    123456: ('Alis', 25),
    234567: ('Ivan', 30),
    345678: ('Mary', 22),
    456789: ('Ihar', 28),
    567890: ('Ann', 32),
    678901: ('Serg', 29)
}

with open("data_file.json", "w+") as write_file:
    json.dump(data, write_file)

'''4. Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.'''

with open("data_file.json") as read_file:
    data = json.load(read_file)

with open('sw_data.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    headers = ['id', 'name', 'age', 'телефон']
    writer.writerow(headers)
    for key, value in data.items():
        writer.writerow([key, value[0], value[1]])

'''5. Прочитать сохранённый csv-файл и сохранить данные
в ехсе|-файл, кроме возраста - столбец с этими данными
не нужен. Таблица должна выглядеть, как на примере:'''
import openpyxl
import csv

with open('sw_data.csv', 'r') as f:
    reader = csv.reader(f)
    # Используем метод list() для преобразования
    # возвращаемого объекта csv.reader в список
    csv_data = list(reader)

# Удаляем столбец, который не нужен
for row in csv_data:
    del row[2]  # удаление столбца с индексом 2

# Создаем книгу Excel и рабочий лист
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Записываем данные из списка csv_data в ячейки Excel
row_num = 1
for row in csv_data:
    col_num = 1
    for cell_value in row:
        worksheet.cell(row=row_num, column=col_num, value=cell_value)
        col_num += 1
    row_num += 1

# Сохраняем книгу Excel в файл
workbook.save('my_file.xlsx')