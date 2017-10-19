from tkinter import *
from math import *
window = Tk()
W=950; H = 650
canv=Canvas(window,width=W,height=H,bg='skyblue')
canv.create_rectangle(0,450,950,650,fill='orange')
#for i in range(W,0+50,-50):
 #   k=0
 #   for j in range(H,0+50,-50):       
 #       canv.create_text(i,j,fill='green',text=j)
 #       if k==0:
  #        canv.create_text(i,j,fill='red',text=i)
  #      k+=1
def sun(picture):
   picture.create_oval(100,100,150,150,fill='yellow',outline='white')
   i = 0
   while i<=pi*2:
      picture.create_line(130*cos(i)+125,130*sin(i)+125,\
                                          125,125,width=2,fill='yellow')
      i+=(pi*2)/8
    
   j = pi*2/16    
   while j<=pi*2:
      picture.create_line(100*cos(j)+125,100*sin(j)+125,125,125,\
                                                   width=2,fill='yellow')
      j+=pi*2/16
      
sun(canv)

#бревно
canv.create_rectangle(110,470,160,350,fill='brown')
canv.create_oval(50,300,140,390,fill='olivedrab',outline='olivedrab')
canv.create_oval(130,300,210,390,fill='olivedrab',outline='olivedrab')
canv.create_oval(30,250,150,360,fill='olivedrab',outline='olivedrab')
canv.create_oval(140,250,260,360,fill='olivedrab',outline='olivedrab')
canv.create_oval(70,175,190,300,fill='olivedrab',outline='olivedrab')
canv.create_oval(170,210,240,300,fill='olivedrab',outline='olivedrab')
#яблоко
canv.create_oval(120,300,140,320,fill='red',outline='olivedrab')
canv.create_oval(210,250,230,270,fill='red',outline='olivedrab')
canv.create_oval(100,200,120,220,fill='red',outline='olivedrab')
canv.create_oval(110,250,130,270,fill='red',outline='olivedrab')
canv.create_oval(60,290,80,310,fill='red',outline='olivedrab')

#Танк + гусли
canv.create_oval(100,540,550,640,fill='black')
#Колеса
canv.create_oval(130,560,190,620,fill='gold')
canv.create_oval(150,580,170,600,fill='red')
#-----
canv.create_oval(470,560,530,620,fill='gold')
canv.create_oval(490,580,510,600,fill='red')
#-----
canv.create_oval(210,545,300,635,fill='gold')
canv.create_oval(245,580,265,600,fill='red')
#-----
canv.create_oval(340,545,430,635,fill='gold')
canv.create_oval(375,580,395,600,fill='red')
#end Колеса

canv.create_oval(100,400,550,560,fill='green')
canv.create_oval(200,340,380,405,fill='green')
canv.create_rectangle(400,435,500,470,fill='orange')


# пушка
canv.create_polygon([340,370],[600,300],[600,310],[340,380],fill='green')
canv.create_polygon([600,300],[650,200],[670,250],[700,200],\
        [680,280],[750,240],[700,300],[800,350],[600,310],fill='red')

canv.pack()
window.mainloop()
