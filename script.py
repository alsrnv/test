import matplotlib.pyplot as plt
import seaborn as sns

# Построение графика с использованием Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x='timestamp', y='metric_value', hue='sensor_name', data=df, marker='o')
plt.title('Time Series of AI VR Calls')
plt.xlabel('Timestamp')
plt.ylabel('Metric Value')
plt.grid(True)
plt.legend(title='Sensor Name')
plt.show()
