import random

numbers = [random.randint(1, 100) for _ in range(10)]

sorted_numbers = sorted(numbers)

print("Начальный список:", numbers)
print("Готовый список:", sorted_numbers)