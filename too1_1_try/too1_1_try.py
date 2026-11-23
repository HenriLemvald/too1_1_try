import math
from random import *


def ulesanne_1():
    print("Tere, maailm!")
    nimi = input("Mis on sinu nimi? ")
    print("Tere, maailm! Tervitan sind " + nimi)
    try:
        vanus = int(input("Kui vana sa oled? "))
        print("Tere, maailm! Tervitan sind " + nimi + "! Sa oled " + str(vanus) + " aastat vana.")
    except ValueError:
        print("Vanus peab olema täisarv!")


def ulesanne_2():
    vanus = 18                 # int
    eesnimi = "Jaak"           # str
    pikkus = 16.5              # float
    kas_kaib_koolis = True     # bool (teine võimalus: False)

    print(type(vanus))
    print(type(eesnimi))
    print(type(pikkus))
    print(type(kas_kaib_koolis))
    print(isinstance(vanus, int))  # True/False kontroll


def ulesanne_3():
    kommid = randint(10, 50)
    print("Laual on komme:", kommid)
    try:
        votan = int(input("Mitu kommi soovid võtta? "))
        kommid = kommid - votan
        print("Laual on nüüd komme:", kommid)
    except ValueError:
        print("Kommide arv peab olema täisarv!")


def ulesanne_4():
    try:
        umbermoot = float(input("Puu ümbermõõt (cm): "))
        labimoot = umbermoot / math.pi
        print("Puu läbimõõt on", round(labimoot, 2), "cm")
    except ValueError:
        print("Ümbermõõt peab olema arv!")


def ulesanne_5():
    try:
        n = float(input("N (m): "))
        m = float(input("M (m): "))
        diagonaal = math.sqrt(n ** 2 + m ** 2)
        print("Diagonaal on", round(diagonaal, 2), "m")
    except ValueError:
        print("N ja M peavad olema arvud!")


# 6. Loogiline viga: kiirus = aeg / teepikkus on vale.
# Kiirus = teepikkus / aeg.
def ulesanne_6():
    try:
        aeg = float(input("Mitu tundi kulus sõiduks? "))
        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
        kiirus = teepikkus / aeg  # parandatud
        print("Sinu kiirus oli " + str(kiirus) + " km/h")
    except ValueError:
        print("Sisesta arv!")
    except ZeroDivisionError:
        print("Aeg ei tohi olla 0!")


def ulesanne_7():
    try:
        a = int(input("Sisesta 1. arv: "))
        b = int(input("Sisesta 2. arv: "))
        c = int(input("Sisesta 3. arv: "))
        d = int(input("Sisesta 4. arv: "))
        e = int(input("Sisesta 5. arv: "))
        summa = a + b + c + d + e
        print("Summa:", summa)
        print("Aritmeetiline keskmine:", summa / 5)
        jagaja = int(input("Millega summa jagada? "))
        print("Täisarvuline osa:", summa // jagaja)
        print("Jääk:", summa % jagaja)
    except ValueError:
        print("Sisesta täisarv!")
    except ZeroDivisionError:
        print("Nulliga ei saa jagada!")


def ulesanne_8():
    print(r'''   @..@
  (----)
 ( \__/ )
 ^^ "" ^^''')


def ulesanne_9():
    a = 3
    b = 4
    c = 5
    p = a + b + c
    print("Kolmnurga ümbermõõt on", p)


def ulesanne_10():
    try:
        inimesi = int(input("Mitu inimest? "))
        kokku = 12.90 * 1.10
        print("Igaüks maksab", round(kokku / inimesi, 2), "€")
    except ValueError:
        print("Inimeste arv peab olema täisarv!")
    except ZeroDivisionError:
        print("Inimesi peab olema vähemalt 1!")


if __name__ == "__main__":
    for i in range(1, 11):
        print("\n--- Ülesanne", i, "---")
        globals()["ulesanne_" + str(i)]()
