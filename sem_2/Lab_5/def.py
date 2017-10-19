print('Ввод массива элемент через пробел:')
M = list(map(int,input().split()))

def BinInsert(Mas):
    for i in range(1,len(Mas)):      
             temp = Mas[i]
             left = 0
             right = i
             
             while left<right:                 
                 m = (left+right)//2
                 if temp<Mas[m]:  right = m-1
                 else:            left = m+1
             Mas.pop(i)
             Mas.insert(left,temp)       
    return(Mas)

M = BinInsert(M)
print(M)




