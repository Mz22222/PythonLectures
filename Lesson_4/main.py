

# def calc1(x):
#     return x + x

# def calc2(x):
#     return x * x

# def math(op, x): # op — операция, воспринимаем её как отдельную функцию
#     print(op(x))

# math(calc2, 10) # 100


# ///////////////////////////////////////////////////////


# # лямбда функция

# def calc1(x, y):
#     return x + y
# # ⇔ (равносильно)
# calc1 = lambda x, y: x + y



# ///////////////////////////////////////////////////////


# # ЗАДАЧА
# # В списке хранятся числа. Нужно выбрать только чётные числа и составить
# # список пар (число; квадрат числа).
# # Пример: 1 2 3 5 8 15 23 38
# # Получить: [(2, 4), (8, 64), (38, 1444)]

# # мой вариант:
# digit = [1, 2, 3, 5, 8, 15, 23, 38]

# def even_digit(digit):
#     res = []
#     for i in digit:
#         if i % 2 == 0:
#             res.append((i, i ** 2))
#     return res

# print(even_digit(digit))



# # варик из лекции:

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = list()

# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))

# print(out)

# # Как можно сделать этот код лучше, используя lambda?

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res) #[1, 2, 3, 5, 8, 15, 23, 38]

# res = where(lambda x: x % 2 == 0, res)
# print(res) # [2, 8, 38]

# res = list(select(lambda x: (x, x ** 2), res))
# print(res) # [(2, 4), (8, 64), (38, 1444)]



# # можно удалить select и везде, вместо этой функции написать map 
# # будет тоже самое 
# # просто select мы явно прописали, а map - это встроенная функция 

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# print(res)

# res = where(lambda x: x % 2 == 0, res)
# print(res)

# res = list(map(lambda x: (x, x ** 2), res))
# print(res)


# #  filter() позволит избавиться от функции where, 

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)




# # ///////////////////////////////////////////////////////

# # Функция map

# list_1 = [x for x in range (1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)


# Задача:
# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?


# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38'] 
# # строка.split() - убирает все пробелы и создаем список из значений строки


# data = list(map(int,input().split()))
# print(data)





# # //////////////////////////////////////////////////
# # функция zip
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# # Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]






# # функция enumerate (Функция enumerate() позволяет пронумеровать набор данных.)
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]














# # Примеры использования различных режимов в коде:
# режим а
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# data.close() — используется для закрытия файла, чтобы разорвать подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в существующий файл, а не перезапись файлов.


# # Ещё один способ записи данных в файл:
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')



# # Режим r (Чтение данных из файла) :
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# # Режим w
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

