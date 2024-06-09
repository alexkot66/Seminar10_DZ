# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)

# 1. Перевод в one hot вид с помощью get_dummies()
# data1 = data['whoAmI'].str.get_dummies()
# print(data1)

# 2. Перевод в one hot вид с помощью цикла и если заранее известны значения внутри столбца
# data['whoAmI_human'] = [1 if item == 'human' else 0 for item in data['whoAmI']]
# data['whoAmI_robot'] = [1 if item == 'robot' else 0 for item in data['whoAmI']]
# data.drop(['whoAmI'], axis=1, inplace=True)
# print(data)

# 3. Перевод в one hot вид с помощью поиска значений внутри столбца и цикла для перевода 
list1_str = data['whoAmI'].to_list() #список строк значений в столбце
set_str = set(list1_str) #сделал множество строк для того, чтобы убрать повтор
list2 = list(set_str) #сделал обратно список строк, так как множество не индексируемо
for elem in list2:
    data[elem] = [1 if item == elem else 0 for item in data['whoAmI']]
# прошел циклом по списку строк, чтобы проверить вхождения, создавая новый столбец и кладем в ячейку 1 если значение есть
# 0 если значение отсутствует.
data.drop(['whoAmI'], axis=1, inplace=True) # убираю первую строку, исходя из примера и результатов работы метода get_dummies()
print(data)
