#HW_1

#1) Создать переменную типа String
String = "First programming language"  #String - строка
print("String = ", String, type(String))

#2) Создать переменную типа Integer
Integer = 23                            #Integer - целые числа
print("Integer = ", Integer, type(Integer))

#3) Создать переменную типа Float
Float = 23.5                            #Float - вещественные числа (с .)
print("Float = ", Float, type(Float))

#4) Создать переменную типа Bytes
Bytes =b"abc"
print("Bytes = ", Bytes, type(Bytes))

#5) Создать переменную типа List
List = [1, 2, 3, 4]
print("List = ", List, type(List))

#6) Создать переменную типа Tuple
Tuple = tuple("Python")
print("Tuple = ", Tuple, type(Tuple))

#7) Создать переменную типа Set
Set = {6, 3, 6, 5, 5}                   #Set - уникальность элементов
print("Set = ", Set, type(Set))

#8) Создать переменную типа Frozen set
Frozen_set = frozenset([1, 2, 5, 2, 6, 1])
print("Frozen_set = ", Frozen_set, type(Frozen_set))

#9) Создать переменную типа Dict
Dict = dict(dog="barba", cat="ymi")     #Dict - словарь
print("Dict = ", Dict, type(Dict))

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
#Указаны сразу в пунктах 1-10.

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
String_breed = "dalmatian"
String_dog_name = "barba"
String_dog = String_breed + " " + String_dog_name
print("Dog = ", String_dog)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(String_breed, Integer)

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(String_breed + " " + str(Integer))
