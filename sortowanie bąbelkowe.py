import random
k = random.randint(17,19)
liczby = []

for i in range(k):
    m = random.randint(2,20)
    liczby.append(m)

print(liczby)
punkt = 2
przejscia = 0
while punkt != 0:
    punkt = 0
    for j in range(k-1):
        if(liczby[j] < liczby[j+1]):
            liczby[j],liczby[j+1] = liczby[j+1],liczby[j]
            punkt = 1
            przejscia+=1


print(liczby)
print(przejscia)