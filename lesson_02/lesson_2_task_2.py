# Функция проверки високосного года
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


# Выбираем любой год для проверки
current_year = 2024

# Вызываем функцию и сохраняем результат в переменную
result = is_year_leap(current_year)

# Выводим ответ в консоль по формату учителя через f-строку
print(f"год {current_year}: {result}")
