# Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
 
# Найдите количество и выведите его.

# count = 0 
# for item in list_1: 
#     if item == k: 
#         count += 1 
# print(count)
# _______________________________

# list_1 = [1, 2, 3, 4, 5]
# k = 2
# count = 0
# for num in list_1:
#     if num == k:
#         count += 1
# print(count)
# ____________________________________


# def count_occurrences(numbers, k):
#     count = 0
#     for num in numbers:
#         if num == k:
#             count += 1
#     return count

# # Пример использования функции
# numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# k = 3
# occurrences = count_occurrences(numbers, k)
# print(f"Число {k} встречается {occurrences} раз(а) в списке {numbers}")
# ___________________________________


# import random
# N = int(input('Введите размер массива N: '))
# X = int(input('Введите число X: '))
# N_array = []
# for i in range(N):
#     N_array.append(random.randint(0, N//2))
# print(f'Число вхождений посчитали с помощью встроенной функции count {N_array.count(X)}')
# print('Некорректный ввод. Попробуйте еще раз!')
# ________________________________________


# n = int(input('Введите кол-во элементов списка: '))
# array = [int(i) for i in input('Введите значение массива: ').split()]
# k = int (input('Введите число х: '))
# count = 0
# for element in array:
#     if element == k:
#         count += 1
# print(count)
# ____________________________________________


# import random
# quantity = int(input('Введите количество элементов массива: '))
# array = [random.randint(0, 9) for i in range(quantity)]
# print(array, end = " ")
# element = int(input(f'\nВведите число X: '))
# print(f'Количество {element} в массиве - {array.count(element)}')
# ______________________________
# __________________________________



# Задача 18
# Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# import random
# quantity = int(input('Введите количество элементов массива: '))
# array = [random.randint(0, 9) for i in range(quantity)]
# print(array, end = " ")
# element = int(input(f'\nВведите число X: '))
# minimal = near = 10
# for i in range(0, len(array)):
#   diff = abs(element - array[i])
#   if diff < minimal:
#     minimal = diff
#     near = array[i]
# print(f'Ближайшее по значению число - {near}')
# ____________________________________


# N = abs(int(input('Введите количество элементов списка А: ')))
# A_entered = input("Введите через пробел элементы списка: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N or N == 0:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
#     min = abs(X - A_num[0])
#     index = 0
#     for i in range(1, N):
#         count = abs(X - A_num[i])
#         if count < min:
#             min = count
#             index = i
#     print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')
# ________________________________________

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# def find_closest_number(list_1, k):
#     closest_num = list_1[0]
#     for num in list_1:
#         if abs(num - k) < abs(closest_num - k):
#             closest_num = num
#     return closest_num
# closest_num = find_closest_number(list_1, k)
# print(closest_num)
# _____________________



# list_1 = [1, 2, 3, 4, 5]
# k = 6

# def closest_number(list_1, k):
#     closest_number = None
#     for number in list_1:
#         if closest_number is None or abs(number - k) < abs(closest_number - k):
#             closest_number = number
#     return closest_number

# closest_number_to_k = closest_number(list_1, k)
# print(closest_number_to_k)
# _______________________________________


#Задача 20: 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}

# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for k, v in list_letters.items():
#         if i in v:
#             summ += k
# print(f"Стоимость слова: {summ}")
# _______________________________________



# dict_with_letter = {1: "AEIOULNSTRАВЕИНОРСТ",
#                     2:"DGДКЛМПУ",
#                     3:"BCMPБГЁЬЯ",
#                     4:"FHVWYЙЫ",
#                     5:"KЖЗХЦЧ",
#                     8:"JXШЭЮ",
#                     10:"QZФЩЪ"} 
 
# def dicting(dict_with_letter, words): 
#  sum_points = 0 
#  for key, value in dict_with_letter.items(): 
#   for letter in words.upper(): 
#    if letter in value: 
#     sum_points += key 
#  print(sum_points) 
# k = str(input()) 
# dicting(dict_with_letter,k)
# _____________________________________


# scrab = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1', 'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1',
#          'D': '2', 'G': '2', 'Д': '2', 'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2',
#          'B': '3', 'C': '3', 'M': '3', 'P': '3', 'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3',
#          'F': '4', 'H': '4', 'V': '4', 'W': '4', 'Y': '4', 'Й': '4', 'Ы': '4',
#          'K': '5', 'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5',
#          'J': '8', 'X': '8', 'Ш': '8', 'Э': '8', 'Ю': '8',
#          'Q': '10', 'Z': '10', 'Ф': '10', 'Щ': '10', 'Ъ': '10'}

# k = str(input()).upper()

# summary = 0
# for char in k:
#   summary += int(scrab[char])

# print(summary)
# ___________________________________


scrab_russian = {
    1: "AEIOULNSTRАВЕИНОРСТ",
    2: "DGДКЛМПУ",
    3: "BCMPБГЁЬЯ",
    4: "FHVWYЙЫ",
    5: "KЖЗХЦЧ",
    8: "JXШЭЮ",
    10: "QZФЩЪ"
}

# Получаем слово от пользователя и переводим его в верхний регистр
k = input("Введите слово: ").upper()

# Инициализируем переменную для суммирования стоимости слова
summary = 0

# Проходим по каждой букве в слове и суммируем стоимость
for char in k:
    for value, letters in scrab_russian.items():
        if char in letters:
            summary += value
            break  # Прерываем внутренний цикл после нахождения соответствующей буквы

# Выводим результат
print(summary)