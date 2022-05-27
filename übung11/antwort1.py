# Ziel dieser Aufgabe ist es, eine Funktion random_path zu schreiben. Diese Funktion erhält als
Parameter eine Zahl und generiert dann einen zufälligen Pfad dieser Länge. Die Funktion soll
den Pfad dann mit Hilfe des Moduls matplotlib anzeigen. Der Pfad soll bei den Koordinaten
(0, 0) beginnen und dann in jedem weiteren Schritt die x- und y-Koordinaten so verändern,
dass der jeweilge Wert entweder um 1 verkleinert wird, gleich bleibt oder um 1 erhöht wird.
Daraus ergeben sich dann 8 verschiedene Richtungen, die zufällig in jedem Schritt generiert
werden.
Tipps:
1. Erstellen Sie zwei Listen. Eine enthält alle x-Koordinaten, die andere alle y-Koordinaten.
2. Verwenden Sie die Funktion randint des Moduls random.
3. Sie können den Pfad anzeigen, indem sie die Funktion plot des Moduls matplotlib.pyplot
verwenden.
4. Die Funktion plot erhält als ersten Parameter alle x-Koordinaten und als zweiten Parameter alle y-Koordinaten in Form einer Liste.
