# Считываем количество записей, которые нужно обработать
n = int(input())

# Список для хранения максимальных значений
max_values = []

# Обрабатываем каждую запись
for _ in range(n):
    measurements = list(map(int, input().split()))
    max_value = max(measurements)
    max_values.append(max_value)

# Сортируем максимальные значения по убыванию
max_values.sort(reverse=True)

# Выводим отсортированный список максимальных значений, разделенный символом ";"
print(";".join(map(str, max_values)))