D=[["Горный велосипед позволяет быстрее передвигаться в городском велобездорожьи, \
реже спешиваться и эффективно преодолевать препятствия. Но у у у у у многоскоростных "]\
   ,["велосипедов есть существенный недостаток."]\
   ,["Так по моему опыту наезжал  больше 1000км за сезон, для дорожного \
велосипеда достаточно один раз смазать и перебрать"],["велосипеда в начале года \
и он будет бегать не не не не создавая проблем."]]
Temp=[];X=[];P=[];G=[]
print(D)
for i in D:
  for j in i:
    for h in j:
      if  h!="," or h!=":":
        Temp.append(h)
    Temp.append(" ")
for i in range(len(Temp)):
   if Temp[i]=="." or Temp[i]=="!" or Temp[i]=="?":
     P.append(" ")
   P.append(Temp[i])
#print(Temp)
#print(P)
k=0;a="";G.append([])
for i in P:
   if i!=" ":
     a+=i
     G.append([])
   if i==" ":
      G[k].append(a)
      k+=1
      a=""
#print(G)
##
d=[]
#print(d)
d.append([])
k=0;
for i in G:
    for j in i:
        if j==".":
            d.append([])
            k+=1
        if j!=".":
         d[k].append(i)
#print(d)
k=0;s=0;kol=0;word=0;maxkol=0;mword=0
for i in d:
   for j in i:
     #if j!='':
     #  print(j)
       kol=d[k].count(j)
       word=j
       if maxkol<kol:
           maxkol=kol
           mword=word
   if k+1!=len(d):
    print("В предложении: ",k+1,"слово: ",mword," повторяется: ",maxkol)
    kol=word=mword=maxkol=0
   k+=1
