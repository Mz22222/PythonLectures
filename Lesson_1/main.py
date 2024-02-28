"""
#присовоение переменных 
n = none #если пустое значение

n = 1.66
print(n)

n = 'priv'
print(n)
"""


# # узнать тип данных с помощью вывода
# n = 5 
# print(type(n))

# n = 'priiiv\'kiiiiiiiii' # если хотим вывести кавычку, то используем слеш
# print(n)



# a = 5
# b = 5.89
# c = 'helloooo'

# # print(f"{a} - {b} - {c}") # интерполяция 
# print ("{} - {} - {}".format(a, b, c)) 


# # ввод данных с клавиатуры
# print('Введите первое число: ')  # ввод с новой строки 
# a = input()

# b = input('Введите второе число: ') # ввод на этой же строке




# # приведение типов 

# с = 5.89
# print(с)
# print(type(с))

# с = int(с)
# print(с)
# print(type(с))

# с = str(с)
# print(с + '67')
# print(type(с))

# # также можем привести к типу bool 
# с = 1
# print(с)
# print(type(с))

# с = bool(с)
# print(с)
# print(type(с))


# # сложение чисел 
# a = int(input('Введите первое число: ')) 

# b = int(input('Введите второе число: ')) 

# print(a, '+', b, '=', a + b)


# # округление чисел 
# a = 5.899576
# b=6.5546865465
# print(round(a*b,4)) # первые аргумент - само число, второй - сколько цифр после запятой оставлять


# #+1 как в С# i++
# iter = 2
# iter += 2 # iter = iter + 2
# iter -= 2 # iter = iter - 2
# iter *= 2 # iter = iter * 2
# iter /= 2 # iter = iter / 2
# iter //= 2 # iter = iter // 2
# iter %= 2 # iter = iter % 2
# iter **= 2 # iter = iter ** 2


# # логические операции 

# a = 1 > 4 
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2 
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b='qwe'
# print(a==b)

# a = 1 < 3 < 5 < 10
# print(a)




# # условия 
# username = input('Введите имя: ')
# if username == 'Маша':
#     print ('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else: 
#     print('Привет, ', username)




#  # цикл while 
# n = 423
# summa = 0 
# while n > 0: 
#     x = n % 10 
#     summa +=x
#     n //=10
# print(summa)




# # цикл while - else 
# i = 0 
# while i < 5: 
#     # if i == 3:
#     #     break 
#     i = i + 1

# else: 
#     print('Пожалуй')
#     print('хватит')
# print(i)





# # метод флажка (нахождение минимального делителя)
# print('Введите число: ')
# n = int(input())
# flag = True 
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False 
#     i +=1





# # цикл for 
# a = 'qwerty'

# print(a[2]) # нам нужна е, нумерация начинается с 0, поэтому индекс буквы е это 2


# a = 'qwerty'

# for i in a: 
#     print(i)




# # вложенный цикл 
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)





# # строки 
# text = 'СЪЕШЬ ещё ЭТИХ мягких французских булок'
# print(len(text)) # позволяет узнать размер нашей строки 

# print ('ещё' in text) # позволяет узнать есть ли данной слово в нашей строке 

# print(text.lower()) # нижний регистр 

# print(text.upper()) # верхний регистр

# print(text.replace('ещё','ЕЩЁ')) # меняет сочетание символов в нашей строке (какое слово меняем на какое)






# срезы 

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # (выводится всё) съешь ещё этих мягких французских булок
print(text[:2]) # (первые 2 элемента) съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[15:]) # (с 15 и до конца) ешь ещё

print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл

text = text[2:9] + text[-5] + text[:2] # ...
print(text)

print(text[-1]) # индексация начинается с конца


