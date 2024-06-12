import pandas as pd

data = {
    'Name': ['Анна', 'Марк', 'Александр', 'Сергей', 'Петр', 'Виктория', 'Антон', 'Николай', 'Алексей', 'Михаил'],
    'Математика': [5, 3, 4, 4, 5, 5, 3, 5, 4, 5],
    'Русский язык': [2, 3, 3, 5, 5, 5, 3, 5, 4, 5],
    'Физика': [4, 5, 4, 4, 5, 5, 3, 5, 4, 5],
    'Информатика': [5, 5, 3, 5, 5, 5, 3, 5, 4, 5],
    'Химия': [3, 3, 3, 5, 5, 5, 3, 5, 4, 5]
}

df = pd.DataFrame(data)

print(df.head(5))

mat_mean = df['Математика'].mean()
rus_mean = df['Русский язык'].mean()
fiz_mean = df['Физика'].mean()
inf_mean = df['Информатика'].mean()
him_mean = df['Химия'].mean()

mat_median = df['Математика'].median()
rus_median = df['Русский язык'].median()
fiz_median = df['Физика'].median()
inf_median = df['Информатика'].median()
him_median = df['Химия'].median()

print(f'Средние оценки: математика - ', {mat_mean}, 'русский язык - ', {rus_mean}, 'физика - ', {fiz_mean}, 'информатика - ', {inf_mean}, 'химия - ', {mat_mean})
print(f'Медиана оценок: математика - ', {mat_median}, 'русский язык - ', {rus_median}, 'физика - ', {fiz_median}, 'информатика - ', {inf_median}, 'химия - ', {him_median})

q1 = df['Математика'].quantile(0.25)
q3 = df['Математика'].quantile(0.75)
IQR = q3 - q1

print(f'Q1 по математике: ', {q1})
print(f'Q3 по математике: ', {q3})
print(f'IQR по математике: ', {IQR})

mat_std = df['Математика'].std()
rus_std = df['Русский язык'].std()
fiz_std = df['Физика'].std()
inf_std = df['Информатика'].std()
him_std = df['Химия'].std()

print(f'Стандартное отклонение: математика - ', {mat_std}, 'русский язык - ', {rus_std}, 'физика - ', {fiz_std}, 'информатика - ', {inf_std}, 'химия - ', {him_std})
