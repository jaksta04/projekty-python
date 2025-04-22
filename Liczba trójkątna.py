
# Liczba trójkątna

def triangle(n):
    if n< 1:
        return 0
    if n==1:
        return 1
    else:
        return n+triangle(n - 1)

n = int(input("ile elemetow w podstawie: "))
print("Ilosc wszystkich elementow dla",n,"w podstawie: ",triangle(n))