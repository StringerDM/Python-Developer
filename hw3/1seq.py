elem_qty = int(input('Введите количество элементов списка: '))

elem_list = []

for i in range(elem_qty):
    elem_list.append(int(input('Введите число: ')))

elem_list.sort()
print(elem_list)
