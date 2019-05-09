import turtle as t
import time
import random

"""
    Ericsson Skool foglalkozás, 2019 május 11
    Kódminta a fő projekthez: akasztófás játék a Turtle modullal

    Lényegében egy parancssorban is játszható, egyszerű input-output játék
    grafikus dekor-elemekkel. A résztvevők projektjeiben mások lesznek a
    feladványok, és más lesz a grafika is.
"""

# A Turtle modulhoz tartozó kódrészeket kiszervezzük függvényekbe, hogy a fő
# részben a játékmenetre koncentrálhassunk.

def beallitasok():
    t.screensize(600, 600, "#778899") # szurke
    t.shape("circle")
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.shapesize(3, 3)

def teglalap(balfelso_x, balfelso_y, szelesseg, magassag):
    t.goto(balfelso_x, balfelso_y)
    t.begin_fill()
    t.goto(balfelso_x + szelesseg, balfelso_y)
    t.goto(balfelso_x + szelesseg, balfelso_y - magassag)
    t.goto(balfelso_x, balfelso_y - magassag)
    t.goto(balfelso_x, balfelso_y)
    t.end_fill()

def kor(kozeppont_x, kozeppont_y, sugar):
    t.goto(kozeppont_x, kozeppont_y - sugar)
    t.begin_fill()
    t.circle(sugar)
    t.end_fill()

def kiiras(szoveg, y):
    t.goto(0, y)
    t.write(szoveg, align="center", font=("Courier", 30, "bold"))

def torles(y):
    t.fillcolor("#778899") # vilagoskek
    teglalap(-400, y+30, 800, 30)

def hatter():
    # eg
    t.fillcolor("#00BFFF") # vilagoskek
    teglalap(-300, 300, 600, 270)
    # fu
    t.fillcolor("#006000") # sotetzold
    teglalap(-300, 30, 600, 130)

def cim():
    t.pencolor("#483D8B") # sotetkek
    kiiras("Országkitalálós játék", 205)

def fa():
    # fatorzs
    t.fillcolor("#533118") # sotetbarna
    teglalap(-20, 0, 40, 100)
    # lombkorona
    t.fillcolor("#228B22") # zold
    kor(0, 90, 120)

def alma_lerak(x, y):
    t.fillcolor("#C94020") # piros
    kor(x, y, 15)

def alma_torol(x, y):
    t.fillcolor("#228B22") # zold
    kor(x, y, 15)

alma_helyek = [(-80, 70), (-10, 100), (60, 70), (-70, 140),
    (40, 160), (-20, 10), (50, 20)]
beallitasok()
hatter()
cim()
fa()
for alma_hely in alma_helyek:
    alma_lerak(*alma_hely)

# Most jöhetnek az adatok. A feladványokat külön plain text fájlból hívjuk be.
with open("feladvanyok.txt", encoding = "utf8") as file:
    feladvanyok = file.read().splitlines()
abece = list('AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ')

#Feladvány generálása a feladványlistából.
feladvany = random.choice(feladvanyok)
megfejtes = ""
for x in feladvany:
    if x in abece:
        megfejtes += "_"
    else:
        megfejtes += x
nemvoltmeg = abece
hibak = []

# És most jön a játék fő ciklusa:
while not feladvany == megfejtes and len(hibak) < 7:
    torles(-150)
    kiiras(megfejtes, -150)
    torles(-200)
    kiiras("".join(hibak), -200)
    tipp = ""
    # Minden körben tippet kérünk a játékostól:
    while not tipp in nemvoltmeg:
        tipp = t.textinput("TIPP", "Tipp: ").upper()
    # Kiértékeljük a tippet:
    if tipp in feladvany:
        megfejtes_uj = ""
        for i in range(len(feladvany)):
            if feladvany[i] == tipp:
                megfejtes_uj += tipp
            else:
                megfejtes_uj += megfejtes[i]
        megfejtes = megfejtes_uj
    else:
        alma_torol(*alma_helyek[len(hibak)])
        hibak.append(tipp)
    nemvoltmeg.remove(tipp)

# Játék vége: nyertünk vagy vesztettünk?
if 7 <= len(hibak):
    torles(-360)
    kiiras("Vége! :(", -360)
else:
    torles(-360)
    kiiras("Szuper! :)", -360)
# Akár nyertünk, akár vesztettünk, kiírjuk kitakarás nélkül a megfejtést:
torles(-300)
kiiras(feladvany, -300)
# Ez azért kell, hogy ne záruljon be az ablak:
t.done()
