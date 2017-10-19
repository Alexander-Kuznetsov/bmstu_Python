from math import *
from random import *

M = int(input("Длина Строки: "))
N = int(input("Длина Столбца: "))
X =[]
B=[]
G=[]
mas=[]
h=0;h1=N-1
for i in range(N):
 X.append([])
 for j in range(M):
   X[i].append(float(input()))
print("Исходная Матрица")
for i in range(N):
  for j in range(M):
    print("{:5.3}".format(X[i][j]),end=" ")
  print()
#for i in range(N):
#  B.append(X[i][i])
#print("Главная диагональ: ", B)
#for i in range(N):
#  G.append(X[h1][h])
#  h+=1
#  h1-=1
#print("Побочная диагональ: ", G)
#print("Рандомная матрица: ")
#for i in range(N):
#  mas.append([])
#  for j in range(N):
#    mas[i].append(randint(-10,10))
#for i in range(N):
#  for j in range(N):
#    print("{:5.3f}".format(mas[i][j]),end= " ")
#  print()
#_-------------------поворот матрицы
print("Поворот матрицы" )
X.reverse()
st=N
if N<M:
  st=M
  for i in range(M-N,M):
    X.append([])
    for j in range(M):
      X[i].append("*")
if M<N:
  st=N
  for i in range(N):
    X.append([])
    for j in range(N-M,N):
      X[i].append("*")

for i in range(st):
  for j in range(i,st):
   # print(i,j)
    X[i][j],X[j][i]=X[j][i],X[i][j]

#for i in range(st):
#  for j in range(st):
 #   if X[i][j]=="*":
  #    X.pop(j)
for i in range(st):
 for j in range(st):
   if X[i][j] != "*":
    print("{:4.3}".format(X[i][j]),end= " ")
 print() 

 
