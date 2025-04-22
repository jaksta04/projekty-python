def dziesietny():
    liczba = int(input("Podaj liczbę dziesiętną do zamiany: "))
    lista = []
    wynik = liczba
    while wynik != 0:
        if(wynik % 2 == 0):
            wynik = wynik/2
            lista.append(0)
        else:
            lista.append(1)
            wynik = int(wynik/2)
    lista.reverse()
    print(lista)
        

def binarny():
    liczba = input("Podaj liczbę binarną do zamiany: (0,1)")
    lista = []
    wynik = 0
    for x in liczba:
        if(x != "0" and x != "1"):
            print("Podaj tylko 0 lub 1")
            quit()
        lista.append(int(x))
    lista.reverse()
    for k in range(0,len(lista)):
        wynik+= lista[k]*2**k
    print(wynik)




choice = int(input("1 - z dziesietnego na binarny, 2- z binarnego na dziesietny"))
if(choice == 1):
    dziesietny()
elif(choice == 2):
    binarny()