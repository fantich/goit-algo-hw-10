import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Total_Production", pulp.LpMaximize)

# Змінні
L = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
F = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Цільова функція
model += L + F, "Total_Products"

# Обмеження
model += 2 * L + 1 * F <= 100   # Вода
model += 1 * L <= 50            # Цукор
model += 1 * L <= 30            # Лимонний сік
model += 2 * F <= 40            # Фруктове пюре

# Розв'язання моделі
model.solve()

# Результати
print("Лимонад:", L.varValue)
print("Фруктовий сік:", F.varValue)
print("Загальна кількість напоїв:", pulp.value(model.objective))