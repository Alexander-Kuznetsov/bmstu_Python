#Задача номер 2.62 выполнил: Кузнецов Александр ИУ7-13
from math import *
N = int(input("Введите длину массива: "))
if (1<=abs(N)<=25):
    Z=[0]*N
    print("Задайте массив")
    #задается массив
    Z=[float(input()) for i in range(N)]
    print(Z)
    W = float(input("Введите действительное число W = "))
    for i in range(len(Z)):
        #Вставка W в массив
        if (i==len(Z)-1) and (W<=Z[i]):
         Z.append(W)
         print(Z)
         break
        if W>=Z[i]:
         Z.insert(i,W)
         print(Z)
         break
else: print("Введена неверная длина")
