#Лабараторная работа №6 (номер 54)-5 Выполнил: Кузнецов Александр ИУ7-13
from math import *
minfy=0;const = 0.00000001
x = float(input("Ввод начального значения x: "))
x1=x
xmi=0
x2= float(input("Ввод конечного значения x: "))
sh = float(input("Ввод шага счета: "))
print(" ________________________________________")
print("|      Y1      |      Y2      |     x    |")
print("-----------------------------------------")
P = 0.5*(exp(x) - exp(-x)) + cos(x)*cos(x)
xmi=x
mi=ma=P
#Высчитывание значений ф-ий и построение таблицы
while x<=x2+const:
  P = 0.5*(exp(x) - exp(-x)) + cos(x)*cos(x)
  Q = e**(-x-1) + 1
  print("|","{:12.5}".format(P),"|","{:12.5}".format(Q),\
        "|","{:8.3f}".format(x),"|")
  print("________________________________________")
  
  #Нахождение минимумов и максимумов функций
  if mi>P:
    mi=P
    xmi=x
  if ma<P: ma=P
  x+=sh
x=x1
ll=P
while x<=x2+const:
  P = 0.5*(exp(x) - exp(-x)) + cos(x)*cos(x)
  #if P<=0:  minfy=((P-mi)/(ma-mi))*60
  if (-1)*abs(ll)<=(-1)*abs(P):
    minfy=((P-mi)/(ma-mi))*60
  ll=P 
  x+=sh
print()
print("График функции: Y1")
print()
#Отрисовка графика функции
while x1<=x2+const:
  funct = 0.5*(exp(x1) - exp(-x1)) + cos(x1)*cos(x1)
  fy = ((funct-mi)/(ma-mi))*60
  if funct<0:
    if round(fy)==round(minfy): print("{:8.3f}".format(x1)," "*round(fy)+"*")  
    else: print("{:8.3f}".format(x1)," "*round(fy)+"*"+\
          " "*(round(minfy)-round(fy)-1)+"|")
  if funct>0:
    if round(fy)==round(minfy): print("{:8.3f}".format(x1)," "*round(fy)+"*")
    else:  print("{:8.3f}".format(x1)," "*round(minfy)+"|"+\
           " "*round(fy-minfy)+"*")
  x1+=sh
  fy=0
print(" "*(round(minfy)+9) +"▼(x)")
print("Минимальное значение функции Y1: ","{:12.5}".format(mi)," при х: ",xmi)
