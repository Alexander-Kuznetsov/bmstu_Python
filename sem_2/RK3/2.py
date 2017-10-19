#2 Шейкер сортировка Билет 6

Y=[]
N=int(input('Длинна списка: '))
print('Заполнение списка по 1-му элементу в строке')
for i in range(1,N+1):
    Y.append(int(input()))
print('Исходный список:')
print(Y)
def SheikSort(Mas):
	for k in range(len(Mas)-1, 0, -1):
		key = False
		for i in range(k, 0, -1):
			if Mas[i]<Mas[i-1]:
				Mas[i], Mas[i-1] = Mas[i-1], Mas[i]
				key = True

		for i in range(k):
			if Mas[i] > Mas[i+1]:
				Mas[i], Mas[i+1] = Mas[i+1], Mas[i]
				key = True
				
		if key == False: break
		
SheikSort(Y)
print('Отсортированный по возрастанию список:')
print(Y)
