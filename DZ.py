import pandas as pd

# 1. Создаем DataFrame
data = {
    'Ученик': [f'Ученик{i}' for i in range(1, 11)],
    'Математика': [78, 92, 85, 67, 90, 74, 88, 79, 95, 82],
    'Физика':      [85, 87, 78, 90, 93, 76, 88, 81, 84, 89],
    'Химия':       [91, 83, 77, 80, 86, 79, 82, 88, 90, 85],
    'Биология':    [75, 80, 85, 82, 78, 90, 88, 84, 79, 83],
    'История':     [88, 76, 90, 85, 82, 79, 91, 87, 84, 80]
}
df = pd.DataFrame(data).set_index('Ученик')

# 2. Первые строки
print("Первые строки DataFrame:")
print(df.head())

# 3. Средняя оценка по предметам
mean_scores = df.mean()
print("\nСредние оценки по предметам:")
print(mean_scores)

# 4. Медианная оценка по предметам
median_scores = df.median()
print("\nМедианные оценки по предметам:")
print(median_scores)

# 5. Q1, Q3 и IQR для математики
q1_math = df['Математика'].quantile(0.25)
q3_math = df['Математика'].quantile(0.75)
iqr_math = q3_math - q1_math
print(f"\nQ1 (25%) для математики: {q1_math}")
print(f"Q3 (75%) для математики: {q3_math}")
print(f"IQR (Размах между Q3 и Q1) для математики: {iqr_math}")

# 6. Стандартное отклонение по предметам
std_scores = df.std()
print("\nСтандартное отклонение по предметам:")
print(std_scores)
