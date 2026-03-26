#Tuples - кортеж коллекция упорядочненная неизменяемая, дублирование разрешено, индексы с 0,
Tuples1 = ("apple", "banana", "cherry")
print("Tuples1:", Tuples1)
print("Len(Tuples1):", len(Tuples1))
TuplesOneItem = ("apple",)
print("TuplesOneItem:", TuplesOneItem, "Type TuplesOneItem:", type(TuplesOneItem), "len(TuplesOneItem):", len(TuplesOneItem))
# Tuple items type: string, number, boolean. Один  tuple содержит разные типы items.
# Tuple Constructor
Tuples2 = tuple(("apple", "banana", "cherry"))
print("Tuples2:", Tuples2)