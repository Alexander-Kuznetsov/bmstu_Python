# Вариант 9
N = int(input("Введите длину массива: "))
if (N <= 35 and N >= 0):
 Y = [0]*N
 Y = [float(input()) for i in range(len(Y))]
 print("Исходный массив", Y)
 for i in range(len(Y)):
    if i%2 == 0:
       Y.append(Y[i])
       Y[i] = "0"
 c = Y.count("0")
 for i in range(c):
     Y.remove("0")
 print("Результат: ", Y)
else: print("Длина массива задана не по усл.")
