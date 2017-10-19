from math import *
x = float(input("Введите Х от -1 до 1: "))
eps = float(input("Введите эпселон: "))
k=0
count = 0
z=0
a=1
if (-1<=x<=1):
 u=0
 while a == 1:
  count+=1
  h=1
  g=1
  p=u
  if u%2 == 0: k = 1
  else: k = -1
  for i in range(0,(p*2)+1,2):
      if i!=0: h*=i
  for i in range(1,(p*2)+1,2): g*=i
  if abs((g/h)*x**u)>abs(eps):
     z+=k*(g/h)*x**u
  if abs((g/h)*x**u)<=abs(eps):
      print("Сумма ряда = ","{:5.7}".format(z))
      break
  u+=1
else: print("Ожидалось: -1<=x<=1")  
