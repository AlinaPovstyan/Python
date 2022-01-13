#HW_1

#1) Создать переменную типа String
itsString = "First programming language"  #String - строка
print("String = ", itsString, type(itsString))

#2) Создать переменную типа Integer
itsInteger = 23                            #Integer - целые числа
print("Integer = ", itsInteger, type(itsInteger))

#3) Создать переменную типа Float
itsFloat = 23.5                            #Float - вещественные числа (с .)
print("Float = ", itsFloat, type(itsFloat))

#4) Создать переменную типа Bytes
itsBytes =b"abc"
print("Bytes = ", itsBytes, type(itsBytes))

#5) Создать переменную типа List
itsList = [1, 2, 3, 4]
print("List = ", itsList, type(itsList))

#6) Создать переменную типа Tuple
itsTuple = tuple("Python")
print("Tuple = ", itsTuple, type(itsTuple))

#7) Создать переменную типа Set
itsSet = {6, 3, 6, 5, 5}                   #Set - уникальность элементов
print("Set = ", itsSet, type(itsSet))

#8) Создать переменную типа Frozen set
itsFrozen_set = frozenset([1, 2, 5, 2, 6, 1])
print("Frozen_set = ", itsFrozen_set, type(itsFrozen_set))

#9) Создать переменную типа Dict
itsDict = dict(dog="barba", cat="ymi")     #Dict - словарь
print("Dict = ", itsDict, type(itsDict))

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
#Указаны сразу в пунктах 1-10.

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
itsString_breed = "dalmatian"
itsString_dog_name = "barba"
itsString_dog = itsString_breed + " " + itsString_dog_name
print("Dog = ", itsString_dog)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(itsString_breed, itsInteger)

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(itsString_breed + " " + str(itsInteger))
