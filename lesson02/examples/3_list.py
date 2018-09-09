# =================================
#             Списки
# =================================

# Список - изменяемая последовательность, элементами которой могут быть любые типы данных
empty_list = []  # пустой список
my_list = [1, 3, 5, 3.45, 'ddd', 's', 333]
print('my_list = ', my_list)
# Т.к. список является последовательностью, с ним можно выполнять те же операции что и со строкой:
# Получение элемента по индексу
print(my_list[0])   # получим первый элемент списка
print(my_list[-1])  # последний элемент списка
# Срезы
print(my_list[0:-3])  # 3 последних элемента списка
# Конкатенация
print(my_list[0:3] + [7, 8, 9])  # получим новый список из 6 элементов
# Мультипликация
print([3, '4'] * 3)  # размножим список
# В отличие от строк, элементы списка можно изменять:
my_list[2] = 'New'
print('my_list after change =', my_list)
# А также заменять часть элементов с помощью срезов. Заменим первые 3:
my_list[0:3] = [2, 4, 6]
print(my_list)
# удалим последние 2
my_list[-2:] = []
print(my_list)
# вставим несолько элементов внутрь
my_list[3:3] = ['this', 'is', 'some', 'elements']
print(my_list)

# вставим элемент в начало списка
my_list[:0] = ['first']
print(my_list)

# Как и для строк, встроенная функция len() вернет длину списка:
print(len(my_list))

# Добавить что-то в конец списка можно так:
my_list[len(my_list):] = [100]
print(my_list)

# Но чаще все-таки используется такая более простая конструкция (простое лучше сложного, помните?):
my_list.append(100)
print(my_list)

# Можно создавать списки, содержащие другие списки:
b = [1, 2, 3, [11, 22, 33], 5, 6]
print('b = ', b)
print('b[3][2] =', b[3][2])

# Оператор вхождения in
print('2 in b -->', 2 in b)
print("'2' in b -->", '2' in b)

# Также у списков есть свои методы. Выше показан метод .append()
# Большинство методов изменяют список, к которому применяются, т.к. список изменяемый
# Подробнее о методах списка см. в справочниках
