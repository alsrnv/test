from scipy.stats import chisquare, poisson, norm

def analyze_sensors(df):
    results = {}
    sensor_names = df['sensor_name'].unique()
    
    for sensor in sensor_names:
        df_sensor = df[df['sensor_name'] == sensor]
        mean_value = np.mean(df_sensor['metric_value'])
        std_value = np.std(df_sensor['metric_value'])
        
        # Проверка распределения Пуассона
        observed_values = df_sensor['metric_value'].value_counts().sort_index()
        unique_values = observed_values.index
        expected_poisson = [poisson.pmf(int(x), mean_value) * len(df_sensor) for x in unique_values]
        
        # Нормализация ожидаемых и наблюдаемых значений
        sum_observed = np.sum(observed_values)
        sum_expected_poisson = np.sum(expected_poisson)
        observed_values = observed_values * (sum_expected_poisson / sum_observed)
        
        chi2_poisson, p_poisson = chisquare(f_obs=observed_values, f_exp=expected_poisson)
        
        # Проверка нормального распределения
        expected_norm = [norm.pdf(x, mean_value, std_value) * len(df_sensor) for x in unique_values]
        
        # Нормализация ожидаемых значений
        sum_expected_norm = np.sum(expected_norm)
        expected_norm = expected_norm * (sum_observed / sum_expected_norm)
        
        chi2_norm, p_norm = chisquare(f_obs=observed_values, f_exp=expected_norm)
        
        # Определение типа распределения
        distribution = "Unknown"
        if p_poisson > 0.05:
            distribution = "Poisson"
        elif p_norm > 0.05:
            distribution = "Gaussian"
        
        # Проверка на аномалии (здесь используется простой Z-тест)
        z_scores = np.abs((df_sensor['metric_value'] - mean_value) / std_value)
        anomalies = np.where(z_scores > 2)[0]
        
        results[sensor] = {
            'Distribution': distribution,
            'Anomalies': len(anomalies) > 0
        }
        
    return results

# Предположим, что df - это ваш DataFrame
# df = ...

# Применение функции
results = analyze_sensors(df)
print(results)
