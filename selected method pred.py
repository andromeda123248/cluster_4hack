import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

def forecast_sales(method, current_data, date_until, granularity='D'):
    """
    Строит численный прогноз продаж до заданной даты.

    :param method: Метод, используемый для прогнозирования ('Constant', 'Exponential Smoothing', 'Gradient Boosting').
    :param current_data: Исходные данные о продажах.
    :param date_until: Дата (в виде строки 'YYYY-MM-DD') до которой нужен прогноз.
    :param granularity: Гранулярность прогноза (например, 'D' - ежедневно).
    :return: Прогноз продаж до заданной даты.
    """
    index = pd.date_range(start=current_data.index[-1] + pd.Timedelta(days=1), end=date_until, freq=granularity)
    forecast_length = len(index)

    if method == 'Constant':
        predictions = [current_data.iloc[-1]] * forecast_length

    elif method == 'Exponential Smoothing':
        model = ExponentialSmoothing(current_data, trend='add', seasonal=None)
        fit = model.fit()
        predictions = fit.forecast(forecast_length)

    elif method == 'Gradient Boosting':
        X = np.arange(len(current_data)).reshape(-1, 1)
        y = current_data.values
        model = GradientBoostingRegressor()
        model.fit(X, y)

        future_X = np.arange(len(current_data), len(current_data) + forecast_length).reshape(-1, 1)
        predictions = model.predict(future_X)

    forecast_series = pd.Series(predictions, index=index)
    return forecast_series

# Пример использования
# Предположим у вас есть текущие данные о продажах в виде временного ряда
current_data = pd.Series(
    [100, 102, 104, 107, 110, 115, 120], 
    index=pd.date_range(start='2024-01-01', periods=7, freq='D')
)

selected_method = 'Exponential Smoothing'
date_until = '2024-01-15'

forecast = forecast_sales(selected_method, current_data, date_until)
print(f"Прогноз продаж для метода {selected_method}:\n{forecast}")
