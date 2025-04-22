
# Wielomiany Hermite’a

def hermite(n,x):
    if(n==0):
        wartosc = 1
    elif(n==1):
        wartosc = 2*x
    else:
        wartosc = 2*x*hermite(n-1,x)-2*(n-1)*hermite(n-2,x)
    return wartosc

x = int(input("wartosc dla x: "))
dl = int(input("dlugosc ciagu: "))
for i in range(0,dl):
    print(str(hermite(i,x)),"  x^"+str(dl-i))