#Tuples - кортеж коллекция упорядочненная неизменяемая, дублирование разрешено, индексы с 0,
Tuples1 = ("apple", "banana", "cherry")
#print("Tuples1:", Tuples1)
#print("Len(Tuples1):", len(Tuples1))
TuplesOneItem = ("apple",)
#print("TuplesOneItem:", TuplesOneItem, "Type TuplesOneItem:", type(TuplesOneItem), "len(TuplesOneItem):", len(TuplesOneItem))
# Tuple items type: string, number, boolean. Один  tuple содержит разные типы items.
# Tuple Constructor
Tuples2 = tuple(("apple2", "banana2", "cherry2"))
#print("Tuples2:", Tuples2)
#Access tuple items индексация с конца "-1" - последний элемент
#print("Tuples1[1]:", Tuples1[1])
#print ("Tuples1[-1]",Tuples1[-1])
#range последний элемент параметра ограничения не включается 
#print("Tuples1[1:3]", Tuples1[1:3]) #1,2
#Если не указать первый элемент, то диапазон начнется с начала tuple
#print ("Tuples1[:3]", Tuples1[:3])
#Если не указать в параметре последний элемент диапазона, то диапазон закончится последним tuple items
#print("Tuples[0:]", Tuples1[0:])
#Диапазон с отрицательными индексами
#print("Tuples1[-3:-1]", Tuples1[-3:-1])
#Проверка присутствия a item in a tuple
#print("apple is present in the Tuples1:", "apple" in Tuples1)
#Для изменения Tuple его преобразовывают в List, изменяют Item, List преобразовывают в Tuple
'''
print("Tuples1:", Tuples1)
List1 = list(Tuples1)
print("List1:", List1)
List1[1] = "kiwi"
print("List1 modified", List1)
Tuples1 = tuple(List1)
print("Tuples1 modofied:", Tuples1)'''
#Добавление кортежа 
'''
Tuples1 += Tuples2
print("Tuples1 extended:", Tuples1)'''
#Удаление tuples
'''del Tuples1
print(Tuples2)
del Tuples2
print(Tuples2)'''
#разборка tuples
'''(i1, i2, i3) = Tuples1
print("i1:", i1)
print("i2:", i2)
print("i3:", i3)'''
# Если количество переменных меньше размера Tuple, нужно к одной из перменных добавить *. тогда эта переменная будет списком с оставшмися переменными
'''(i1, *l1) = Tuples1
print("i1:", i1)
print("list:", l1)'''
#for
'''
for item in Tuples1:
    print("Tuple1 item:", item)
for index in range(len(Tuples1)):
    print("Tuples1 item", index, ":", Tuples1[index])'''
#while
'''
index = 0
while index < len(Tuples1):
    print("Tuples1 item", index, ":", Tuples1[index])
    index += 1'''
#Tuples можно складывать, умножать на число
'''print(" Tuples1 + Tuples2:", Tuples1 + Tuples2)
print("Tuples1 * 2:", Tuples1 * 2)'''