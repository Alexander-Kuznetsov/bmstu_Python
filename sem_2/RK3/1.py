#1 Max индекс + Sort включениями + time sort Билет 6
import time
print('Введите количество символов <=8 символов:')
N = int(input('> '))
R=[0]*12

def Sort(Mas,N):   
    global ind, Times
    Maxim = Mas[3]   
    ind = 3
    for i in range(3,N+3):
           if Mas[i]>Maxim:
               Maxim = Mas[i]
               ind = i
               
    t1 = time.time()
    for i in range(3,N+3):
        min_ind = i
        for j in range(i, N+3):
            if Mas[min_ind] < Mas[j]:
                min_ind = j
        Mas[i], Mas[min_ind] = Mas[min_ind], Mas[i]
    Times = time.time()-t1


if N<=8:  
  print('Ввод элементов массива по 1-му в строке:')
  for i in range(3,3+N):
      R[i]=float(input())
       
  print('Исходный список: ')
  for i in range(3,N+3):
      print(R[i],end=' ')
  Sort(R,N)  
  print('\n\nМаксимальный элемент списка имеет индекс: ',ind)
  print('\nОтсортированный массив: ')
  for i in range(3,N+3):
      print(R[i],end=' ')
  
  print('\nВремя выполнения сортировки *1000 = ', Times*1000)
else:
    print('Количество элементов не уд.усл.задачи')
