#Программа построения по 3м точкам треугольника
#и вычисление: сторон, биссектрисы из меньшего угла
#и лежит ли точка в заданной плоскости(Кузнецов ИУ7-13)

from math import *

xa = float(input("Введите координату точки А на х: "))
ya = float(input("Введите координату точки A на y: "))
xb = float(input("Введите координату точки B на x: "))
yb = float(input("Введите координату точки B на y: "))
xc = float(input("Введите координату точки C на х: "))
yc = float(input("Введите координату точки C на y: "))

#Проверка по уравнению прямой(лежат ли 3 точки на одной прямой или нет)
if (xc-xa)*(yb-ya)-(yc-ya)*(xb-xa) !=0:
 #Высчитывает длины векторов по координатам
 AB = sqrt((xb-xa)**2+(yb-ya)**2)
 BC = sqrt((xc-xb)**2+(yc-yb)**2)
 CA = sqrt((xa-xc)**2+(ya-yc)**2)
 
 #Высчитывает углы треугольника по т.кос
 alpha = acos(((AB)**2-(BC)**2-(CA)**2)/(-2*BC*CA))
 betha = acos(((BC)**2-(AB)**2-(CA)**2)/(-2*AB*CA))
 gamma = acos(((CA)**2-(AB)**2-(BC)**2)/(-2*AB*BC))
 
 #Определяет наименьший угол и проводит биссектрису из наименьшего угла по т.син
 if alpha <= betha and alpha <= gamma: bis = (CA*sin(betha))/sin(gamma+alpha/2)
 elif betha <= alpha and betha <= gamma: bis = (CA*sin(alpha))/sin(gamma+betha/2)
 elif gamma <= betha and gamma <= alpha: bis = (AB*sin(betha))/sin(gamma/2 + alpha)
 #Выводит все 3 длины прямых и длину биссектрисы
 print("AB = ", round(AB,4), " BC = ", round(BC,4),  " AC = ", round(CA,4)," биссектриса = ", round(bis,4))
 
 #Ввод координат точки, которую будем проверять на пренадлежность к заданной плоскости
 xt = float(input("Введите координату точки t на x: "))
 yt = float(input("Введите координату точки t на y: "))
 
 #Высчитывает площади основного треугольника и площади 3х треугольников, образованных данной точкой
 S = abs((xc-xa)*(yb-ya)-(yc-ya)*(xb-xa))/2
 s1 = abs((xt-xa)*(yb-ya)-(yt-ya)*(xb-xa))/2
 s2 = abs((xt-xb)*(yc-yb)-(yt-yb)*(xc-xb))/2
 s3 = abs((xt-xc)*(ya-yc)-(yt-yc)*(xa-xc))/2
 
 #Проверка на равенство основной площади и суммы 3х площадей образованной данной точкой
 if s1+s2+s3==S:
   #Если все хорошо, то получаем, что точка лежит в плоскости
   print("Точка лежит в треугольнике")
   #Считает 3 высоты треугольников образованной данной точкой
   h1=(2*s1)/AB
   h2=(2*s2)/BC
   h3=(2*s3)/CA
   #Находим самую большую высоту => это и будет наибольшее удаление точки от прямой
   maxh=h1
   if h2>=maxh: maxh = h2
   if h3>=maxh: maxh = h3
   #Вывод наибольшего расстояния от точки до прямой, с 4мя знаками после запятой
   print("Наибольшее расстояние от точки до прямой = ", round(maxh,4))
 else: print("Точка не лежит в треугольнике")
#Если 3 точки лежат на одной прямой или 2 точки имеют одинаковую координату
else:print("Ошибка в построении: неверно введены координаты")
