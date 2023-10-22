import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

# Предположим, что df - это ваш исходный DataFrame с колонками 'timestamp', 'metric_value', и 'sensor_name'

# Шаг 1: Фильтрация данных для одного из sensor_name, например, 'Sensor_1'
df_sensor = df[df['sensor_name'] == 'Sensor_1']

# Шаг 2: Подготовка данных для Prophet
df_prophet = df_sensor.rename(columns={'timestamp': 'ds', 'metric_value': 'y'})

# Шаг 3: Инициализация и обучение модели
model = Prophet()
model.fit(df_prophet)

# Шаг 4: Прогнозирование
future = model.make_future_dataframe(periods=0)
forecast = model.predict(future)

# Определение выбросов
forecast['anomaly'] = 0
forecast.loc[forecast['yhat_lower'] > df_prophet['y'].reset_index(drop=True), 'anomaly'] = -1  # Ниже нижнего предела
forecast.loc[forecast['yhat_upper'] < df_prophet['y'].reset_index(drop=True), 'anomaly'] = 1   # Выше верхнего предела

# Визуализация результатов
fig = model.plot(forecast)
plt.title('Time Series with Anomalies')
plt.show()
