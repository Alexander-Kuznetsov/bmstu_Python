from math import sqrt
Ax=[]; Ay=[]
Box=[]; Boy = []; R = []
Xtemp = []
Ytemp = []
Rtemp = []
Temp = []
Nt = int(input("Введите количество точек: "))
No = int(input("Введите количество окружностей: "))
for i in range(Nt):
    print('x(точки)[',i+1,'] = ',end = ' ')
    Ax.append(float(input()))
    print('y(точки)[',i+1,'] = ',end = ' ')
    Ay.append(float(input()))
for i in range(No):
    print('x(центра окружности)[',i+1,'] = ',end = ' ')
    Box.append(float(input()))
    print('y(центра окружности)[',i+1,'] = ',end = ' ')
    Boy.append(float(input()))
    print('Радиус окружности[',i+1,'] = ',end = ' ')
    R.append(float(input()))

for i in range(No):
    k=0
    for j in range(Nt):
        if (sqrt((Ax[j]-Box[i])**2 + (Ay[j]-Boy[i])**2)<=R[i]):
            k+=1
    Temp.append(k)
    Xtemp.append(Box[i])
    Ytemp.append(Boy[i])
    Rtemp.append(R[i])
ind  = Temp.index(max(Temp))
print('\nРезультат: \n')
print('Окружность с x: ', round(Xtemp[ind],3), '; y: ',\
      round(Ytemp[ind],3)
      ,'; R: ',round(R[ind],3)\
      ,' имеет максимальное количество точек: ', Temp[ind])
