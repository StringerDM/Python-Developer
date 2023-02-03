input_data_1 = input('Введите цифры через ",": ')
input_data_2 = input('Введите цифры через ",": ')

elem_list1 = input_data_1.split(',')
elem_list2 = input_data_2.split(',')

for i in elem_list2:
    while i in elem_list1:
        elem_list1.remove(i)

print(elem_list1)

