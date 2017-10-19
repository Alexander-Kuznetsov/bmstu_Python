from math import *

print("Введите уравнение вида +(-)ax^2 +(-) bx +(-) c = 0")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("введите c: "))
 
if a!=0:  
 if b != 0 and c != 0:
  D = b**2 - 4*a*c
  if D > 0:
   x1=((-b)+sqrt(D))/(2*a)
   x2=((-b)-sqrt(D))/(2*a)
   print("Первый корень = ",round(x1,4)," Второй корень = ",round(x2,4))
  elif D==0:print("Корень = ",(-b)/(2*a))
  else: print("Невозможно высчитать, D < 0")
 elif b==0 and c==0:print("Корень = 0")
 elif c==0 and b!=0:print("Первый корень = 0 Второй корень = ",round((-b/a),4))
 elif c!=0 and b==0 and (-c)/a > 0: print("Первый корень = ", round(sqrt(-c/a),4)," Второй корень = ",-sqrt(-c/a))
 elif c!=0 and b==0 and (-c)/a < 0: print("Корней нет")
else: print("Это не квадратное уравнение") 

