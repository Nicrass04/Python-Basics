import random

cherry = "🍒" #Gewinn: (2) 0.5x  (3) 1.0x    Chance: 50%
apple = "🍎" #Gewinn: (2) 1.0x  (3) 1.5x     Chance: 30%
banana = "🍌" #Gewinn: (2) 2.0x  (3) 3.0x     Chance: 14%
mais = "🌽" #Gewinn: (2) 5.0x  (3) 7.5x       Chance: 5%
mushroom = "🍄" #Gewinn: (2) 10.0x  (3) 25.0x Chance: 1%

Geld = float(1000)
print(f'Du hast momentan {Geld:,}€')
while Geld > 0:
    print('Falls du keine Lust mehr zum spielen hast, schreibe eine negative Zahl')
    if Geld < 0:
        break
    einsatz = float(input("Mit wie viel Geld möchtest du spielen?\n> "))
    if einsatz <= 0:
        break
    elif einsatz != int:
        print("Das verstehe ich nicht")
    while einsatz < 1:
        print("Du musst mindestens 1€ setzen!")
        einsatz = float(input("Mit wie viel Geld möchtest du spielen?\n> "))
    while (einsatz > Geld):
        print(f"Das kannst du dir nicht leisten!\nDu hast nur {Geld}€")
        einsatz = float(input("Mit wie viel Geld möchtest du spielen?\n> "))
    Geld -= einsatz
    slot1 = random.randint(1,100)

    if slot1 >= 1 and slot1 <= 50:
        slot1 = "🍒"
    elif slot1 > 50 and slot1 <= 80:
        slot1 = "🍎"
    elif slot1 > 80 and slot1 <= 94:
        slot1 = "🍌"
    elif slot1 > 94 and slot1 <= 99:
        slot1 = "🌽"
    elif slot1 == 100:
        slot1 = "🍄"

    slot2 = random.randint(1,100)

    if slot2 >= 1 and slot2 <= 50:
        slot2 = "🍒"
    elif slot2 > 50 and slot2 <= 80:
        slot2 = "🍎"
    elif slot2 > 80 and slot2 <= 94:
        slot2 = "🍌"
    elif slot2 > 94 and slot2 <= 99:
        slot2 = "🌽"
    elif slot2 == 100:
        slot2 = "🍄"

    slot3 = random.randint(1,100)

    if slot3 >= 1 and slot3 <= 50:
        slot3 = "🍒"
    elif slot3 > 50 and slot3 <= 80:
        slot3 = "🍎"
    elif slot3 > 80 and slot3 <= 94:
        slot3 = "🍌"
    elif slot3 > 94 and slot3 <= 99:
        slot3 = "🌽"
    elif slot3 == 100:
        slot3 = "🍄"

#┏  ┓  ┛ ┗  ┃ ━ (Slot Deko)
    print(f"\n┏━━━━━━━━━━━━━━━━━━┓\n┃   [MAGIC SLOT]   ┃\n┃━━━━━━━━━━━━━━━━━━┃\n┃  ____ ____ ____  ┃\n┃ | {slot1} | {slot2} | {slot3} | ┃  O\n┃  ‾‾‾‾ ‾‾‾‾ ‾‾‾‾  ┃  ┃\n┃                  ┃  ┃\n┃━━━━━━━━━━━━━━━━━━┃━━┛\n┃    ┏━━━━━━━━┓    ┃\n┃    ┗━━━━━━━━┛    ┃\n┗━━━━━━━━━━━━━━━━━━┛\n")

#Vergleiche, um zu schauen, ob gewonnen oder nicht
    if slot1 == slot2 != slot3 and slot1 == "🍒":
        einsatz *= 0.5
        Geld += einsatz
    elif slot1 == slot2 == slot3 and slot1 == "🍒":
        einsatz = einsatz
        Geld += einsatz

    if slot1 == slot2 != slot3 and slot1 == "🍎":
        einsatz = einsatz
        Geld += einsatz
    elif slot1 == slot2 == slot3 and slot1 == "🍎":
        einsatz *= 1.5
        Geld += einsatz  
        
    if slot1 == slot2 != slot3 and slot1 == "🍌":
        einsatz *= 2
        Geld += einsatz
    elif slot1 == slot2 == slot3 and slot1 == "🍌":
        einsatz *= 3
        Geld += einsatz
        
    if slot1 == slot2 != slot3 and slot1 == "🌽":
        einsatz *= 5
        Geld += einsatz
    elif slot1 == slot2 == slot3 and slot1 == "🌽":
        einsatz *= 7.5
        Geld += einsatz

    if slot1 == slot2 != slot3 and slot1 == "🍄":
        einsatz *= 10
        Geld += einsatz
    elif slot1 == slot2 == slot3 and slot1 == "🍄":
        einsatz *= 25
        Geld += einsatz
    elif slot1 != slot2:
        Geld += 0
    print(f"Du hast momentan {Geld:,}€")
