from tkinter import *
from math import *

def house(picture):
#Дом
   picture.create_rectangle(300,300,550,500,width=2,\
                                                 outline='black',fill='brown')
#Ступени
   x0=550; y0=465; x1=570
   for i in range(4):
      picture.create_rectangle(x0,y0,x1,500,width=2,fill='black')
      x0+=20; y0+=10; x1+=20
   picture.create_polygon([298,300],[425,180],[552,300],width=2,\
                                            outline='black',fill='red')
   picture.create_polygon([330,200],[330,270],[380,226]\
                              ,[380,200],outline='black',width=2,fill='brown')
#Окна
   picture.create_rectangle(400,230,450,280,width=2,fill='gold')
   picture.create_rectangle(400,360,450,430,width=2,fill='gold')
   picture.create_rectangle(370,430,480,435,width=2,fill='black')
   picture.create_line(425,360,425,430,width=2)
   picture.create_line(425,395,450,395,width=2)
#Котяра
   picture.create_oval(455,415,475,425,fill='gray',outline='gray')
   picture.create_line(470,425,472,430,width=2,fill='gray')
   picture.create_line(467,430,469,425,width=2,fill='gray')
   picture.create_line(458,430,460,425,width=2,fill='gray')
   picture.create_line(455,430,457,421,width=2,fill='gray')

   picture.create_line(455,420,457,405,width=2,fill='gray')
   picture.create_oval(472,420,482,410,fill='gray',outline='gray')
   picture.create_polygon([472,420],[477,408],[479,420],width=2,\
                                            outline='gray',fill='gray')
#Дым
   picture.create_oval(300,130,360,190,fill='gray',outline='gray')
   picture.create_oval(255,100,305,150,fill='gray',outline='gray')
   picture.create_oval(210,90,250,130,fill='gray',outline='gray')
   picture.create_oval(175,85,205,115,fill='gray',outline='gray')
   picture.create_oval(150,80,170,100,fill='gray',outline='gray')

def sun(picture):
   picture.create_oval(700,30,850,180,fill='yellow',outline='white')
   i = 0
   while i<=pi*2:
      picture.create_line(130*cos(i)+775,130*sin(i)+105,\
                                           775,105,width=2,fill='yellow')
      i+=(pi*2)/8
    
   j = pi*2/16    
   while j<=pi*2:
      picture.create_line(100*cos(j)+775,100*sin(j)+105,775,105,\
                                                   width=2,fill='yellow')
      j+=pi*2/16

def sky(picture):
   #1
   picture.create_oval(30,20,200,70,fill='white',outline='white')
   picture.create_oval(0,90,100,50,fill='white',outline='white')
   picture.create_oval(125,5,240,50,fill='white',outline='white')
   
   #2
   picture.create_oval(330,70,560,120,fill='white',outline='white')
   picture.create_oval(290,60,430,100,fill='white',outline='white')
   picture.create_oval(420,90,620,140,fill='white',outline='white')

   #3
   picture.create_oval(30,200,200,250,fill='white',outline='white')
   picture.create_oval(5,190,120,230,fill='white',outline='white')
   picture.create_oval(120,220,250,260,fill='white',outline='white')
   
   #4
   picture.create_oval(570,230,770,280,fill='white',outline='white')
   picture.create_oval(640,250,820,300,fill='white',outline='white')
   picture.create_oval(750,250,940,300,fill='white',outline='white')
   picture.create_oval(710,270,880,320,fill='white',outline='white')
   picture.create_oval(770,230,1000,280,fill='white',outline='white')
   picture.create_oval(640,210,820,260,fill='white',outline='white')
   picture.create_oval(750,200,920,250,fill='white',outline='white')
   
def forest(picture):    
   picture.create_rectangle(130,490,150,520,fill='brown')
   picture.create_polygon([50,500],[140,400],[230,500],fill='olivedrab')
   picture.create_polygon([70,450],[140,370],[210,450],fill='olivedrab')
   picture.create_polygon([90,405],[140,340],[190,405],fill='olivedrab')
   picture.create_polygon([110,365],[140,320],[170,365],fill='olivedrab')

   picture.create_rectangle(780,560,800,590,fill='brown')
   picture.create_polygon([700,570],[790,470],[880,570],fill='olivedrab')
   picture.create_polygon([720,520],[790,440],[860,520],fill='olivedrab')
   picture.create_polygon([740,475],[790,410],[835,470],fill='olivedrab')
   picture.create_polygon([760,430],[790,380],[820,430],fill='olivedrab')

root = Tk()
canv=Canvas(root,width=950,height=650,bg='skyblue')

#Земля
canv.create_rectangle(0,465,950,650,fill='green')

sun(canv)
sky(canv)
forest(canv)
house(canv)
canv.pack()
root.mainloop()

