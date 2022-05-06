import statistics
import csv

csvpassagierfrequenz = open("passagierfrequenz.csv", "r")
file = csv.DictReader(csvpassagierfrequenz, delimiter=';')

DTV = []
DWV = []
DNWV = []
Bahnhof_Haltestelle = []

for col in file:    
    
    DTV.append(col["DTV"])    
    DWV.append(col["DWV"])    
    DNWV.append(col["DNWV"])    
    Bahnhof_Haltestelle.append(col["Bahnhof_Haltestelle"])

    DTV = list(map(int, DTV))
    DWV = list(map(int, DWV))
    DNWV = list(map(int, DNWV))
    
    print("Mittelwert DTV: ", statistics.mean(DTV))
    
    print("Mittelwert DWV: ", statistics.mean(DWV))
    
    print("Mittelwert DNWV: ", statistics.mean(DNWV))
    
    print("Median DTV: ", statistics.median(DTV))
    
    print("Median DWV: ", statistics.median(DWV))
    
    print("Median DNWV: ", statistics.median(DNWV))
    
    kleinsterDTV = min( DTV)
    
    posmin =   DTV.index(kleinsterDTV)
    grössterDTV = max(  DTV)
    
    posmax =   DTV.index(grössterDTV)
    
    print("Kleinster DTV: ", Bahnhof_Haltestelle[posmin])
    print("Grösster DTV: ", Bahnhof_Haltestelle[posmax])
