#Sets
print("Sets")
# Sets are used to store multiple items in a single variable.
# Set: коллекция не упорядочненная, не изменяемая, не индексированная, дубликаты не допускаются
# Допускается удаление (remove), добавление (add) items in the set
# Записывается в фигурных скобках {}
# true & 1, false & 0 : считаются одинаковыми значениями
# в одном set могут содержаться разные типы значений
set1 = {"value1", "value2", "value3"}
'''print("set1:", set1)'''
# длина set
'''print("Длина set1:", len(set1))'''
# Проверка типа
'''print("Type set1:", type(set1))
print(type(set1) == set)'''
# Constructor set((listVar))
set2 = set(("value4", "value5", "value6"))
# print("set2:", set2)
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
# добавление items из набора. Набором может быть list, tuple, dictonaries
# print("set2:", set2)
# set2.update(set1)
# print("set2:", set2)
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