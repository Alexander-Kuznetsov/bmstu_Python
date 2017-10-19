abc=["ц","к","н","г","ш","щ","з","х","ф",\
     "в","п","р","л","д","ж","э","ч","с","м","т","б"]
D=[["За переход дороги в неположенном месте предусмотрен штраф "]\
,["в размере 500р."],["Пешеходы обязаны соблюдать правила ПДД."],\
["За каждого сбитого пешехчччччччччччода отвечает водитель, так как он управляет "],\
["средством повышенной опасности."]]
print("Исходный текст: ")
B=[];
for i in D:
    for j in i:
        for h in j:
            if h!="," and h!=".": B.append(h)
            if h==".": B.append(" "); B.append(h);
            print(h,end="")
MaxWord = 0; Word = 0;MaximWord=[]
for i in range(len(B)):
   for j in range(len(abc)):
       if abc[j]==B[i].lower(): Word+=1
   if B[i]==" ":
       if MaxWord<Word:  MaxWord=Word
       Word = 0
   if B[i]==".": MaximWord.append(MaxWord)
kolvo = max(MaximWord)
for i in range(len(MaximWord)):
    if MaximWord[i]==kolvo:
        predlogenie=i+1
        break
print("\nВ предложении: ",predlogenie," есть слово с ",kolvo, " согласными")
