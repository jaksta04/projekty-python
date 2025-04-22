import os

def wyswietl_plansze():
    os.system("cls")
    print("    [0]"+"  [1]"+"  [2] ")
    m = 0
    for kolumna in plansza:
        print("["+str(m)+"]",end="  ")
        for wiersz in kolumna:
            print(wiersz,end="    ")
        print("\n")
        m+=1
    

def postaw_symbol(plansza,x,y,symbol):
    plansza[y][x] = symbol

def czy_obszar_zajety(plansza,wsp_x,wsp_y):
    zajety = False
    if(plansza[wsp_y][wsp_x] != "."):
        zajety = True
    return zajety

def sprawdz_czy_gracz_wygral(plansza,nr_gracza):
    wygran = False
    if(nr_gracza == 1):
        symbol = "X"
    else:
        symbol = "O"


    if(plansza[0][0]==plansza[0][1]==plansza[0][2]==symbol):
        wygran = True
    elif(plansza[1][0]==plansza[1][1]==plansza[1][2]==symbol):
        wygran = True
    elif(plansza[2][0]==plansza[2][1]==plansza[2][2]==symbol):
        wygran = True
    elif(plansza[0][0]==plansza[1][0]==plansza[2][0]==symbol):
        wygran = True
    elif(plansza[0][1]==plansza[1][1]==plansza[2][1]==symbol):
        wygran = True
    elif(plansza[0][2]==plansza[1][2]==plansza[2][2]==symbol):
        wygran = True
    elif(plansza[0][2]==plansza[1][1]==plansza[2][0]==symbol):
        wygran = True
    elif(plansza[2][2]==plansza[1][1]==plansza[0][0]==symbol):
        wygran = True
    return wygran

plansza = [[".",".","."],[".",".","."],[".",".","."]]


print("Gra kółko i krzyżyk")
n = input("Naciśnij spację aby pokazać planszę ")
if(n == " "):
    wyswietl_plansze()
    for gra in range(5):
        print("Gracz 1/ symbol X")
        gracz = 1
        print("Podaj współrzedne")
        x = int(input("kolumna: "))
        y = int(input("wiersz: "))
        symbol = "X"
        if(czy_obszar_zajety(plansza,x,y) == True):
            print("\nTen obszar jest zajęty \n")
        else:
            postaw_symbol(plansza,x,y,symbol)
        if(sprawdz_czy_gracz_wygral(plansza,gracz) == True):
            print("\n Wygrywa gracz 1 (X)")
            wyswietl_plansze()
            quit()
        wyswietl_plansze()

        print("Gracz 2/ symbol O")
        gracz = 2
        print("Podaj współrzedne")
        x = int(input("kolumna: "))
        y = int(input("wiersz: "))
        symbol = "O"
        if(czy_obszar_zajety(plansza,x,y) == True):
            print("\nTen obszar jest zajęty \n")
        else:
            postaw_symbol(plansza,x,y,symbol)
        if(sprawdz_czy_gracz_wygral(plansza,gracz) == True):
            print("\n Wygrywa gracz 2 (O)")
            wyswietl_plansze()
            quit()
        wyswietl_plansze()
else:
    quit()

print("Remis, koniec gry")
input()