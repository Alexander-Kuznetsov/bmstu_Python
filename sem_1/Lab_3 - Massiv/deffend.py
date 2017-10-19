from math import *
kx = int(input("Введите количество элементов массива X: "))
ky = int(input("Введите количество элементов массива Y: "))
kz = int(input("Введите количество элементов массива Z: "))

print("Ввод массива X: ")
X = [int(input()) for i in range(kx)]
print("Ввод массива Y: ")
Y = [int(input()) for i in range(ky)]
print("Ввод массива Z: ")
Z = [int(input()) for i in range(kz)]
print("Массив X = ", X)
print("Массив Y = ", Y)
print("Массив Z = ", Z)
for i in range(len(X)):
 Xm = min(X)
 X.remove(Xm)
 county = 0
 countz = 0
 for j in range(len(Y)):
     if Xm == Y[j]:
         county = 1
         break
 for k in range(len(Z)):
     if Xm == Z[k]:
         countz = 1
         break
 if county == 0 and countz == 0: print(Xm)
 
