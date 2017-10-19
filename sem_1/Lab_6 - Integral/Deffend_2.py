from math import*
def y(x):
    return x*x
a=float(input('Введите нижний предел интеграла\n'))
b=float(input('Введите верхний предел интеграла\n'))
eps=float(input('Введите точность нахождения площади\n'))
h=b-a
i=1
S1=h*(y(a)+y(b))/2
S2=h/2*((y(a)+y(b))/2+y(a+h/2))
while abs(S2-S1)>eps:
    i*=2
    h=h/2
    S1=S2
    S=0
    for j in range(1,2*i):
        S+=y(a+j*h/2)
    S2=h/2*((y(a)+y(b))/2+S)
print('Площадь по методу трапеций равна','{:7.3f}'.format(S1),', Количетсво отрезков',i)
