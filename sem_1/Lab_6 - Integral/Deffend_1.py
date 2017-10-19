a = float(input("Введите нижний предел интгрирования(a): "))
b = float(input("Введите верхний предел интегрирования(b): "))
eps = float(input("Введите точность(eps): "))
def funct(x):
    return (x*x)
def methodP(n):
    h1=abs((b-a)/(n))
    summa=0;k=n
    for i in range(k):
        x=a+h1*i
        if i%2==0:
            summa+=2*funct(x)
        else:
            summa+=4*funct(x)

    Ploshad = (h1/3)*(funct(a)+summa+funct(b))
    return(Ploshad)
              
h = 1; Integral=methodP(h)
while abs(methodP(2*h)-methodP(h))>abs(eps):
     Integral = methodP(h)
     h*=2
print("Значение интеграла по методу параболы: ","{:11.9}".format(Integral),
      "\nПри количестве разбиений: ",h)
