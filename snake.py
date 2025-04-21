import os
import random
import msvcrt
from time import sleep

def wyswietlanie_mapy(gracz_x,gracz_y,punkty,wyniki):
    os.system('cls')
    print("punkty:",punkty,"                              Tabela wyników",wyniki)
    for i in range(20):
        for j in range(20):
            print(mapa[i][j],end=" ")
        print()
    print("współrzędne: x",gracz_x,"y",gracz_y)


def jablko():
    jabl_x = random.randint(2,18)
    jabl_y = random.randint(2,18)
    if(mapa[jabl_y][jabl_x] == "."):
        mapa[jabl_y][jabl_x] = "@"
    else:
        jablko()

def ustawienie(lista,mapa):
    mapa[lista[0][1]][lista[0][0]] = "."



def rozgrywka():
    punkty = 0
    wyniki = []
    czas = 0.12
    czy_zrobil_ruch = False
    gracz_x = random.randint(2,18)
    gracz_y = random.randint(2,18)
    mapa[gracz_y][gracz_x] = "O"
    jablko()
    wyswietlanie_mapy(gracz_x,gracz_y,punkty,wyniki)
    kordy = []
    kordy.append([gracz_x,gracz_y])
    print(kordy)
    kierunek_x = 0
    kierunek_y = 0
    while True:
        if(msvcrt.kbhit() == True):
            klawisz = msvcrt.getwch()
                
            if(klawisz == "w"):
                kierunek_x = 0
                kierunek_y = -1 
            elif(klawisz == "s"):
                kierunek_x = 0
                kierunek_y = 1
            elif(klawisz == "a"):
                kierunek_x = -1
                kierunek_y = 0
            elif(klawisz == "d"):
                kierunek_x = 1
                kierunek_y = 0
            else:
                kierunek_x = 0
                kierunek_y = 0

        
        gracz_x += kierunek_x
        gracz_y += kierunek_y
        if(mapa[gracz_y][gracz_x] == "."):
            mapa[gracz_y][gracz_x] = "O"
            ustawienie(kordy,mapa)
            kordy.pop(0)
            kordy.append([gracz_x,gracz_y])
            czy_zrobil_ruch = True

                    
        elif(mapa[gracz_y][gracz_x] == "@"):
            punkty +=10
            czas -= 0.01
            mapa[gracz_y][gracz_x] = "O"
            kordy.append([gracz_x,gracz_y])
            ustawienie(kordy,mapa)
            jablko()
            czy_zrobil_ruch = True


        else:
            if(czy_zrobil_ruch == True):
                if(punkty > 0):
                    wyniki.append(punkty)
                punkty = 0
                czas = 0.12
                for i in range(1,19):
                    for j in range(1,19):
                        mapa[i][j] = "."
                kordy.clear()
                gracz_x = random.randint(3,17)
                gracz_y = random.randint(3,17)
                mapa[gracz_y][gracz_x] = "O"
                kordy.append([gracz_x,gracz_y])
                jablko()
                czy_zrobil_ruch = False
                kierunek_x = 0
                kierunek_y = 0
        wyswietlanie_mapy(gracz_x,gracz_y,punkty,wyniki)
        print(kordy)
        if(czas < 0.06):
            czas = 0.06
        sleep(czas)

mapa = [ 
         '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '| . . . . . . . . . . . . . . . . . . | '.split(' '),
         '_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '.split(' ')
]

rozgrywka()