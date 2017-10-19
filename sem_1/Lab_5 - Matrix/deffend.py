from math import *
print("Ввод данных:")
N = int(input("Введите длину строки матрицы: "))
K = int(input("Введите длину столбца матрицы: "))
eps = float(input("Введите эпселон: "))
a = float(input("Введите число a: "))
A=[]
n = 0
t = 0

if(N<=15)and(N>=2) and (K<=10) and (K>=2):
 print("Введите элементы матрицы по 1му в строке: ")
 for i in range(K):
    A.append([]) 
    for j in range(N):
        A[i].append(float(input()))
 print("Результат работы программы: ")
 while abs(tek)>=abs(eps):
     m = 2*n+1
     tek=(a**m)/factorial(m)
     t+=tek
     m=0
     tek=0
     n+=1
 u=0
 for i in range(K):
     for j in range(N):
         if A[i][j]>t:
             u+=1
 X=[0]*u
 p=0
 for i in range(K):
     for j in range(N):
         if A[i][j] > t:
             X[p]=A[i][j]
             p+=1
 d=0
 maxim = max(X)
 for i in range(len(X)):
     if X[i] == maxim:
         d=i
         break
 X[0],X[d]=X[d],X[0]
 print("Сумма бесконечного ряда (t): ","{:0.5}".format(t))
 print("Исходная матрица (Z): ")
 for i in range(K):
    for j in range(N):
        print("{:6}".format(A[i][j]),end=" ")
    print()
 print("Вектор (X): ",X)
else: print("Введен размер не уд.усл.задачи")
