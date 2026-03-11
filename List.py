#List - набор элементов в одной переменной упорядоченый, допускаются дубликаты индексы с 0
print("List")
list1 = [1, 2, 3, 4, 5]
print("Список list1:", list1)
# Новые элементы добавляются в конец
# List можно изменять после создания
# Длина List len(list)
print("Длина списка list1:", len(list1))
# Элементы списка могут быть любого типа. В одном списке могут быть элементы разного типа.
# Определение типа переменной type(list1)
print("Тип списка list1", type(list1))
# Конструктор
list2 = list([1, 2, 3])
list3 = list((1, 2, 3))
print("Список list2:", list2)
print("Список list3:", list3)
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''
# при отрицательной индексации отсчет начинается с конца
print("индекс отрицательный -1 в list1", list1[-1])
# Диапазон индексов начинается с первого значения включаемого до последнего не включаемого
print("Диапазон индексов list1:", list1[1:3])
# Если первое значение не указать, то начнется с начала
print("Диапазон list1 без указания начального элемента:", list1[:3])
# Если не указать последний элемент, то кончиться последним
print("Диапазон list1 без указания последнего значения", list1[1:])
# При указании отрицательных индексов
print("Вывод list1 с отрицательными индексами в диапазоне:", list1[-4:-1])
#Проверка существования элемента в List
print("Проверка существования 3 в list1:", 3 in list1)