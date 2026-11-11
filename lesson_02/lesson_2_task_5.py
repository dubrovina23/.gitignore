def month_to_season(month):
    # Проверяем диапазоны месяцев с помощью логики
    if month == 12 or month == 1 or month == 2:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


# Проверяем работу функции
print(month_to_season(2))  # Выведет: Зима
print(month_to_season(6))  # Выведет: Лето
