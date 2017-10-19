s=str(input("Введите строку: "))
x=[]
WordRus=["А","Е","Ё","И","О","У","Ы","Э","Ю","Я"]
WordEng=["A","E","I","O","U","Y"]
kolrus=koleng=0
def funct(a,b,c=0):
 for i in range(a,b):
  for j in s:     
    if chr(i)==j:
        c+=1
 return c
print("Количество строчных английских букв = ",funct(97,123))
print("Количество строчных русских букв = ",funct(1072,1104))
for i in WordRus:
    for j in s:
        if i==j:
           x.append(j)
           kolrus+=1
for i in WordEng:
    for j in s:
        if i==j:
            x.append(j)
            koleng+=1
for i in range(48,57):
    for j in s:
        if chr(i)==j:
            x.append(j)
if len(x)>0:
    print(x)
    for i in range(len(x)):
      print(x[i],"=", ord(x[i]))
else: print("Прописных букв или цифр не обнаружено")

 

  
