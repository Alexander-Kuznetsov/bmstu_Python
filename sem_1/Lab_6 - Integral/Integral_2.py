from math import *
print("Ввод исходных данных:")
a = float(input("Нижний предел интегрирования(a): "))
b = float(input("Верхний предел интегрирования(b): "))
h1 = int(input("Количество отрезков(n1): "))
h2 = int(input("Количество отрезков(n2): "))
if h1==0 or h2==0:
   print("Ошибка ввода исходных данных")
else:
 eps = float(input("Введите eps: "))
 print("______________________________\nРезультат работы программы:")
 def Funct(x):
    #I=x*x
    I=x+1
    return(I)  
 def methodTrapec(n):
    h=abs((b-a)/n)
    a1=a+h
    summa=0
    while a1<b:
      summa+=Funct(a1)
      a1+=h
    Ploshad = h*((Funct(a)+Funct(b))/2 + summa)
    return(Ploshad)
 def method38(n):
     h=abs((b-a)/(3*n))
     summa=0;k=3*n
     for i in range(k):
         x=a+h*i
         if i%3==0:
             summa+=2*Funct(x)
         else:
             summa+=3*Funct(x)
     Ploshad = 3/8*h*(Funct(a)+Funct(b)+summa)
     return(Ploshad)
 print("______________________________________________________")
 print("|   Метод    |  n1 = ","{:10}".format(h1),\
       "|  n2 = ","{:10}".format(h2),"|")
 print("______________________________________________________")
 print("|  Трапеция  |","{:17.10}".format(methodTrapec(h1)),\
       "|","{:17.10}".format(methodTrapec(h2)),"|")
 print("______________________________________________________")
 print("|    3/8     |","{:17.10}".format(method38(h1)),\
       "|","{:17.10}".format(method38(h2)),"|")
 print("______________________________________________________")
 h3 = 1; Integral=methodTrapec(h3)
 while abs(methodTrapec(2*h3)-methodTrapec(h3))>abs(eps):
     Integral = methodTrapec(h3)
     h3*=2
 print("Значение интеграла (метод Трапеции) = ","{:5.10}".format(Integral)\
       ," Участков разбиения = ",h3)
 
 
     

    
