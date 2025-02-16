
import random

# 14 Ülesanne
inim = int(input("Sisesta inimeste arv: "))
kohad = int(input("Sisesta bussi kohtade arv: "))
bussid = inim // kohad
vbuss = inim % kohad
if vbuss:
    bussid += 1
print(f"Vaja on {bussid} bussi, viimases bussis on {vbuss if vbuss else kohad} inimest.")

# 13 Ülesanne
soo = input("Sisesta sugu (m/n): ")
if soo == "n":
    print("Sobid, pole piiranguid.")
elif soo == "m":
    vanus = int(input("Sisesta vanus: "))
    if 16 <= vanus <= 18:
        print("Sobid.")
    else:
        print("Ei sobi.")

# 12 Ülesanne
hind = float(input("Sisesta hind: "))
if hind < 10:
    soodustus = hind * 0.9
    print(f"Teil on soodustus 10%, nüüd teie hind on {soodustus:.2f}€.")
else:
    soodustus = hind * 0.8
    print(f"Teil on soodustus 20%, nüüd teie hind on {soodustus:.2f}€.")

# 11 Ülesanne
synniaasta = int(input("Sisesta sünniaasta: "))
vanus = 2025 - synniaasta
if vanus % 10 == 0:
    print("Juubel!")
else:
    print("Pole juubel.")

# 10 Ülesanne
arv1 = float(input("Sisesta esimene arv: "))
tehe = input("Sisesta tehe (+, -, *, /): ")
arv2 = float(input("Sisesta teine arv: "))
if tehe == "+":
    print(f"Vastus on {arv1 + arv2}")
elif tehe == "-":
    print(f"Vastus on {arv1 - arv2}")
elif tehe == "*":
    print(f"Vastus on {arv1 * arv2}")
elif tehe == "/":
    if arv2 != 0:
        print(f"Vastus on {arv1 / arv2}")
    else:
        print("Viga: nulliga jagamine pole lubatud.")
else:
    print("Vale tehe.")

# 9 Ülesanne
kulg1 = float(input("Sisesta esimene külg: "))
kulg2 = float(input("Sisesta teine külg: "))
if kulg1 == kulg2:
    print("Tegemist on ruuduga.")
else:
    print("Tegemist on ristkülikuga.")

#8 
import random

tooted = ["piim", "sai", "leib"]
hinnad = {toode: round(random.uniform(0.5, 5.0), 2) for toode in tooted}
kokku = 0

print("Tere tulemast poodi!")
for toode in tooted:
    if input(f"Kas soovite osta {toode}? (jah/ei): ").strip().lower() == "jah":
        kogus = int(input(f"Mitu tükki {toode} soovite?: "))
        hind = hinnad[toode] * kogus
        kokku += hind
        print(f"{toode.capitalize()}: {kogus} tk x {hinnad[toode]}€ = {hind:.2f}€")

print(f"Kokku: {kokku:.2f}€")

# 7 Ülesanne
sugu = input("Sisesta sugu (m/n): ")
pikkus = float(input("Sisesta pikkus: "))
if sugu == "m":
    if pikkus < 1.70:
        print("Lühike mees")
    elif pikkus <= 1.85:
        print("Keskmine mees")
    else:
        print("Pikk mees")
elif sugu == "n":
    if pikkus < 1.60:
        print("Lühike naine")
    elif pikkus <= 1.75:
        print("Keskmine naine")
    else:
        print("Pikk naine")


#6 ьlesanne
pikkus = float(input("Sisesta pikkus: "))
if pikkus > 1.6:
    print("Sa oled pikk")
if pikkus < 1.6:
    print("Sa oled lьhike")

# 5 Ülesanne
temperatuur = float(input("Sisesta toatemperatuur: "))
if temperatuur < 18:
    print("Soovitav toasoojus talvel")

# 4 Ülesanne
hind = float(input("Sisesta hind: "))
if hind > 700:
    soodushind = hind * 0.7
    print(f"Teil on soodustus 30%, nüüd teie hind on {soodushind:.2f}€.")

# 3 Ülesanne
laius = float(input("Sisesta laius: "))
pikkus = float(input("Sisesta pikkus: "))
pindala = laius * pikkus

print(f"Pindala on {pindala} ruutmeetrit") 
remont = input("Kas on vaja remonti teha? (jah/ei): ")
if remont.lower() == "jah":
    print("Tuleb remontida")
    rmhind = float(input("Sisesta ruutmeetri hind: "))
    print(f"Remont maksab {pindala * rmhind:.2f} eurot")
else: 
    print("Ei ole vaja remonti teha")

#2 ulesanne
nimi1 = input("Sisesta nimi: ")
nimi2 = input("Sisesta nimi: ")
nimi3 = input("Sisesta nimi: ")
nimed = {nimi1, nimi2, nimi3}

if all(nimi.isalpha() for nimi in nimed):
    if {"eldar", "adri", "nastja"} == nimed:
        print(" pinginaabrid")
else:
    print("ne pinginaabrid")

#1 ulesanne
nimi = input("Sisesta nimi: ")
if nimi.isupper() and nimi == "JUKU":
    print("Lahme kinno")
    vanus = input("Sisesta vanus: ")
    if vanus.isdigit():
        vanus = int(vanus)
        if vanus < 0 or vanus > 100:
            print("Valed andmed")
        elif vanus < 6:
            print(f"Tasuta pilet, sest oled {vanus} aastat vana")
        elif vanus <= 14:
            print(f"Lastepilet, sest oled {vanus} aastat vana")
        elif vanus <= 65:
            print(f"Tдispilet, sest oled {vanus} aastat vana")
        else:
            print(f"Sooduspilet, sest oled {vanus} aastat vana")
    else:
        print("Valesti sisestatud vanus")
