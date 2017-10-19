from math import *

Z = int(input('Введите количество точек пространстрва: '))
X=[];Y=[];x1=[];x2=[];x3=[];y1=[];y2=[];y3=[];Temp=[]; S=[]
for i in range(Z):
    print('x[',(i+1),'] = ',end=' '); X.append(int(input()))
    print('y[',(i+1),'] = ',end=' '); Y.append(int(input()))

def Ploshad(a,bis,degr):    
    S1 = 0.5*a*bis*sin(degr/2)
    return(abs((SB-S1)-S1))
       
def Action(xa,xb,xc,ya,yb,yc):
    AB = sqrt((xb-xa)**2+(yb-ya)**2)
    BC = sqrt((xc-xb)**2+(yc-yb)**2)
    CA = sqrt((xa-xc)**2+(ya-yc)**2)
    
    gamma = acos(((AB)**2-(BC)**2-(CA)**2)/(-2*BC*CA))
    alpha = acos(((BC)**2-(AB)**2-(CA)**2)/(-2*AB*CA))
    betha = acos(((CA)**2-(AB)**2-(BC)**2)/(-2*AB*BC))
   
    CG = (CA*sin(alpha))/sin(betha+gamma/2)
    AG = (CA*sin(gamma))/sin(betha+alpha/2)
    BG = (AB*sin(alpha))/sin(betha/2+gamma)
   
    global SB
    SB = 0.5*BC*CA*sin(gamma)

    Temp.append(Ploshad(AB,AG,alpha))
    Temp.append(Ploshad(BC,BG,betha))
    Temp.append(Ploshad(BC,CG,gamma))

    S.append(min(Temp))
    Temp.clear()
    
for i in range(Z):
    for j in range(i+1,Z):
         for k in range(j+1,Z):
             if (X[k]-X[i])*(Y[j]-Y[i])-(Y[k]-Y[i])*(X[j]-X[i])!=0:
                 x1.append(X[i]); x2.append(X[j]);  x3.append(X[k])
                 y1.append(Y[i]); y2.append(Y[j]);  y3.append(Y[k])
                 
                 
for i in range(len(x1)):
    Action(x1[i],x2[i],x3[i],y1[i],y2[i],y3[i])
print('Результат: ')
if len(S)==0:
    print('Нет точек формирующих плоскость треугольника!')
else:
    cash = S.index(min(S))
    print('x1 = ',x1[cash], 'y1 = ',y1[cash],'\nx2 = ',x2[cash], 'y2 = ',y2[cash]\
 ,'\nx3 = ',x3[cash], 'y3 = ',y3[cash],'\nМинимальная разность площадей = '\
 ,S[cash])
