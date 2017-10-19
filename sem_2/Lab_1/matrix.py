from math import *
N = int(input("Введите размер матрицы: "))
A=[]
if(N<=7)and(N>=2):
 print("Введите элементы массива по 1му в строке: ")
 for i in range(N):
    A.append([]) 
    for j in range(N):
        A[i].append(int(input()))
 print("Исходная матрица: ")
 for i in range(N):
    for j in range(N):
        print("{:4}".format(A[i][j]),end=" ")
    print()
 print("Результат работы программы: ")
 A.reverse()
 for i in range(N):
     for j in range(N):
       A[i][j]=A[N-j-1][i]
 print(A)
 #for j in range(N):
  #  for i in range(N):
   #     print("{:4}".format(A[i][j]),end=" ")
 #   print()
else: print("Введен размер не уд.усл.задачи")
