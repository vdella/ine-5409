from math import exp, sin, cos
          

def f(n): 
    return exp(n) + n         # a = -1, b = 0
    #return exp(n) - 2*cos(n)  # a = 0, b = 2
    #return exp(n)*sin(n) - 1  # a = 0, b = 1

def metodo(a,b): 
    #return (a+b)/2
    return a - (f(a)*(b-a) / (f(b)-f(a)))


a = -1 #modificar esses valores de acordo
b = 0  #com o intervalo desejado
xm = metodo(a,b)
fa = f(a)
fb = f(b)
fxm = f(xm)
erro = 10**-2
i = 0

while (abs(fxm) > erro):
    xm = metodo(a,b)
    fxm = f(xm)
    if fa*fxm < 0:
        b = xm
        fb = fxm
    else:
        a = xm
        fa = fxm
    i = i + 1
print(i)
print(xm)
print(fxm)
