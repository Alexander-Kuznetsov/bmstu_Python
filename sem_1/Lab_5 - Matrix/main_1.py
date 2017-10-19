#Лабараторная работа "выполнить разворот матрицы на 180гр влево
#Кузнецов ИУ7-13
from math import *
L = int(input("Введите размер матрицы: "))
R=[]
if(L<=7)and(L>=2):
 print("Введите элементы массива по 1му в строке: ")
 for i in range(L):
    R.append([]) 
    for j in range(L):
        R[i].append(int(input()))
 print("Исходная матрица: ")
 for i in range(L):
    print(R[i])
 R.reverse()
 print("Результат работы программы: ")
 for i in range(L):
  R[i].reverse()
  print(R[i])
else: print("Введены данные несоответствующие условию задачи")
