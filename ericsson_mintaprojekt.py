import turtle as t
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
    t.screensize(800, 800, "#778899") # szurke
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
    t.write(szoveg, align="center", font=("Courier", 36, "bold"))

def torles(y):
    t.fillcolor("#778899") # vilagoskek
    teglalap(-400, y+50, 800, 50)

def hatter():
    # eg
    t.fillcolor("#00BFFF") # vilagoskek
    teglalap(-400, 400, 800, 370)
    # fu
    t.fillcolor("#006000") # sotetzold
    teglalap(-400, 30, 800, 230)

def cim():
    t.pencolor("#483D8B") # sotetkek
    kiiras("Országkitalálós játék", 330)

def fa():
    # fatorzs
    t.fillcolor("#533118") # sotetbarna
    teglalap(-30, 0, 60, 150)
    # lombkorona
    t.fillcolor("#228B22") # zold
    kor(0, 150, 180)

def alma_lerak(x, y):
    t.fillcolor("#C94020") # piros
    kor(x, y, 20)

def alma_torol(x, y):
    t.fillcolor("#228B22") # zold
    kor(x, y, 20)

alma_helyek = [(-110, 110), (0, 170), (110, 140), (-90, 220), (50, 260), (-30, 30), (60, 60)]
beallitasok()
hatter()
cim()
fa()
for alma_hely in alma_helyek:
    alma_lerak(*alma_hely)

felso_sor = -300
also_sor = -360

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
    torles(felso_sor)
    kiiras(megfejtes, felso_sor)
    torles(also_sor)
    kiiras("".join(hibak), also_sor)
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

# Játék vége: kiírjuk kitakarás nélkül a megfejtést.
torles(felso_sor)
kiiras(feladvany, felso_sor)
torles(also_sor)
# Nyertünk vagy vesztettünk?
if 7 <= len(hibak):
    kiiras("Vége! :(", also_sor)
else:
    torles(also_sor)
    kiiras("Szuper! :)", also_sor)
# Ez azért kell, hogy ne záruljon be az ablak:
t.done()
