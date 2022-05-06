(a) random.randrange(1, 100, 2)

Liefert eine beliebige ganze Zahl von 1 bis 100 mit Schritt 2
Datentyp: int 


(b) random.choice([2, 3, 4, 5, 9, 10])
# Dies ist gleichbedeutend mit np.random.randint(2, 3, 4, 5, 9, 10)
# druckt einen Zufallswert aus der Liste
# 2 
(c) random.randint(0, 100)
# Erzeugt eine Zufallszahl zwischen
# einem gegebenen positiven Bereich
# Random number between 0 and 100 is 83

(d) random.uniform(50, 200)
# 50 ist die Untergrenze der zu erzeugenden Zufallszahl an.
# 200 ist die Obergrenze der zu erzeugenden Zufallszahl an.

# Rückgabe : Gibt die generierte Fließkommazufallszahl zwischen der Untergrenze und der Obergrenze zurück.
# Die generierte Zufallszahl zwischen 50 und 200 ist: 53.85236821595338

(e) random.sample([11, 12, 13, 14, 15, 16, 17], 3)
Syntax : random.sample(Folge, k)

Parameter:
Sequenz: Kann eine Liste, ein Tupel, eine Zeichenkette oder eine Menge sein.
k: Ein Integer-Wert, der die Länge einer Stichprobe angibt.

Rückgabe: k Länge neue Liste von Elementen, die aus der Sequenz ausgewählt wurden.
# [12, 13, 17]

(f) random.random()

Syntax : random.random()

Parameter : Diese Methode akzeptiert keine Parameter.

Rückgabe : Diese Methode gibt eine zufällige Fließkommazahl zwischen 0 und 1 zurück.

