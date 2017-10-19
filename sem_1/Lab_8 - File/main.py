file = open("main_file.txt")
lines = [line for line in file]
print("Исходные данные:")
for i in lines:  print(i,end="")
print("Для поиска по марке авто введите: 1\nДля поиска по стране изготовителя\
 введите: 2\nДля поиска по марке и стране введите: 3")
cache = input(">> ")
if cache=="1":
   name=input("Введите марку авто: ")
   for i in lines:
       if name == i[i.find(""):i.find(" ")]: print(i,end="")
elif cache == "2":
   country=input("Введите страну: ")
   for i in lines:
       if country == i[i.find(" ")+1:i.rfind(" ")]: print(i,end="")
elif cache == "3":
   name=input("Введите марку авто: "); country=input("Введите страну: ")
   for i in lines:
       if country == i[i.find(" ")+1:i.rfind(" ")]\
       and name == i[i.find(""):i.find(" ")]:
           print(i,end="")
file.close()
