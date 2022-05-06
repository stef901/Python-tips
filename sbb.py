
Sehen Sie sich den Datensatz aus der Datei passagierfrequenz.csv genauer an. Die Daten
stammen von dem Open Data Angebot der SBB und können unter https://data.sbb.ch/pages/home/
heruntergeladen werden. Die Bezeichnungen sind wie folgt definiert:
• DTV = Durchschnittlicher täglicher Verkehr (Montag bis Sonntag) im Jahr 2018.
• DWV = Durchschnittlicher werktäglicher Verkehr (Montag bis Freitag) im Jahr 2018.
• DNWV = Durchschnittlicher nicht-werktäglicher Verkehr (Samstage, Sonntage, Feiertage) im Jahr 2018.
Schreiben Sie ein Programm, welches die Datei einliest. Dann sollen mithilfe des Moduls statistics
die folgenden statistischen Auswertungen durchgeführt werden:
• Berechnen Sie den arithmetischen Mittelwert von den Werten aus den Spalten DTV, DWV,
DNWV.
• Ermitteln Sie den Median der Werte aus den Spalten DTV, DWV, DNWV.
• Finden Sie den Bahnhof mit dem kleinsten und dem grössten Wert DTV.

import statistics
import csvpassagierfrequenz = open("passagierfrequenz.csv", "r")
file = csv.DictReader(passagierfrequenz, delimiter=';')

DTV = []DWV = []DNWV = []Bahnhof_Haltestelle = []

for col in file:    
    
    DTV.append(col["DTV"])    
    DWV.append(col["DWV"])    
    DNWV.append(col["DNWV"])    
    Bahnhof_Haltestelle.append(col["Bahnhof_Haltestelle"])
    int DTV = list(map(int, DTV))
    int DWV = list(map(int, DWV))
    int DNWV = list(map(int, DNWV))
    
    print("Mittelwert DTV: ", statistics.mean(int DTV))
    
    print("Mittelwert DWV: ", statistics.mean(int DWV))
    
    print("Mittelwert DNWV: ", statistics.mean(int DNWV))
    
    print("Median DTV: ", statistics.median(int DTV))
    
    print("Median DWV: ", statistics.median(int DWV))
    
    print("Median DNWV: ", statistics.median(int DNWV))
    
    kleinsterDTV = min(int DTV)
    
    posmin = int DTV.index(kleinsterDTV)
    grössterDTV = max(int DTV)
    
    posmax = int DTV.index(grössterDTV)
    
    print("Kleinster DTV: ", Bahnhof_Haltestelle[posmin])
    print("Grösster DTV: ", Bahnhof_Haltestelle[posmax])
