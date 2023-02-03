input_data = input('Введите цифры через "," или ";" или "/": ')
delimiter = ''
if ',' in input_data:
    delimiter = ','
elif ';' in input_data:
    delimiter = ';'
elif '/' in input_data:
    delimiter = '/'

elem_list = input_data.split(delimiter)
unique_list = []

for i in elem_list:
    if elem_list.count(i) == 1:
        unique_list.append(i)

print(unique_list)
