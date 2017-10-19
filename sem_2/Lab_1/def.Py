from math import *
S=[]
Y=[]

def Read(n,m,matS):
    print('Ввод матрицы по 1му элементу в строке: ')
    for i in range(n):
        matS.append([])
        for j in range(m):
            matS[i].append(float(input()))
            
def Action(n,m,matS,masY):
    temp = 0
    for j in range(m):
        for i in range(n):
            if(matS[i][j] > 0):
                    temp = temp + matS[i][j]
        if temp>0:
                masY.append(temp/n)
        temp=0
    masY[masY.index(max(masY))],masY[len(masY)-1]\
    = masY[len(masY)-1],masY[masY.index(max(masY))]
    
def Output(n,m,matS,masY):
    print('Результат:\n Матрица S:\n')
    for i in range(n):
        for j in range(m):
            print('{:5.4}'.format(S[i][j]),end=' ');
        print()
    print('\n Массив Y:\n\n',masY)
    
a=int(input('Введите количество строк матрицы: '))
b=int(input('Введите количество столбцов матрицы: '))

if (1<=a<=12) and (1<=b<=7):
  Read(a,b,S)
  Action(a,b,S,Y)
  Output(a,b,S,Y)
else: print('Приняты значения не удовл. условию задачи!')
