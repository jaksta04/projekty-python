def sortowanie(list):
    zamiana = 1
    while zamiana != 0:
        zamiana = 0
        for k in range(len(list)-1):
            if(list[k] > list[k+1]):
                list[k],list[k+1] = list[k+1],list[k]
                zamiana = 1
    return list

def wyszukiwanie_binarne(list,liczba):
    print(list)
    znaleziona = False
    początek = 0
    koniec = len(list)
    while znaleziona != True:
        srodek = int((początek + koniec)/2)
        if(list[srodek] == liczba):
            print("Liczba znaleziona("+str(liczba)+")","miejsce:",srodek+1)
            znaleziona = True
            break
        else:
            if(liczba > list[srodek]):
                początek = srodek
            else:
                koniec = srodek


list = []
plik_open = open("tekst_wej.txt","w")
wpisz = 1
while wpisz != 0:
    wpisz = int(input("Podaj liczbe do pliku: "))
    plik_open.write(str(wpisz)+"\n")
    list.append(wpisz)

list.pop(-1)
sortowanie(list)
plik_open2 = open("wyniki.txt","w")
for i in list:
    plik_open2.write(str(i)+"\n")


liczba = int(input("Podaj szukaną liczbe: "))
if(liczba in list):
    wyszukiwanie_binarne(list,liczba)
else:
    print("Na liście nie ma twojej liczby")

