def get_predictions_for_method(predictions_dict, selected_method):
    """
    Возвращает предсказания для выбранного метода.
    
    :param predictions_dict: Словарь, где ключи - названия методов, значения - прогнозы.
    :param selected_method: Имя выбранного метода.
    :return: Прогнозы выбранного метода.
    """
    if selected_method in predictions_dict:
        return predictions_dict[selected_method]
    else:
        raise ValueError(f"Метод '{selected_method}' не найден. Доступные методы: {list(predictions_dict.keys())}")

# Пример использования
selected_method = 'Exponential Smoothing'  # Пользовательский выбор
selected_predictions = get_predictions_for_method(predictions_dict, selected_method)
print(f"Прогнозы для метода {selected_method}: {selected_predictions}")
