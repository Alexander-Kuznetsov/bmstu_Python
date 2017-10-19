from math import *
Z=[]
N = int(input("Введите длину массива X: "))
print("Задайте массив X")
X = [float(input()) for i in range (N)]
M = int(input("Введите длину массива Y: "))
Y = [float(input()) for i in range (M)]
Z=X+Y
for i in range(len(Z)):
 s=0
 minf=Z[i]
 for j in range(i,len(Z)):
    if Z[j]<=minf:
        minf=Z[j]
        s=j
 Z[s]=Z[i]
 Z[i]=minf
print(Z)
#Дан массив X(>=17) Y(>=10)
#получить массив X+Y = Z 
