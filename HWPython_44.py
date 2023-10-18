# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести его 
# в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# # data.head()

# one_hot_data = pd.get_dummies(data['whoAmI'])
# data = pd.concat([data, one_hot_data], axis=1)
# data.head()
# _____________________________________



# import random
 
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# print(data)
 
# # Добавляем временный столбец 'tmp' со значениями 1
# data['tmp'] = 1
# # Устанавливаем индекс по столбцам 'whoAmI' и 'tmp'
# data.set_index([data.index, 'whoAmI'], inplace=True)
# # Делаем распаковку столбца 'whoAmI' в новые столбцы
# data = data.unstack(level=-1, fill_value=0).astype(int)
# data.columns = data.columns.droplevel()
# data.columns.name = None
# print(data)
# __________________________________


import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = data['whoAmI'].str.get_dummies()

one_hot.head()