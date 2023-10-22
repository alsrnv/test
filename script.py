import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Предположим, что df - это ваш исходный DataFrame с колонками 'timestamp', 'metric_value', и 'sensor_name'

# Указываем имя датчика, который хотим тестировать
test_sensor_name = 'Sensor_1'

# Шаг 1: Фильтрация данных для выбранного sensor_name
df_sensor = df[df['sensor_name'] == test_sensor_name]

# Шаг 2: Визуализация распределения данных
plt.hist(df_sensor['metric_value'], bins=20, density=True)
plt.title('Histogram of Metric Values')
plt.xlabel('Metric Value')
plt.ylabel('Frequency')
plt.show()

# Шаг 3: Хи-квадрат тест
observed_values = df_sensor['metric_value'].value_counts().sort_index().values
mean_value = np.mean(df_sensor['metric_value'])

# Убедимся, что размеры массивов совпадают
unique_values = df_sensor['metric_value'].unique()
expected_values = [np.exp(-mean_value) * mean_value**x / np.math.factorial(x) * len(df_sensor) for x in unique_values]

if len(observed_values) == len(expected_values):
    chi2_stat, p_value = chisquare(f_obs=observed_values, f_exp=expected_values)
    if p_value > 0.05:
        print('The distribution seems to follow the expected distribution.')
    else:
        print('The distribution does not seem to follow the expected distribution.')
else:
    print(f"The lengths of observed and expected values do not match. Observed: {len(observed_values)}, Expected: {len(expected_values)}. Cannot perform chi-square test.")
