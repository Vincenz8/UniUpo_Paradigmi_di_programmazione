# *Indice esercizi*

- [Esercizi Stringhe](#esercizi-stringhe)
- [Esercizi Comprehension](#esercizi-comprehension)
---
## **Esercizi Stringhe**
Scrivi una funzione che trova una lista di parole in una matrice di lettere.

La matrice di lettere viene letta dal file di testo **WordSquare.txt**. 

La parola puo' essere orizzontale o verticale e puo' essere
in un qualsiasi orientamento 

    sinistra=> destra, destra=>sinistra, alto=>basso, basso => alto

La funzione ritorna un dizionario con chiave le parole da cercare
se la parola c'e', viene associata alla coppia di indici di inizio e
fine della parola nella matrice, se non c'e' viene associata a -1.    

1. Prima scrivere una funzione: `leggiFile(direct, nomeFile)`
che prende in input il nome della directory e quello del file nelle 
directory in cui si trovano le stringhe che rappresentano le righe
della matrice di lettere e ritorna la lista di tali stringhe.


2. Poi scrivere una funzione `cercaInRighe(parola, righe)` che prende in input 
una parola e una lista di stringhe (le righe della matrice di lettere) 
e cerca la parola nelle stringhe sia da sinistra a destra che 
da destra a sinistra e ritorna gli indici di inizio e fine della parola
e -1 se non la trova.


3. Usare la funzione precedente per definire una funzione
`cercaInColonne(parola, righe)` per cercare nelle colonne della matrice
di lettere come la precedente la parola puo' essere dall'alto in basso
o dal basso in alto e come la precedente ritorna le coordinate di inizio
e fine oppure -1.


4. Usare le 2 funzioni precedenti per definire la funzione

    `cercaParole (parole, righe) => dizionario` 
con chiavi le stringhe in parole

    e valore -1 o gli indici di inizio e fine delle parole.

Questa e' la lista delle parole:      
      
    parole = ['angelico','ariosto','baviera', 'camilleri','cassino','corsica',
              'fenoglio','maglia','notaio','olandesi','pacifico',
              'palomar','parise','roncalli','sciascia','serao']

`leggiFile(baseDir,'WordSquare.txt')` dovrebbe ritornare:

    ['olandesirap',
     'iiseraoimaa',
     'angelicosio',
     'tnvghrrcrtc',
     'oaacaeaeoai',
     'nrroilgonef',
     'ieirolagcei',
     'siosaiavaec',
     'svsirmaglia',
     'aatcramolap',
     'cboaicsaics',
    ]

## Esercizi Comprehension
1. crea una lista con il cubo dei numeri da 1 a 20 inclusi.


2. crea una lista con il cubo dei numeri divisibili per 4 da 1 a 20 inclusi.


3. crea una lista con tutti i cubi divisibili per 4 dei numeri da 1 a 20 inclusi.


4. scrivi una funziona exps1 che accetta 3 parametri:
   - esponente
   - limite
   - base
   
   e ritorna una lista con tutti i numeri da 1 al limite (inclusi) che
sono divisibili per la base elevata all'esponente

         exps1(1,10,2) =>[2, 4, 6, 8, 10]

5. scrivi una funziona exps2 che accetta 3 parametri:
   - esponente
   - limite
   - base

   e ritorna una lista con tutti i numeri da 1 al limite (inclusi) 
   elevati all'esponente, se questo e' divisibile per la base

         exps2(2,10,1) => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
6. scrivi una funzione areEq che accetta gli stessi parametri di exps1 e exps2
e ritorna True se e solo se exps1 e exps2 applicate a questi
parametri ritornano liste uguali.


7. scrivi un'espressione che chiama la funzione areEq con exp 
da 2 a 9 (inclusi), base da 2 a 9, e limit 30 e ritorna una lista di
tuple (exp, base) per tutti le coppie exp, base per cui areEq ritorna False.


8. assumendo che una tripla (stringa, booleano, lista persone) rappresenti una
persona (nome, sesso, lista dei figli) con Donna associata True e Uomo a False
ad esempio:

        paola =("Paola", True,[])
        andrea =("Andrea", True,[paola])
        peter =("Peter", False,[])
        giulia =("Giulia", True, [paola, peter])
        persone = [paola, peter, giulia]

    ottenere:

   - la lista delle persone il cui nome inizia con “P”
   - la lista delle coppie (nome madre, nome figlia/o)


9. Riscrivi la funzione righeColonne che prende in input una lista 
di stringhe `[r1,...,rn]` tutte della stessa lunghezza m, e ritorna 
la lista di stringhe `[c1,...,cm]` dove  `ci=r1[i]r2[i]....rn[i]`
usando la Comprehension.