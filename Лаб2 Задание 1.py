money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_spend = spend
savings = money_capital

while True:
    # бюджет текущего месяца: подушка + зарплата
    budget = savings + salary

    # если денег не хватает — выходим
    if current_spend > budget:
        break

    # оплачиваем расходы
    savings = budget - current_spend
    months += 1

    # рост расходов со следующего месяца
    current_spend *= (1 + increase)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
