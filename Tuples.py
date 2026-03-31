#Tuples - кортеж коллекция упорядочненная неизменяемая, дублирование разрешено, индексы с 0,
Tuples1 = ("apple", "banana", "cherry")
#print("Tuples1:", Tuples1)
#print("Len(Tuples1):", len(Tuples1))
TuplesOneItem = ("apple",)
#print("TuplesOneItem:", TuplesOneItem, "Type TuplesOneItem:", type(TuplesOneItem), "len(TuplesOneItem):", len(TuplesOneItem))
# Tuple items type: string, number, boolean. Один  tuple содержит разные типы items.
# Tuple Constructor
Tuples2 = tuple(("apple", "banana", "cherry"))
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