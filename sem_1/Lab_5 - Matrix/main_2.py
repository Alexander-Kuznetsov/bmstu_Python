#Лабараторная работа - Вычислить бесконечный ряд
#Кузнецов ИУ7-13
from math import *
x = float(input("Введите x: "))
print("____________________________________")
P=0
if x<=1: print("Результат: 1")
else:
 if 1<x<2:
  eps = float(input("Введите eps: "))
  n=1
  y=n*x/(x+1)**n
  P+=y
  n=2
  while True:
    if abs(eps)<abs(y):
     y=n*x/(x+1)**n
     P+=y
     n+=1
    else:
     print("Результат: ","{:5.4}".format(P))
     break
 if x>=2:
  for i in range(1,6+1):
     j=1
     z=1
     while j!=i+1:
         z*=i/(j*x)
         j+=1         
     P+=z
     print(z)
  print("Результат: ","{:5.4f}".format(P))
     
