#  СПИСКИ

# list_1 = [] # создали пустой список

# list_1 = list() # создали функцию list, которая также будет создавать пустой список 

# list_1 = [1, 2, 3, 8]
# print(*list_1) # чтобы [] и , не выводились, нужно написать * перед названием переменной (будет просто перечисление каких-то значений)

# for i in list_1: 
#     print(i)  # вывод с помощью цикла 

# print(len(list_1)) # длина списка

# print(list_1[0]) # обращение к 1-му элементу 
# print(list_1[-1]) # индексация начинается с конца

# # добавление значений в список
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)


# # мини-код в котором мы поочередно добавляем какие-то значения с помощью цикла for 
# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)




# # основные функции, которые могут быть в списках

# # удаление последнего элемента списка 
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1 ]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7 ]


# #  удаление конкретного элемента из списка 
# list_1 =  [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [ 7, -1, 21, 0]


# #  добавление элемента на нужную позицию 
# list_1 =  [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) 
# print(list_1) #  [12, 7, 11, -1, 21, 0]





# #  работа со срезами 
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) # [9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1,7]
# print(list_1[::6]) # [1,7]








# #  КОРТЕЖИ 

# t = ()
# print(type(t))  

# t = (1, 5, 3,) # добавим какое-то значение
# print(type(t)) # чтобы он выводил тип данных кортеж, в конце нужно поставить запятую 



# v = [1, 8, 9]
# print(v)
# print(type(v))
# # преобразуем в кортеж
# v = tuple(v)
# print(v)
# print(type(v))



# # присвоение переменных
# a = 1
# b = 2
# # или можно так 
# a,b = 1,3 # множественное присванивание 

# # поделим наш кортеж на 3 переменные 
# a,b,c = v
# print (a, b, c)


# # отличие кортежа от списка 
# # сходства 

# t = (1, 2, 3, 5, )

# for i in range(len(t)): 
#     print(t[i])

# # или 

# for i in t: 
#     print(i)


# t[0] = 2 # так делать нельзя т.к. кортеж не поддежривает преобразование элемента
# #  если же там будет список вместо кортежа, то все будет работать








# # СЛОВАРИ
# d = {} # создали пустой словарь
# d=dict() # это тоже значит создание словаря

# # добавление значение 
# d['q'] = 'qwerty' # q - ключ 
# print(d)

# d['w'] = 'werty' # q - ключ 
# print(d)

# # вывод значения с помощью ключа
# print(d['q'])


# # небольшой пример 
# dictionary = {}
# dictionary = {'up': '⬆', 'left': '←', 'down': '⬇', 'right': '⭢'}

# print(dictionary) # ['up':'t', left':'+', down': 't', 'right':'→)
# print (dictionary['left']) # ←
# # типы ключей могут отличаться
# print (dictionary ['up']) # ⬆
# # типы ключей могут отличаться
# dictionary['left'] = '←'
# print(dictionary['left']) # ←
# # print(dictionary['type']) # KeyError: 'type'

# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ⬆
# # down: ⬇
# # right: ⭢


# dictionary[895] = 98998
# print(dictionary)







# # МНОЖЕСТВА

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}

# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}

# colors.remove('red') # удалить red
# print(colors) # {'green', 'blue','gray'}

# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok # сначала проверяет есть ли этот цвет, если есть - удаляет, если нет, просто пропускает
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }  # удаление всех элементов
# print(colors) # set()

# q = set()




# # Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}  - скопировали  элементы из мн-ва а в мн-во с
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} - объединение
# i = a.intersection(b) # i = {8, 2, 5} - пересечние
# dl = a.difference(b) # dl = {1, 3} - разность (a - b)
# dr = b.difference(a) # dr = {13, 21} - разность (b-a)
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} - сначала находим пересечение a и b, далее а объединяем с b и находим разность 




# #  неизменяемые или замороженные
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})



# # List Comprehension

# # 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# # 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]


# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так с помощью генератора списков:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]


# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
