# читаем первый многочлен из первого текстового файла
with open("file1.txt", "r") as f:
    poly1 = f.read()

# читаем второй многочлен из второго текстового файла
with open("file2.txt", "r") as f:
    poly2 = f.read()

# делаем их сумму
sum = poly1 + "+" + poly2

# записываем итог в файл sum.txt
with open("sum.txt", "w") as f:
    f.write(sum)