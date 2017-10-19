X = []; xi=[]; yj=[]; S=[]

def Read(matrix,N):
    print('Ввод матрицы по одному элементу в строке')
    for i in range(N):
        matrix.append([])
        for j in range(N):
            temp = input()
            if temp != "t" and temp != "f":
               print('Ошибка введенного элемента, ожидалось: `t` or `f`\n\
               Попробуйте снова: ')
               temp = input()
            matrix[i].append(temp)
            
def Write(matrix,N):
    print('Ваша матрица:')
    for i in range(N):
        for j in range(N):
            print(matrix[i][j],end = ' ')
        print()

def Action(matrix, N):
  I=[]; J=[];Plosh=[]
  for i in range(N):
      for j in range(N):
          if matrix[i][j]=='t':
              I.append(i);J.append(j)
              firstI = i; endI = i
              firstJ = j; endJ = j
              length = 1; width = 1
              while matrix[i][endJ]!='f' and endJ!=N-1:
                  length+=1
                  endJ+=1
              while matrix[endI][j]!='f' and endI!=N-1:
                  width+=1
                  endI+=1
              for k in range(firstI,endI+1):
                  for d in range(firstJ,endJ+1):
                      matrix[k][d]='f'
              Plosh.append(length*width)
  Ind=Plosh.index(max(Plosh))
  print('Результат:\nx: ',I[Ind]+1,'\ny: ',J[Ind]+1)
              
M = int(input('Введите размер матрицы: '))  
    
Read(X,M)
Write(X,M)
Action(X,M)
