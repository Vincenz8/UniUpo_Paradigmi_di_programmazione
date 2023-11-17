# *Indice esercizi*

- [Esercizi Generatori](#esercizi-generatori)
- [Esercizi Comprehension](#esercizi-funzioni)
---
## **Esercizi Generatori**
### 1)
Definisci un generatore `mioRange(start,end,step) `
che ha 3 parametri e che produce i numeri che 
produrrebbe una chiamata di range:
```python
list(mioRange(3,7,1)) => [3,4,5,6]

list(mioRange(7,3,1)) => []

list(mioRange(3,7,2)) => [3,5]

list(mioRange(3,7,-2)) => []

list(mioRange(3,7,-1)) => []

list(mioRange(7,3,-1)) => [7, 6, 5, 4]

list(mioRange(3,7,-2)) => []

list(mioRange(7,3,-2)) => [7,5]
```

### 2) 
Definisci un generatore genFib(n) che produce i primi n numeri Fibonacci
```python
list(genFib(7)) => [1, 1, 2, 3, 5, 8, 13, 21]
for x in genFib(7):
     print(x)
```
stampa `1 1 2 3 5 8 13 21`

### 3)
Definisci un generatore `genFibInf()` che produce una enumerazione di tutti i numeri 
Fibonacci

Per testare il generatore non potete usare come nel caso precedente  
```python
for x in genFibInf():
    print(x)
```
ma potete usare la funzione next
```python
fib = genFibInf()
for x in range(1,10):
   print(next(fib))
```
### 4) 
Definisci un generatore genFibN(n) che produce una generalizzazione dei 
numeri di Fibonacci:

Ogni numero della serie e' uguale alla somma degli N numeri precedenti  
I primi N numeri sono 0,0,...,0,1   
Questo sara' un generatore per una sequenza infinita!    
Per esempio:

      genFibN(3) produce 1, 1, 2, 4, 7, 13, 24, 44, 81, 149...    
      genFibN(4) produce 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, ...    
      genFibN(2) produce i normali numeri Fibonacci      		

Di nuovo se provate a scrivere le seguenti espressioni  

      list(genFibN(4)) oppure
      [x for x in genFibN(3) if x < 100]

producete un loop infinito. Come in precedenza potete usare next:

      g5 = genFibN(5)
      next(g5)
      next(g5)
      next(g5)  

Ogni chiamata produce l'elemento successivo oppure con (il generatore) zip 
produrre una lista di coppie (ad esempio 10):

      list(zip(range(10),genFibN(3)))

il secondo elemento sara' il numero di Fibonacci.  
Questo funziona perche' zip si ferma quando la lista piu' corta (fra) dei suoi argomenti finisce.

## **Esercizi Funzioni**
### 1)
Scrivi una funzione comp che ha come parametri due funzioni, f e g, e 
ritorna una funzione che e' la composizione delle due funzioni.   
Per esempio, se chiamo `comp(f, g)` dove f e' una funzione che ritorna il quadrato del suo 
argomento, e g e' una funzione che ritorna il doppio del suo argomento, 
allora `comp(f,g)` ritorna una funzione che ritorna il quadrato del doppio 
del suo argomento.

### 2)
Considera la seguente definizione della funzione foldLeft: 

```python
def foldLeft(lis,init,fn):
   acc = init
   for x in lis:
      acc = fn(acc,x)
   return acc
```

foldLeft ha 3 parametri: 
- una lista `lis` 
- un valore iniziale di un accumulatore `acc`
- una funzione, fn che ha due parametri
  - un valore accumulatore 
  - un elemento della lista
  
  e ritorna un nuovo valore dell'accumulatore.

L'idea e' che foldLeft applica la funzione fn agli elementi di lis, accumulando
il risultato e ritornando il valore finale dell'accumulatore.  
Esempio:

```python
lis = [1,3,4,6,2]

def add (acc,x):
   return  acc+x

foldLeft(lis,0,add)
```
cosa ritorna?  
Definite una funzione fn e un valore iniziale di accumulatore init tale
che:

      foldLeft(lis,init,fn) => [2, 6, 4, 3, 1] 

cioe' il risultato e' il reverse della lista di input.

### 3)
Scrivi una funzione che accetta come argomenti una sequenza di funzioni
e un valore, applica ogni funzione a quel valore, e ritorna la funzione che
ha ritornato il valore massimo.  
(Se c'e' un pareggio, ritorna la prima
funzione che ritorna quel valore)

### 4)
Scrivi una funzione che accetta un iteratore e due funzioni booleane.    
Ritorna un iteratore di tutti gli elementi dell'iteratore di input per
cui entrambe le funzioni booleane ritornano un valore truthy.

### 5)
Scrivi una funzione che accetta due sequenze della stessa lunghezza.  
La prima sequenza rappresenta input, la seconda output.   
Crea e ritorna una funzione che dato un valore della sequenza di input, ritorna il
corrispondente output.  
Se il valore di input non c'e', ritorna None.

Per esempio:
```python
foo = makeFn([1, 2, 3, 4, 6],(7, 6, 5, 4, 3))
print(list(map(foo, range(10))))
```
Stamperebbe:
```python
[None, 7, 6, 5, 4, None, 3, None, None, None]
```
    
