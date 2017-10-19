from random import *
for i in range(5):
 print("Новый цикл")
 k=randint(4,20)
 n=randint(4,20)
 A=[int(randint(3,10)) for i in range(n)]
 B=[int(randint(5,10)) for i in range(k)]
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
  #if (Am==Bm) and AL!=sA and BL != sB:
  if Am==Bm:
     if BL != sB and AL != sA:
      Z[i]=Am
      A.remove(Am)
      sA+=1       
  print(A)
  print(B)
  print(Z)
  print("--------------------------")

