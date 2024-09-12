import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.ensemble import GradientBoostingRegressor

def forecast_sales(trained_models, method, current_data, date_until, granularity='D'):
    """
    Строит численный прогноз продаж до заданной даты с помощью уже обученной модели.

    :param trained_models: Словарь обученных моделей.
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

    elif method in trained_models:
        future_X = np.arange(len(current_data), len(current_data) + forecast_length).reshape(-1, 1)
        predictions = trained_models[method].predict(future_X)

    forecast_series = pd.Series(predictions, index=index)
    return forecast_series



# Словарь моделей
trained_models = {
    'Exponential Smoothing': exp_model,
    'Boosting': b_model
}

selected_method = 'Exponential Smoothing'
date_until = '2024-01-15'

forecast = forecast_sales(trained_models, selected_method, current_data, date_until)
print(f"Прогноз продаж для метода {selected_method}:\n{forecast}")
