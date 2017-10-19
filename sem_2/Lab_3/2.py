Ax=[]; Ay=[]
Box=[]; Boy = []; Razn = []
x1=[];x2=[];y1=[];y2=[];x1temp = []; y1temp = []; x2temp = []; y2temp = []
Nt = int(input("Введите количество точек: "))
R = []
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
for i in range(Nt):
    for j in range(i+1,Nt):
          x1.append(Ax[i]); x2.append(Ax[j]);
          y1.append(Ay[i]); y2.append(Ay[j]);
print(x1temp)#[ind],y1temp[ind],x2temp[ind],y2temp[ind])
for i in range(len(x1)):    
    for j in range(No):
        vishe = 0
        nije = 0
        for k in range(Nt):
            if (Ax[k]**2+Ay[k]**2 < R[j]**2):
                if (x1[i]-x2[i])*Ay[k]+(y1[i]-y2[i])*Ax[k]+(x1[i]*y2[i]-x2[i]*y1[i])>0 :
                   vishe +=1
                if (x1[i]-x2[i])*Ay[k]+(y1[i]-y2[i])*Ax[k]+(x1[i]*y2[i]-x2[i]*y1[i])<0 :
                   nije +=1
        x1temp.append(x1[i])
        x2temp.append(x2[i])
        y1temp.append(y1[i])
        y2temp.append(y2[i])
        Razn.append(abs(vishe-nije))
ind = Razn.index(min(Razn))
#print('(',x1temp[ind],y1temp[ind]\
#      ,')','  (',x2temp[ind],y2temp[ind],')
print(x1temp[ind],y1temp[ind],x2temp[ind],y2temp[ind])
print('Разность минимальна = ',Razn[ind])
    
   
