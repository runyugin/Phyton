# Урок 10. Построение графиков
# Задание 44

# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
data = pd.DataFrame(lst, columns={'whoAmI'})
data.head()

# whoAmI
# 0	human
# 1	human
# 2	robot
# 3	human
# 4	human

data = pd.DataFrame(random.sample(['robot', 'human'] * 10, 20) ,columns={'whoAmI'})
data.head()

# whoAmI
# 0	robot
# 1	human
# 2	human
# 3	human
# 4	robot