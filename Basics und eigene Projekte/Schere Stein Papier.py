import random
schere = "Schere"
stein = "Stein"
papier = "Papier"
Spiel = input('''Wenn du das Spiel beginnen willst, schreibe "Ja", wenn nicht, schreibe "Nein"
Willst du das Spiel beginnen? ''')
Punkte = 10

if Spiel.lower() == "ja":
    print('Zum beenden des Spiels erreiche entweder 20 Punkte, verliere alle deine Punkte oder schreibe "Stop"\nViel Spaß :D')
    while Punkte > 0 or Punkte <= 20:
        print(f"Du hast {Punkte} Punkte!")
        if Punkte == 0:
            break
        elif Punkte == 20:
            break
        
        gegner = random.randint(1,3)
        if gegner == 1:
            gegner = "Schere"
        elif gegner == 2:
            gegner = "Stein"
        elif gegner == 3:
            gegner = "Papier"
            
        antwort = input("Wollen sie Schere, Stein oder Papier wählen? ")    
        if antwort.lower() == schere.lower():
            antwort = "Schere"
        elif antwort.lower() == stein.lower():
            antwort = "Stein"
        elif antwort.lower() == papier.lower():
            antwort = "Papier"
        elif antwort.lower() == "stop":
            print("Noch einen schönen Tag :D")
            break
        else:
            print("Das verstehe ich nicht")
    
        if antwort == "Schere" and gegner == "Schere":
            print("Es ist ein unentschieden")
        elif antwort == "Schere" and gegner == "Stein":
            print("Du hast leider verloren")
            Punkte -= 1
        elif antwort == "Schere" and gegner == "Papier":
            print("""Du hast gewonnen!
Herzlichen Glückwunsch""")
            Punkte += 1
    
        if antwort == "Stein" and gegner == "Stein":
            print("Es ist ein unentschieden")
        elif antwort == "Stein" and gegner == "Papier":
            print("Du hast leider verloren")
            Punkte -= 1
        elif antwort == "Stein" and gegner == "Schere":
            print("""Du hast gewonnen!
Herzlichen Glückwunsch""")
            Punkte += 1
    
        if antwort == "Papier" and gegner == "Papier":
            print("Es ist ein unentschieden")
        elif antwort == "Papier" and gegner == "Schere":
            print("Du hast leider verloren")
            Punkte -= 1
        elif antwort == "Papier" and gegner == "Stein":
            print("""Du hast gewonnen!
Herzlichen Glückwunsch""")
            Punkte += 1
elif Spiel.lower() == "nein":
    print("Schade, noch einen schönen Tag")
else:
    print("Das verstehe ich leider nicht")