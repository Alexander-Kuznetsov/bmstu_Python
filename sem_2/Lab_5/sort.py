#======Binar Insert Sort====== by Kuznetsov v1.1
import time
from random import *
print('Binar Insert Sort')
stack = [1000,10000,100000];
def BinInsert(Mas):                   #Сортировка бинарными вставками
    for i in range(1,len(Mas)):          
             temp = Mas[i]
             left = 0
             right = i-1
             
             while left<=right:
                 m = (left+right)//2
                 if temp<Mas[m]:  right = m-1
                 else:            left = m+1
             Mas.pop(i)
             Mas.insert(left,temp)
    return(Mas)

def BinInsertPart2(Mas):              #-/- для матрицы [[1,'t','t'],[2,'f','t']]
    for i in range(1,len(Mas)):      
             temp = Mas[i][0]
             temp1 = Mas[i]
             left = 0
             right = i-1
             
             while left<=right:                 
                 m = (left+right)//2
                 if temp < Mas[m][0]:  right = m-1
                 else:            left = m+1
             Mas.pop(i)
             Mas.insert(left,temp1)
    return(Mas)


def Times(Mas,Alg):                        #Измеряет время выполнения алгоритма 
    start = time.time()
    Alg(Mas)
    return(round((time.time()-start),6))

def Table(stack,timeSort,timeRand,timeRevSort):   #Таблица
 print('-----------------------------------------------------------------------')
 print('| N |Elements qt. |Time(Sort(mas))| Time(Rand(mas))| Time(reverse(mas))')
 print('-----------------------------------------------------------------------')
 for i in range(len(stack)):  
   print('|'+'{:3}'.format(i+1)+'|'+\
        '{:13}'.format(stack[i])+'|'+\
            '{:15.6}'.format(timeSort[i])+'|'+\
               '{:16.6}'.format(timeRand[i])+'|'+\
                   '{:18.6}'.format(timeRevSort[i])+'|')
   print('-----------------------------------------------------------------------')

def Action(Alg,stack):           #Подсчет времени, сортировка,вывод таблицы
  timeRand = []; timeSort = []; timeRevSort = []; Mas = []
  for i in stack:
    if Alg == BinInsert:      #Заполнение 1го массива    
       for j in range(i): Mas.append(randint(-10000,10000))
    else:                     #Заполнение 2го массива
       for j in range(i):
           Mas.append([])
           for k in range(3):
              if k==0: Mas[j].append(randint(-10000,10000))
              else:    Mas[j].append(chr(randint(65,128)))
              
    timeRand.append(Times(Mas,Alg))
    timeSort.append(Times(Mas,Alg))
    Mas.reverse()
    timeRevSort.append(Times(Mas,Alg))
    Mas.clear()
  Table(stack,timeSort,timeRand,timeRevSort)
  
print('Part 1 (Sorting integer numbers)')
#print('Example: before [4,5,2,1]; after [1,2,4,5]')
Action(BinInsert,stack)
print('Part 2 (Sorting char symbols and integer nubmers)')
#print('Example: before [[`3`,`t,`t`],[`1`,`t`,`r`]]')
Action(BinInsertPart2,stack)






