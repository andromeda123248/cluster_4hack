import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.ensemble import GradientBoostingRegressor

def mean_absolute_percentage_error(y_true, y_pred): 
    """
    Рассчитывает среднее абсолютное процентное отклонение (MAPE).
    """
    y_true, y_pred = pd.Series(y_true), pd.Series(y_pred)
    return ((y_true - y_pred).abs() / y_true.abs()).mean() * 100

def calculate_metrics(true_values, predictions_dict):
    """
    Рассчитывает метрики прогнозов для нескольких методов.

    :param true_values: Список (или массив) истинных значений.
    :param predictions_dict: Словарь, где ключи - названия методов, значения - списки (или массивы) прогнозов.
    :return: DataFrame с метриками для каждого метода.
    """
    metrics_data = []

    for method, predictions in predictions_dict.items():
        rmse = mean_squared_error(true_values, predictions, squared=False)
        mae = mean_absolute_error(true_values, predictions)
        mape = mean_absolute_percentage_error(true_values, predictions)
        r2 = r2_score(true_values, predictions)
        
        metrics_data.append({
            'Method': method,
            'RMSE': rmse,
            'MAE': mae,
            'MAPE': mape,
            'R2': r2
        })
        
    return pd.DataFrame(metrics_data)

# Собираем прогнозы
predictions_dict = {
    'Constant': constant_prediction,
    'Exponential Smoothing': exp_predictions,
    'Boosting': gb_predictions
}

metrics_df = calculate_metrics(true_values, predictions_dict)
print(metrics_df)
