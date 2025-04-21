from random import randint
print("Zaczynasz niezwykłą przygodę ale wcale nie będzie łatwo!")
akthp = 350
maxhp = 350
zloto = 50
poziom = 1
zdobyte_doswiadczenie = 0
ilosc_mikstur_leczniczych = 0
mała = 0
duża = 0


while True:
    if (zdobyte_doswiadczenie >= 0 and zdobyte_doswiadczenie <= 300):
        twoje_obrażenia = randint(38, 45)
        hp_przeciwnika = randint(250, 270)
        zdobycz = randint(20, 28)
        doswiadczenie = randint(100, 120)
    elif (zdobyte_doswiadczenie > 300 and zdobyte_doswiadczenie <= 700):
        poziom = 2
        maxhp = 400
        twoje_obrażenia = randint(44, 54)
        hp_przeciwnika = randint(280, 330)
        zdobycz = randint(30, 35)
        doswiadczenie = randint(150, 180)
    elif (zdobyte_doswiadczenie > 700 and zdobyte_doswiadczenie <= 1300):
        poziom = 3
        maxhp = 430
        twoje_obrażenia = randint(58, 66)
        hp_przeciwnika = randint(350, 430)
        zdobycz = randint(35, 45)
        doswiadczenie = randint(220, 230)
    elif (zdobyte_doswiadczenie > 1300 and zdobyte_doswiadczenie <= 2000):
        poziom = 4
        maxhp = 460
        twoje_obrażenia = randint(65, 74)
        hp_przeciwnika = randint(430, 470)
        zdobycz = randint(45, 55)
        doswiadczenie = randint(260, 280)
    elif (zdobyte_doswiadczenie > 2000 and zdobyte_doswiadczenie <= 3000):
        poziom = 5
        maxhp = 500
        twoje_obrażenia = randint(75, 90)
        hp_przeciwnika = randint(500, 600)
        zdobycz = randint(55, 60)
        doswiadczenie = randint(290, 300)
    elif (zdobyte_doswiadczenie > 3000 and zdobyte_doswiadczenie <= 7000):
        poziom = 6
        maxhp = 530
        twoje_obrażenia = randint(92, 107)
        hp_przeciwnika = randint(620, 700)
        zdobycz = randint(60, 65)
        doswiadczenie = randint(350, 400)
    elif (zdobyte_doswiadczenie > 7000 and zdobyte_doswiadczenie < 8000):
        poziom = 7
        maxhp = 560
        twoje_obrażenia = randint(92, 107)
        hp_przeciwnika = randint(800,850 )
        zdobycz = randint(62, 68)
        doswiadczenie = randint(350, 400)
        print("Niedługo ostateczny pojedynek, kup mikstury!")
    elif (zdobyte_doswiadczenie >= 8000):
        poziom = 8
        maxhp = 700
        twoje_obrażenia = randint(102, 128)
        hp_przeciwnika = 6000

    if(zdobyte_doswiadczenie >= 8000):
        print("Przed tobą walka z bossem!")
        akthp = maxhp
        choice = 3
    else:
        hp = round(akthp/maxhp*100)
        if(hp <= 0):
            hp = 0
        hp = str(hp)
        choice = input("""Tutaj wybierasz co dalej robić:"""+"  "+"hp:"+hp+"%"+"""
            1-(regeneracja) 2-(kup miksture) 3-(łatwa walka) 4-(trudna walka) 5-(sprawdź statystyki gracza): """)
        if(choice.isdigit()):
            choice = int(choice)

    if(choice == 1):
        cena = randint(15, 22)
        print("Będziesz mógł odpocząć, ale nie za darmo!  Należność:",cena)
        choice_1 = input("Płacisz wędrowcze? (Tak/Nie)").lower()
        if(choice_1 == "tak"):
            if(zloto >= cena):
                if(akthp <= maxhp):
                    akthp = maxhp
                    print("Posiadasz pełne zdrowie")
                    zloto -= cena
                    continue
            else:
                print("Nie masz wystarczająco dużo pieniędzy!")
        elif(choice_1 == "nie"):
            print("Będziesz żałował!")
        else:
            print("Skup się!")
    if(choice == 2):
        print("""Duża mikstura przywraca 50% zdrowia(koszt 45 monet)
Mała mikstura przywraca 25% zdrowia(koszt 25 monet)""" )
        print("Twoja ilość  złota wynosi:",zloto)
        choice2_1 = input("Którą wybierasz? (Duża)(Mała),aby wrócić wpisz (q) ").lower()
        if(choice2_1 == "duża"):
            if(zloto >= 45):
                print("Kupiłeś dużą miksturę.")
                zloto = zloto - 45
                ilosc_mikstur_leczniczych += 1
                duża += 1
                continue
            else:
                print("Posiadasz za mało złota!")
                continue
        elif(choice2_1 == "mała"):
            if (zloto >= 25):
                print("Kupiłeś mała miksturę.")
                zloto = zloto - 25
                ilosc_mikstur_leczniczych += 1
                mała += 1
                continue
            else:
                print("Posiadasz za mało złota!")
                continue
        elif(choice2_1 == "q"):
            continue


    if(choice == 3):
        if(zdobyte_doswiadczenie < 8000):
            print("Czas na walkę! wybrałeś łatwego przeciwnika")
        print("Atakujesz pierwszy")
        while True:
            choice3_1 = input("1-(atak) 2-(mikstura): ")
            if(choice3_1.isdigit()):
                choice3_1 = int(choice3_1)
            if(choice3_1 == 1):
                kryt = randint(1, 4)
                if (kryt == 2):
                    wartosc_kryt = twoje_obrażenia+ int(0.7*twoje_obrażenia)
                    print("Cios krytyczny")
                    hp_przeciwnika = hp_przeciwnika - wartosc_kryt
                else:
                    twoje_obrażenia = twoje_obrażenia
                    hp_przeciwnika = hp_przeciwnika - twoje_obrażenia

                if (hp_przeciwnika == 0 or hp_przeciwnika < 0):
                    print("Zabiłeś przeciwnika.", "Twoje hp wynosi:", akthp)
                    if(zdobyte_doswiadczenie >= 8000):
                        print("Huraa! Jesteś teraz mistrzem")
                        print("Statystyki gry:")
                        print("")
                        print("Aktualne zdrowie: ", akthp)
                        print("Max hp: ", maxhp)
                        print("Twoje złoto: ", zloto)
                        print("Poziom bohatera: ", poziom)
                        print("Zdobyte doświadczenie: ", zdobyte_doswiadczenie)
                        print("Liczba mikstur: ", ilosc_mikstur_leczniczych)
                        quit()
                    else:
                        zloto += zdobycz
                        zdobyte_doswiadczenie += doswiadczenie
                        print("Zdobyłeś",zdobycz,"złota i ",doswiadczenie,"doświadczenia")
                        break
                if (zdobyte_doswiadczenie >= 8000):
                    obrażenia_przeciwnika = randint(47, 54)
                else:
                    obrażenia_przeciwnika = randint(36, 43)
                akthp = akthp - obrażenia_przeciwnika
                if (akthp == 0 or akthp < 0):
                    if (zdobyte_doswiadczenie >= 8000):
                        print("Nie udało Ci się zostać prawdziwym gladiatorem.")
                        print("Statystyki gry:")
                        print("")
                        print("Aktualne zdrowie: ", akthp)
                        print("Max hp: ", maxhp)
                        print("Twoje złoto: ", zloto)
                        print("Poziom bohatera: ", poziom)
                        print("Zdobyte doświadczenie: ", zdobyte_doswiadczenie)
                        print("Liczba mikstur: ", ilosc_mikstur_leczniczych)
                        quit()
                    else:
                        print("Poniosłeś klęskę!")
                        break
                print("Aktualnie masz",akthp,"hp","Twój przeciwnik ma",hp_przeciwnika,"hp")

            elif(choice3_1 == 2):
                print("Posiadasz",ilosc_mikstur_leczniczych,"mikstur",  "małe:",mała,  "duże:",duża)
                if(mała > 0 and duża > 0):
                    choice3_2 = str(input("Jakiej chcesz użyć? (Duża/Mała): ")).lower()
                    if(choice3_2 == "duża"):
                        ilosc_mikstur_leczniczych -= 1
                        duża -= 1
                        akthp += round(1/2*maxhp)
                        print("Uzupełniłeś hp i teraz wynosi:",akthp)
                        continue
                    if (choice3_2 == "mała"):
                        ilosc_mikstur_leczniczych -= 1
                        mała -= 1
                        akthp += round(1/4 * maxhp)
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                if(mała > 0 and duża == 0):
                    choice3_3 = str(input("Chcesz użyć małej? (Tak/Nie): ")).lower()
                    if(choice3_3 == "tak"):
                        ilosc_mikstur_leczniczych -= 1
                        mała -= 1
                        akthp += round(1/4 * maxhp)
                        if(akthp > maxhp):
                            akthp = maxhp
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                    elif(choice3_3 == "nie"):
                        continue
                if(mała == 0 and duża > 0):
                    choice3_4 = str(input("Chcesz użyć dużej? (Tak/Nie): ")).lower()
                    if(choice3_4 == "tak"):
                        ilosc_mikstur_leczniczych -= 1
                        duża -= 1
                        akthp += round(1/2  * maxhp)
                        if (akthp > maxhp):
                            akthp = maxhp
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                    elif (choice3_4 == "nie"):
                        continue
            else:
                print("Skup się! Zostałeś zaatakowany")
                obrażenia_przeciwnika = randint(36, 43)
                akthp = akthp - obrażenia_przeciwnika
                print("Aktualnie masz", akthp, "hp", "Twój przeciwnik ma", hp_przeciwnika, "hp")
                if (akthp == 0 or akthp < 0):
                    print("Poniosłeś klęskę!")
                    break
    if (choice == 4):
        print("Uważaj, będzie trudniej!")
        print("Atakujesz pierwszy")
        hp_przeciwnika = hp_przeciwnika+ int(1/2*hp_przeciwnika)
        while True:
            choice3_1 = input("1-(atak) 2-(mikstura): ")
            if(choice3_1.isdigit()):
                choice3_1 = int(choice3_1)
            if (choice3_1 == 1):
                kryt = randint(1, 4)
                if (kryt == 2):
                    wartosc_kryt = twoje_obrażenia + int(0.7 * twoje_obrażenia)
                    print("Cios krytyczny")
                    hp_przeciwnika = hp_przeciwnika - wartosc_kryt
                else:
                    twoje_obrażenia = twoje_obrażenia
                    hp_przeciwnika = hp_przeciwnika - twoje_obrażenia

                if (hp_przeciwnika == 0 or hp_przeciwnika < 0):
                    print("Zabiłeś przeciwnika.", "Twoje hp wynosi:", akthp)
                    zloto += zdobycz
                    zdobyte_doswiadczenie += doswiadczenie
                    print("Zdobyłeś", zdobycz, "złota i ", doswiadczenie, "doświadczenia")
                    break
                obrażenia_przeciwnika = randint(55, 66)
                akthp = akthp - obrażenia_przeciwnika
                if (akthp == 0 or akthp < 0):
                    print("Zostałeś pokoanany, wróć silniejszy!")
                    break
                print("Aktualnie masz", akthp, "hp", "Twój przeciwnik ma", hp_przeciwnika, "hp")
            elif(choice3_1 == 2):
                print("Posiadasz", ilosc_mikstur_leczniczych, "mikstur", "małe:", mała, "duże:", duża)
                if (mała > 0 and duża > 0):
                    choice3_2 = str(input("Jakiej chcesz użyć? (Duża/Mała): ")).lower()
                    if (choice3_2 == "duża"):
                        ilosc_mikstur_leczniczych -= 1
                        duża -= 1
                        akthp += round(1/2 * maxhp)
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                    if (choice3_2 == "mała"):
                        ilosc_mikstur_leczniczych -= 1
                        mała -= 1
                        akthp += round(1/4 * maxhp)
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                if(mała > 0 and duża == 0):
                    choice3_3 = str(input("Chcesz użyć małej? (Tak/Nie): ")).lower()
                    if (choice3_3 == "tak"):
                        ilosc_mikstur_leczniczych -= 1
                        mała -= 1
                        akthp += round(1/4 * maxhp)
                        if (akthp > maxhp):
                            akthp = maxhp
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                    elif (choice3_3 == "nie"):
                        continue
                if(mała == 0 and duża > 0):
                    choice3_4 = str(input("Chcesz użyć dużej? (Tak/Nie): ")).lower()
                    if (choice3_4 == "tak"):
                        ilosc_mikstur_leczniczych -= 1
                        duża -= 1
                        akthp += round(1/2 * maxhp)
                        if (akthp > maxhp):
                            akthp = maxhp
                        print("Uzupełniłeś hp i teraz wynosi:", akthp)
                        continue
                    elif (choice3_4 == "nie"):
                        continue
            else:
                print("Skup się! Zostałeś zaatakowany")
                obrażenia_przeciwnika = randint(55, 66)
                akthp = akthp - obrażenia_przeciwnika
                print("Aktualnie masz", akthp, "hp", "Twój przeciwnik ma", hp_przeciwnika, "hp")
                if (akthp == 0 or akthp < 0):
                    print("Poniosłeś klęskę!")
                    break

    if(choice == 5):
        print("Aktualne zdrowie: ",akthp)
        print("Max hp: ",maxhp)
        print("Twoje złoto: ",zloto)
        print("Poziom bohatera: ",poziom)
        print("Zdobyte doświadczenie: ",zdobyte_doswiadczenie)
        print("Liczba mikstur: ",ilosc_mikstur_leczniczych)


    if(choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5):
        print("Skup się!")

