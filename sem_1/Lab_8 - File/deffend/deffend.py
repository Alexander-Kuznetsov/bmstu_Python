file = open("File.txt")
lines = [i for i in file]
print("Для поиска по марке компьютера введите: 1\nДля поиска по тактовой \
частоте введите: 2\nДля поиска по марке комп. и тактовой частоте введите: 3")
temp = input("-> ")
if temp !="1" and temp !="2" and temp !="3":
    print("Данные введены неверно")
else:
 Newfile = open("NewFile.txt","w")
 if temp == "1":
    mark=input("Введите марку компьютера: ")
    for i in lines:
       if mark == i[i.find(""):i.find(" ")]:        
           print(i,end="")
           Newfile.write(i)
    Newfile.close()
 elif temp == "2":
    V=input("Введите тактовую частоту(ГГц): ")
    for i in lines:
       if V == i[i.find(" ")+1:i.rfind(" ")]:
           print(i,end="")
           Newfile.write(i)
    Newfile.close()
 elif temp == "3":
     mark=input("Введите марку компьютера: ");
     V=input("Введите тактовую частоту: ")
     for i in lines:
       if V == i[i.find(" ")+1:i.rfind(" ")]\
       and mark == i[i.find(""):i.find(" ")]:
           print(i,end="")
           Newfile.write(i)
     Newfile.close()
file.close()

