# Вариант 4
L = int(input("Введите длину массива: "))
if (L <= 11 and L > 0):
 S = [0]*L
 S = [int(input()) for i in range(len(S))]
 print("Исходный массив: ", S)
 for i in range(len(S)):
  k=0
  for j in range(i+1,len(S)):      
      if S[i] == S[j]:
          S[j] = "0"
          k+=1
  if k!=0:
      S[i] = "0"
 c = S.count("0")
 for i in range(c):
      S.remove("0")
 if c!=L: print("Результат: ", S)
 else: print("Результат: неповторяющихся элементов не обнаружено")
else: print("Длина массива задана не по усл.")
