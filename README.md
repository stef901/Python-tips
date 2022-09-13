# Python 

Python

matplotlib.pyplot.axhline
(https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.axhline.html)
Quindi oggi parleremo del laboratorio di pensiero computazionale eth
così abbiamo
ETH Computational Thinking Labs: istruzioni generali
Compiti in aula
Rapporti: sintassi Markdown
Linguaggio di programmazione: interprete python3
Esegui python3 dalla riga di comando
Scrivi python3
Strumento di collaborazione: GitHub
Scrivi ed esegui script python3 in vscode
Strumento di collaborazione: script di condivisione dal vivo in vscode
Strumento di collaborazione: scrivi script python3 in Overleaf
Strumento di collaborazione: senza installazione: esegui python3 in CTL-code-expert
Strumento di collaborazione: Scrivi ed esegui Matlab
Dove ottenere aiuto
Compiti in aula
Riceverai un invito per ogni incarico via e-mail. Accetta il compito e scegli tra i gruppi esistenti, se desideri unirti a uno dei gruppi esistenti, oppure creane uno nuovo. Dopo l'accettazione, troverai un nuovo repository nel tuo account GitHub personale. Vedi sotto se non hai ancora un account GitHub.

Compiti in aula in vscode
Avvia vscode. Per gestire i compiti in classe, fai clic sul simbolo github nella barra delle applicazioni di sinistra, accedi a github. Per confermare le modifiche, fai clic sull'icona del controllo del codice sorgente (Crtl-G). Lascia sempre un messaggio per i tuoi impegni.

Compiti in aula su GitHub
Una volta accettato un compito, troverai un nuovo repository nel tuo GitHub personale. Non è necessario utilizzare vscode per modificare i codici, puoi anche modificarli direttamente su GitHub o clonare la directory in una directory locale e modificare da lì utilizzando un altro software. Assicurati di confermare le modifiche.

Compiti in classe sul retro
Puoi creare un nuovo progetto su Overleaf dal tuo compito su GitHub come descritto di seguito. Sfortunatamente, i file che terminano con .py non vengono visualizzati come file di testo in Overleaf, a meno che non crei un nuovo file.py su Overleaf e incolli il contenuto dello script python al suo interno. Gli script Python che si trovano sul tuo Overleaf possono essere eseguiti tramite lo strumento online esperto di codice CTL.

Rapporti: sintassi Markdown
Tutte le informazioni su un progetto diverso dallo script stesso, come obiettivi, idee, risultati dovrebbero essere raccolte nel file report.md che si trova nell'assegnazione di github. Tutti i membri del gruppo devono essere abilitati alla modifica di report.md. i file md vengono interpretati utilizzando la sintassi Markdown su GitHub. Un rapido riferimento alla sintassi di Markdown è disponibile su https://www.markdownguide.org/cheat-sheet/

Linguaggio di programmazione: interprete python3
Installare
windows, macos, linux: scarica da https://docs.conda.io/en/latest/miniconda.html

Miniconda è un programma di installazione minimo gratuito per conda. È una piccola versione bootstrap di Anaconda che include solo conda, Python, i pacchetti da cui dipendono e un piccolo numero di altri pacchetti utili, inclusi pip, zlib e pochi altri. Usa il comando conda install per installare pacchetti aggiuntivi come numpy o matplotlib.

Esegui python3 dalla riga di comando
Esegui uno script python3 dalla riga di comando
windows: cerca e apri il prompt dei comandi. macos e linux: apre la finestra del terminale. Passa (cd) alla directory contenente il tuo script o fornisci il percorso completo del tuo script. accedere

python3 [yourscript.py] [argomenti]
Esci da python3 interattivo tramite quit(). Visualizza il valore di uscita tramite

python3 [yourscript.py] [argomenti]; eco $?
Scrivi python3
Cheat sheet: https://cheatography.com/tag/-python/, https://www.pythoncheatsheet.org/

Usa gli argomenti della riga di comando nel tuo script python3
importazione sist
...
# il numero di argomenti della riga di comando è: len(sys.argv)-1
n = int(sys.argv[1])
Struttura generale dello script Python che può essere importato o riutilizzato ed eseguito anche dalla riga di comando
importazione sist

def miafunzione1 (a):
    print("il primo (intero) argomento è "+str(a))
    
def miafunzione2 (a,b):
    print("il primo (intero) argomento è "+str(a))
    print("Il secondo argomento (mobile) è "+str(b))

# esegui le seguenti operazioni se chiamato dalla riga di comando

se len(sys.argv)-1==1:
    a = int(sys.argv[1])
    mia funzione1(a)
elif len(sys.argv)-1==2:
    a = int(sys.argv[1])
    b = float(sys.argv[2])
    miafunzione2(a,b)
Esci dal tuo script python3 con valore 13
importazione sist
...
sys.exit(13)
Ritorna ed esci con un valore
importazione sist

def mia funzione (a):
    print("il primo (intero) argomento è "+str(a))
    b = 2*a
    ritorno b
    
# esegui le seguenti operazioni se chiamato dalla riga di comando

se len(sys.argv)-1==1:
    a = int(sys.argv[1])
    b = mia funzione(a)
    sys.exit(int(b))
Controlla se myfile esiste all'interno del tuo script python
import os.path
...
if os.path.isfile("myfile"):
  ...
Leggere e salvare la matrice con valori interi da e nel file tic-tac-toe.txt
importa numpy come np
data = np.genfromtxt("tic-tac-toe.txt", dtype=np.int)
dati[0,0]=1
np.savetxt("tic-tac-toe.txt", data, fmt="%d")
Crea file grafico mygraphics.png
importa matplotlib.pyplot come plt
# supponendo che myarray (un array) porti la tua immagine
plt.imshow(myarray)
plt.savefig('mygraphics.png')
Introduzione alle classi Python e relative
https://www.youtube.com/watch?v=ZDa-Z5JzLYM

Strumento di collaborazione: GitHub
Crea il tuo account github personale su www.github.com

Scrivi ed esegui pyth
