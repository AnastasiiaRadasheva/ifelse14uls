#14 �lesanne
inim = int(input("Sisesta inimeste arv: "))
kohad = int(input("Sisesta bussi kohtade arv: "))
bussid = inim // kohad
vbuss = inim % kohad
if vbuss:
    bussid += 1
print(f"Vaja on {bussid} bussi, viimases bussis on {vbuss if vbuss else kohad} inimest")

#13 �lesanne
soo = input("Sisesta sugu: ")
if soo == "n":
    print("Sobid, pole piiranguid")
if soo == "m":
    vanus66 = int(input("Sisesta vanus: "))
    if 16 <= vanus66 <= 18:
        print("Sobid")
    else:
        print("Ei sobi")

#12 �lesanne
hind = float(input("Sisesta hind: "))
if hind < 10:
    soodustus1 = hind - (hind * 0.1)
    print(f"Teil on soodustus 10%, n��d teie hind on {soodustus1}")
if hind > 10:
    soodustus2 = hind - (hind * 0.2)
    print(f"Teil on soodustus 20%, n��d teie hind on {soodustus2}")

#11 �lesanne
synniaasta = int(input("Sisesta s�nniaasta: "))
vanus = 2025 - synniaasta
if vanus % 10 == 0:
    print("Juubel")
else:
    print("Pole juubel")

#10 �lesanne
arv1 = float(input("Sisesta esimene arv: "))
tehe = input("Sisesta tehe: ")
arv2 = float(input("Sisesta teine arv: "))
if tehe == "+":
   print(f"Vastus on {arv1 + arv2}")
elif tehe == "-":
   print(f"Vastus on {arv1 - arv2}")
elif tehe == "*":
   print(f"Vastus on {arv1 * arv2}")
elif tehe == "/":
   print(f"Vastus on {arv1 / arv2}")
else:
   print("Vale tehe")

#9 �lesanne
kulg1 = float(input("Sisesta esimene k�lg: "))
kulg2 = float(input("Sisesta teine k�lg: "))
if kulg1 == kulg2:
    print("Ruut")
else:
    print("Ristk�lik")
#7 �lesanne
sugu = input("Sisesta sugu (m/n): ")
pikkus = float(input("Sisesta pikkus: "))
if sugu == "m":
        if pikkus < 1.70:
            print("L�hike mees")
        elif pikkus <= 1.85:
            print("Keskmine mees")
        else:
            print("Pikk mees")
if sugu == "n":
        if pikkus < 1.60:
            print("L�hike naine")
        elif pikkus <= 1.75:
            print("Keskmine naine")
        else:
            print("Pikk naine")

#6 �lesanne
pikkus = float(input("Sisesta pikkus: "))
if pikkus > 1.6:
    print("Sa oled pikk")
if pikkus < 1.6:
    print("Sa oled l�hike")

#5 �lesanne
temperatuur = float(input("Sisesta toatemperatuur: "))
if temperatuur < 18:
    print("Soovitav toasoojus talvel")

#4 �lesanne
hind = float(input("Sisesta hind: "))
if hind > 700:
    soodushind = hind - (hind * 0.3)
    print(f"Teil on soodustus 30%, n��d teie hind on {soodushind}")

#3 �lesanne
laius = float(input("Sisesta laius: "))
pikkus = float(input("Sisesta pikkus: "))
pindala = laius * pikkus

print(f"Pindala on {pindala} ruutmeetrit") 
remont = input("Kas on vaja remonti teha? ")
if remont == "jah":
    print("Tuleb remontida")
    rmhind = float(input("Sisesta ruutmeetri hind: "))
    print(f"Remont maksab {pindala * rmhind} eurot")
else: 
    print("Ei ole vaja remonti teha")

#2 �lesanne
nimi1 = input("Sisesta nimi: ")
nimi2 = input("Sisesta nimi: ")
nimi3 = input("Sisesta nimi: ")
nimed = {nimi1, nimi2, nimi3}

if all(nimi.isalpha() for nimi in nimed):
    if {"eldar", "adri", "nastja"} == nimed:
        print("Super, vy pinginaabrid")
else:
    print("Oneet, vy ne pinginaabrid")

#1 �lesanne
nimi = input("Sisesta nimi: ")
if nimi.isupper() and nimi == "JUKU":
    print("L�hme kinno")
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
            print(f"T�ispilet, sest oled {vanus} aastat vana")
        else:
            print(f"Sooduspilet, sest oled {vanus} aastat vana")
    else:
        print("Valesti sisestatud vanus")
