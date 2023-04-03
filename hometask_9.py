# Урок 9. Работа с табличными данными

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')
df[df['population']<=500].mean()['median_house_value']
# 206799.95140186916

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
df[df['population']==df['population'].min()]['households'].max()