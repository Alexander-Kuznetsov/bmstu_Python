from math import *
Ntoc=int(input('Введите количество точек пространства: '))
Ntre=int(input('Введите количество треугольников пространства: '))
xt = []; yt = []; x1 = []; x2 = []; x3 = []; y1 = []; y2 = []; y3 = []
x1t=[];x2t=[];x3t=[];y1t=[];y2t=[];y3t=[]
def A(y1,y2):
    A=y1-y2
def B(x1,x2):
    B=x2-x1
def C(x1,x2,y1,y2):
    C=x1*y2-x2*y1
print('Ввод множества точек: ')
for i in range(Ntoc):
    print('x[',(i+1),'] = ',end=' '); xt.append(int(input()))
    print('y[',(i+1),'] = ',end=' '); yt.append(int(input()))
print('Ввод множества треугольников: ')
for i in range(Ntre):
    print('Треугольник: ',i+1)
    print('x1 = ',end=' '); x1.append(int(input()))
    print('y1 = ',end=' '); y1.append(int(input()))
    print('x2 = ',end=' '); x2.append(int(input()))
    print('y2 = ',end=' '); y2.append(int(input()))
    print('x3 = ',end=' '); x3.append(int(input()))
    print('y3 = ',end=' '); y3.append(int(input()))
    
for i in range(len(x1)):
     for j in range(i+1,x1):
          for k in range(j+1,x1):
               x1t.append(xt[i]) y1t.append(yt[i])
               x2t.append(xt[j]) y2t.append(yt[j])
               x3t.append(xt[k]) y3t.append(yt[k])
or i in range(len(x1t))
        A=A(
        B
        C
         y1=-C(yt1[i])*A   
    
