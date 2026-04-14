#Sets
print("Sets")
# Sets are used to store multiple items in a single variable.
# Set: коллекция не упорядочненная, не изменяемая, не индексированная, дубликаты не допускаются
# Допускается удаление (remove), добавление (add) items in the set
# Записывается в фигурных скобках {}
# true & 1, false & 0 : считаются одинаковыми значениями
# в одном set могут содержаться разные типы значений
set1 = {"value1", "value2", "value3", "value4"}
print("set1:", set1)
# длина set
'''print("Длина set1:", len(set1))'''
# Проверка типа
'''print("Type set1:", type(set1))
print(type(set1) == set)'''
# Constructor set((listVar))
set2 = set(("value3","value4", "value5", "value6"))
print("set2:", set2)
# доступ к items  по индексу, ключу - не возможен
# Перебор в цикле for
'''for item in set1:
    print("Item:", item)'''
# Проверка присутствия item в set
'''print("value1 in set1:", "value1" in set1)
print("value4 not in set1:", "value4" not in set1)'''
# Добавление item в set
# print("set2:", set2)
#set2.add("value7")
# print("set2:", set2)
# добавление items из набора. Набором может быть list, tuple, dictonaries дубликаты исключаются
set3 = {"value8", "value9"}
print("set3:", set3)
''' set2.update(set1)'''
list1 = ("value10", "value11")
print ("list1", list1)
'''print("union set1, set2, set3, list1:", set1.union(set2, set3, list1)) # объединяет коллекции все'''
'''print("set1 | set2 | set3",  set1 | set2 |set3)# объединяет множества только'''

# удаление items из set
# print("set2:", set2)
# set2.remove("value7") # если item не существует - будет сообщение об ошибке
# set2.discard("value7")# если item не существует - будет сообщение об ошибке не будет
# print("set2:", set2)
# Удаление случайного item из set
# print("set2:", set2)
# print("удаленный item:", set2.pop())
# print("set2:", set2)
# Очистка set
'''' print("set2:", set2)
print("Очистка set2")
set2.clear()
print("set2:", set2)'''
# Удаление set
'''print("set2:", set2)
print("удаление set2")
del set2
print("set2:", set2)''' 
# Пересечение sets
'''print("set1.intersection(set2)", set1.intersection(set2))# объединяет коллекции
print("set1 & set2", set1 & set2)# Объединяет sets
set4 = set1
print("set4:", set4)
set4.intersection_update(set2)# мзменяет исзодный set
print("set4.intersection_update(set2):", set4)'''
# Возвращает set1.items которых нет в set2
'''print("set1.difference(set2):", set1.difference(set2))# collections
print("set1 - set2:", set1 - set2)# sets
set5 = set1
print("set5:", set5)
set5.difference_update(set2)
print("set5.difference_update(set2):", set5)'''
# items отсутствующие в обоих sets (не пересекающиеся)
'''set6 = set1.symmetric_difference(set2)
print("set6 = set1.symmetric_difference(set2):", set6)
set7 = set1 ^ set2
print("set7 = set1^set2:", set7)
set8 = set1
set8.symmetric_difference_update(set2)
print("set8 = set1.symmetric_difference_update(set2):", set8)# изменяет исходный набор'''
# fronzen set - set нельзя добавлять, удалять items
'''frozenset1 = frozenset({"value11", "value12", "value13"})
print("frozenset1:", frozenset1, "type(frozenset1):", type(frozenset1))'''