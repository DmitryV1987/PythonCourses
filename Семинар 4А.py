import random

# ввод степени многочлена
k = int(input("Enter the degree of the polynomial: "))

# коэффициенты
coefficients = []

# генерируем случайное значение коэффициентов от -100 до 100
for i in range(k+1):
    coefficients.append(random.randint(-100, 100))

# создаем многочлен
polynomial = ""
for i in range(k,+1,-1):
    if i == k:
        polynomial += str(coefficients[i])
    else:
        polynomial += "+" + str(coefficients[i]) + "*x^" + str(i)

polynomial += "=0"

# записываем его в файл
with open("polynom.txt", "w") as f:
    f.write(polynomial)