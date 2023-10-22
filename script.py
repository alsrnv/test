# Генерация временного ряда для нескольких датчиков
sensor_names = ['Sensor_1', 'Sensor_2', 'Sensor_3']
timestamps = pd.date_range(start='2021-01-01', end='2021-01-31', freq='D')
data = []

for sensor in sensor_names:
    metric_values = np.random.poisson(lam=10, size=len(timestamps))
    for t, value in zip(timestamps, metric_values):
        data.append([t, value, sensor])

# Создание DataFrame
df = pd.DataFrame(data, columns=['timestamp', 'metric_value', 'sensor_name'])

# Построение графика с использованием Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x='timestamp', y='metric_value', hue='sensor_name', data=df, marker='o')
plt.title('Time Series of AI VR Calls')
plt.xlabel('Timestamp')
plt.ylabel('Metric Value')
plt.grid(True)
plt.legend(title='Sensor Name')
plt.show()
