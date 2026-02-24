#Types:
print("Types")
#Getting the Data Type: type(var)
#text:str
text1 = "text"
text2 = str("text2")
print("Text1:", type(text1), text1)
#numeric: int, float, complex. You can convert Numbers кроме complex
num_int1 = 20
num_int2 = int(20)
print("num_int1:", type(num_int1), num_int1)
num_float1 = 3.14
num_float2 = float(3.666)
num_float3 = 3e5
print("num_float1:", type(num_float1), num_float1)
print("num_float3:", type(num_float3), num_float3)
num_complex1 = 1j
num_complex2 = complex(2j)
print("num_complex1:", type(num_complex1), num_complex1)
#Sequence (последовательности): list(список), tuple(кортеж), range(диапазон)
list1 = [1, 2, 3]
list2 = list((4, 5, 6))
print("list1:", type(list1), list1)
tuple1 = (1, 2, 3)
tuple2 = tuple((4, 5, 6))
print("tuple1:", type(tuple1), tuple1)
range1 = range(10)
print("range1:", type(range1),range1)
#Mapping (отображения): dict
dict1 = {"key1": "value1", "key2": "value2"}
dict2 = dict(key1 = "value1", key2 = "value2")
print("dict1:", type(dict1), dict1)
#Set (набор): set, frozenset
set1 = {1,2,3}
set2 = set((5, 4, 6))
print("set1:", type(set1), set1)
print("set2:", type(set2), set2)
frozenset1 = frozenset([1,2,3])
frozenset2 = frozenset((4,5,6))
print("frozenset1:", type(frozenset1), frozenset1)
print("frozenset2:", type(frozenset2), frozenset2)
#Boolean (логические): bool
bool1 = True
bool2 = bool(False)
print("bool1:", type(bool1), bool1)
print("bool2:", type(bool2), bool2)
#Binary (двоичные): bytes, bytearray, memoryview
bytes1 = b"Hi"
bytes2 = bytes(5)
print("bytes1:", type(bytes1), bytes1)
print("bytes2:", type(bytes2), bytes2)
bytearray1 = bytearray(5)
print("bytearray1:", type(bytearray1), bytearray1)
memoryview1 = memoryview(bytes(1))
print("memoryview1:", type(memoryview1), memoryview1)
#None: NoneType
nonetype1 = None
print("nonetype1:", type(nonetype1), nonetype1)

