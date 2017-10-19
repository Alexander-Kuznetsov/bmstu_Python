#Защита лаб #1 Кузнецов Александр ИУ7-13 номер 22
from math import *
xa = float(input("Введите координату точки А на х: "))
ya = float(input("Введите координату точки A на y: "))
xb = float(input("Введите координату точки B на x: "))
yb = float(input("Введите координату точки B на y: "))
xc = float(input("Введите координату точки C на х: "))
yc = float(input("Введите координату точки C на y: "))
if (xc-xa)*(yb-ya)-(yc-ya)*(xb-xa) !=0:
 AB = sqrt((xb-xa)**2+(yb-ya)**2)
 BC = sqrt((xc-xb)**2+(yc-yb)**2)
 CA = sqrt((xa-xc)**2+(ya-yc)**2)
 alpha = acos(((AB)**2-(BC)**2-(CA)**2)/(-2*BC*CA))
 betha = acos(((BC)**2-(AB)**2-(CA)**2)/(-2*AB*CA))
 gamma = acos(((CA)**2-(AB)**2-(BC)**2)/(-2*AB*BC))
 S=0.5*AB*BC*sin(gamma)
 if alpha <= betha and alpha <= gamma: h = (2*S)/AB
 elif betha <= alpha and betha <= gamma: h = (2*S)/BC
 elif gamma <= betha and gamma <= alpha: h = (2*S)/CA
 print("Высота из наименьшего угла = ",round(h,4))
else: print("по заданным координатам нельзя построить треугольник")
