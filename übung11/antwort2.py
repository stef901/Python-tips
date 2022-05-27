Lesen Sie diese mit Hilfe des Pakets pandas ein
und erfüllen Sie folgende Aufgaben:
1. Machen Sie sich zunächst mit der Tabelle vertraut. Welche Daten werden abgebildet?
Welche Spalten gibt es?

Abbildung 0.1: Ein zufälliger Pfad der Länge 500, generiert durch den Funktionsaufruf
random_path(500).

2. Geben Sie für jede Ortschaft (location) die totalen Fälle (total_cases) sowie die totalen Todesfälle (total_deaths) an.
3. Fügen Sie dem in Schritt 2 berechneten Dataframe eine neue Spalte (death_rate) hinzu.
In dieser Spalte soll die Todesrate vom jeweiligen Land berechnet werden (dieser Wert
muss selber berechnet werden).
Tipp: Um einem Dataframe df eine neue Spalte address hinzufügen zu können, kann
df["address"] = values gebraucht werden, wobei values für die Werte in der Spalte
stehen.
4. (Zusatz) Geben Sie die 10 Länder mit den höchsten Todesraten zurück.
Tipp: Brauchen Sie die pandas-Funktion sort_values().

Sehen: covid-data.csv
  
 


covid 
  
