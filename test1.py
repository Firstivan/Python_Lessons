# a = 123
# b = 1.23
# print(a)
# print(b)
# _____________________

# value = None
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 1234
# print(value)
# ________________


# s = 'hello,' # создание 1-ой строки
# w = "world" # создание 2-ой строки
# print(s, w)
# _________________


# print(1)
# —------------------
'''print(1)
print(1)
print(1)
print(1)
print(1)'''
# ______________


# s = 'hello "world"'
# print (s)
# s = "hello 'world'"
# print (s)
# s = 'hello \"world'
# print (s)
# __________________


# a = 3
# b = 11
# s = 2022
# print(a, b, s)
# print(a,'-', b,'-', s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'first - {a} second - {b} third - {s}')
# ______________________________


# n = 1.345
# print(int(n))
# _____________


# m = '345'
# print(m * 2) # При умножении строки на число, она повторяется столько раз на какое была умножена
# print(int(m) * 2)
# ________________


# n = 1.345
# print(str(n) * 2) #str() - функция, которая позволяет перевести из любого типа данных в строку(если это возможно)
# __________________


# n = '1.345'
# print(float(n) * 2) #float() - функция, которая позволяет перевести из любого типа данных в вещественный(если это возможно)

# m = 2
# print(float(m))
# _____________________


# n = int(input()) # ввод числа с экрана (5)
# print(n * 2) # 10
# _________________________-


# Приоритет арифметических операций
# 1. Возведение в степень (**)
# 2. Умножение (*)
# 3. Деление (/)
# 4. Целочисленное деление (//)
# 5. Остаток от деления (%)
# 6. Сложение (+)
# 7. Вычитание (-)


# a = 1.43425
# b = 2.2983
# c = round(a * b, 5) # Можно указать количество знаков после запятой
# ______________________


# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5
# __________________________


# a = 1 > 4
# print(a) # False


# a = 1 < 4 and 5 > 2
# print(a) # True


# a = 1 == 2
# print(a) # False


# a = 1 != 2
# print(a) # True


# a = 'qwe'
# b = 'qwe'
# print(a == b) # True


# a = 1 < 3 < 5 < 10
# print (a) # True
# __________________________


# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)
# __________________


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)
# ___________________


# n = int(input('Веедите число '))
# if n % 2 == 0 and n % 3 == 0:
#     print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
#     print('Число кратно 15')
# _____________________


# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9
# ___________________


# i = 0
# while i < 5:
#     if i == 3:
#       break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)
# _______________


# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)
# _________________


# n = int(input('введите число у которого требуется найти минимальный делитель: '))
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1
# ____________________


# for i in 1, -2, 3, 14, 5:
# print(i)
# __________________



# Range
# ● Range выдает значения из диапазона с шагом 1.
# ● Если указано только одно число — от 0 до заданного числа.
# ● Если нужен другой шаг, третьим аргументов можно задать приращение

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
# print(i)    # 100 80 60 40 20
# _____________________


# for i in range(5):
#     print(i)    # в столбец будут цифры: 0 1 2 3 4
# ___________________-


# for i in 'qwerty':
#     print(i)    # в столбец будут буквы
# ______________________


# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
# 


# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # Определить количество символов в строке:39
# print('ещё' in text) # Проверить наличие символа в строке (in): True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# rint(text.replace('ещё','ЕЩЁ')) # Заменить слово на другое
# _______________________


text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...