# *Indice esercizi*

- [Min, max, e sort](#min-max-e-sort)
- [Reduce, map e filter](#reduce-map-e-filter)
- [Funzioni ricorsive](#funzioni-ricorsive)

## *Min, max e sort*
People e' una lista di tuple. Ogni tupla rappresenta un personaggio.    
Gli elementi della tupla sono (cognome, nome, programma televisivo, altezza)

```python
people = [
          ("Joey", "Tribbiani", "Friends", 185),
          ("Ralph", "Kramden", "The Honeymooners", 180),
          ("Ross", "Geller", "Friends", 180),
          ("Monica", "Geller", "Friends", 175),
          ("Spencer", "Cogswell", "The Jetsons", 170),
          ("Chandler", "Bing", "Friends", 175),
          ("Elroy", "Jetson", "The Jetsons", 140),
          ("Astro", "Jetson", "The Jetsons", 60),
          ("Fred", "Flintstone", "The Flintstones", 175),
          ("Barney", "Rubble", "The Flintstones", 150),
          ("Betty", "Rubble", "The Flintstones", 165),
          ("Bambam", "Rubble", "The Flintstones", 45),
          ("Alice", "Kramden", "The Honeymooners", 165),
          ("Ed", "Norton", "The Honeymooners", 170),
          ("Trixie", "Norton", "The Honeymooners", 165),
          ("George", "Jetson", "The Jetsons", 175),
          ("Jane", "Jetson", "The Jetsons", 170),
          ("Phoebe", "Buffay", "Friends", 175),
          ("Pebbles", "Flintstone", "The Flintstones", 30),
          ("Judy", "Jetson", "The Jetsons", 160),
          ("Cosmo", "Spacely", "The Jetsons", 140),
          ("Wilma", "Flintstone", "The Flintstones", 170),
          ("Rachel", "Green", "Friends", 170),
          ]
```
### 1)
Trova il personaggio piu' alto, specificare la funzione sia con una lambda
espressione che con un operatore predefinito di Python.

### 2)
Trova il personaggio piu' basso.

### 3)
Trova il personaggio col nome che è l'ultimo in ordine lessicografico.

### 4)
Trova il personaggio che sarebbe elencato per primo in un elenco telefonico

### 5)
Crea una lista con gli elementi di people ordinati per altezza dal
piu' alto al piu' basso.

### 6)
Crea una lista con gli elementi di people ordinati per programma televisivo.

### 7)
Crea una lista con gli elementi di people ordinati per cognome poi nome.

### 8)
Crea una lista con gli elementi di people ordinati per programma televisivo,
poi cognome, poi nome.

## *Reduce, map e filter*
### 1)
Scrivere la funzione fattoriale(n) usando la funzione reduce (senza iterazione o ricorsione).

### 2)
Scrivi una list comprehension equivalente a:
```python
list(map(lambda x: x**3,(filter(lambda x: x % 5 != 0, range(3,20,3)))))
```

### 3)
Usando map e zip scrivere una funzione `diff(seq)` che data una sequenza di interi genera la sequenza delle differenze degli elementi adiacenti.  
Ad esempio

```python
diff([3,2,7,4,4)) => [1,-5,3,0]
```

### 4)
Scrivere una funzione `contaVocali(str)` che ritorna una quintupla (nA,nE,nI,nO,nU) 
contenente il numero di a, e, i,o ,u  della stringa.     
Usare la funzione foldLeft

```python
def foldLeft(lis, init, fn):
     acc = init
     for x in lis:
         acc = fn(acc,x)
     return acc
```

Ad esempio 
```python
contaVocali("abeiarc") ==>  (2,1,1,0,0)
```

## *Funzioni ricorsive*

### 1)
Scrivere una funzione ppTree per stampare questi alberi in notazione infissa. 
Per esempio:

`ppTree(optree1) => (7+4)*(7-4)`

Puo' essere utile sapere che la funzione print prende un argomento end, che 
specifica l'ultimo carattere da stampare.   
Il default e' `\n`; se non si vuole che vada a capo si puo' specificare print('foo', end='').    
Provate a eseguire 

    print('foo','bar')
    print('foo') seguito da print('bar') e
    print('foo',end=' ') seguito da print('bar')

### 2)

Scrivere una funzione che prende un albero tree e un intero n, mette 
in una lista il contenuto dei nodi di livello n di tree
```python
depthN(optree1,1)  =>  ['+', '-']
depthN(optree1,2)  =>  [7, 4, 7, 4]
```

    optree3 = Tree('*',
                  Tree('+',
                       Tree(7,
                            Tree('*',
                                 Tree('+',
                                      Tree(7),
                                      Tree(4)),
                                 Tree('-',
                                      Tree(8),
                                      Tree(6)
                                      )
                                 )
                            ),
                       Tree(4)),
                  Tree('-',
                       Tree(8),
                       Tree(6))
                  )

### 3)
Scrivere una funzione `maxProf` che prende un albero t e un intero n, e ritorna
la massima profondita' di n (distanza dalla radice di t) se n e' un dato dell'albero
Se n non compare in t ritorna -1.

    tree = Tree( 5,
                  Tree( 9,
                       Tree(7,
                            Tree( 7,
                                 Tree( 4,
                                      Tree(9),
                                      None
                                      ),
                                 Tree(6)
                                 ),
                        Tree(4)
                        ),
                     Tree(4,
                       None,
                       Tree(6)
                       )
                     ),
                  None
            )

    maxProf(tree,6) => 4
    maxProf(tree,11) => -1
    maxProf(tree,4) => 4

### 4)
Scrivi una funzione eleva(a,b) che calcola a**b ricorsivamente.

    a ** 0 = 1  eleva(a, 0) = 1 
    eleva(a, b) = eleva(a,b2) * eleva(a, b2)) dove b2 = b // 2 e b e' pari
    a ** b = (a ** b2) * (a ** b2)  se b2 = b // 2 e  b e' pari
    a ** b = (a ** b2) * (a ** b2) * a  se b2 = b // 2 e b e' dispari

### 5)
Scrivi una definizione ricorsiva foldLeftRic della seguente funzione foldLeft.
```python
def foldLeft(lis,init,fn):
    acc = init
    for x in lis:
        acc = fn(acc,x)
    return acc


lis = [1,3,4,6,2]

def add (acc,x):
    return  acc+x
```
`foldLeftRic(lis,0,add) => 16`