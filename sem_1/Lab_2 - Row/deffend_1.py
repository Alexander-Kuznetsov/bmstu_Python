from math import *
x = float(input("Задайте значение Х: "))
n = int(input("Введите до какого числа будет проводится операция: "))
eps = float(input("Введите значение Eps: "))
j=0
z=0
for i in range(1,n+1):
    j=j+1
    if i % 2 !=0:
      if x**i/factorial(i) >= eps:
        z+=x**i/factorial(i)
        print("n = ",round(i,4),"            ","z = ",round(z,4), "            ","Текущ. знач = ",round(x**i/factorial(i),4))
      else:
        z+=x**i/factorial(i)
        print("n = ",round(i,4),"            ","z = ", round(z,4),"            ","Текущ. знач = ",round(x**i/factorial(i),4))
        print("Ряд сошелся")
        break
    if n == j and  x**i/factorial(i)>= eps: print("Ряд не сошелся за N-цикл, текущее значение n= ",n ,"текущее значение z = ", round(z,4),"Текущ.знач = ",round(x**i/factorial(i),4))
