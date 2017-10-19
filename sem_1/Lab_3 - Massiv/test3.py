from random import *
n = int(input("ввод длины А: "))
k = int(input("ввод длины B: "))
print("Ввод массива А")
A=[float(input()) for i in range(n)]
print("Ввод массива B")
B=[float(input()) for i in range(k)]
Z=[]
N = len(A)+len(B)
AL = len(A)
BL = len(B)
Z=[0]*N
print(A)
print(B)
print("--------------------")
sA=0
sB=0
for i in range(len(Z)):

  if sB != BL: Bm = min(B)
  if sA != AL: Am = min(A)

  if Am>Bm and sB != BL:
      Z[i]=Bm
      B.remove(Bm)
      sB+=1

  elif Bm>Am and sA != AL:
      Z[i]=Am
      A.remove(Am)
      sA+=1

  else:
     if sA == AL and sB != BL:
      Z[i]=Bm
      B.remove(Bm)
      sB+=1
      
     if sB == BL and sA != AL:
      Z[i]=Am
      A.remove(Am)
      sA+=1

  if Am==Bm:
     if BL != sB and AL != sA:
      Z[i]=Am
      A.remove(Am)
      sA+=1       
print(Z)
 
