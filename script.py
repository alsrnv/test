
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генерация временного ряда
timestamps = pd.date_range(start='2021-01-01', end='2021-01-31', freq='D')
metric_values = np.random.poisson(lam=10, size=len(timestamps))
sensor_names = ['Sensor_1'] * len(timestamps)

# Создание DataFrame
df = pd.DataFrame({'timestamp': timestamps, 'metric_value': metric_values, 'sensor_name': sensor_names})

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['metric_value'], marker='o')
plt.title('Time Series of AI VR Calls')
plt.xlabel('Timestamp')
plt.ylabel('Metric Value')
plt.grid(True)
plt.show()
