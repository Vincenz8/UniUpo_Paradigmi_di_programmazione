
#%%
# Scrivi una funzione che accetta una lista di numeri
# e ritorna true se e solo se (sse) tutti i numeri sono distinti 
# Esempi: distinti([1,2,3,4]) -> True
#         distinti([1,2,3,2]) -> False
def distinti(numeri: list[int]) -> bool:
    return len(set(numeri)) == len(numeri)

print(distinti([1,2,3,4]))
print(f"{distinti([1,2,3,2])}\n")

#%%
# Scrivi una funzione che ritorna il numero cifre di un intero
# Esempi: cifre(0) -> 1
#         cifre(1003) => 4
import math

def cifre(n: int) -> int:
    return 1 if (n == 0) else (int(math.log10(abs(n))) + 1)

print(cifre(0))
print(f"{cifre(1003)}\n")10000
#%% 
# Scrivi una funziona che accetta un int e ritorna il numero
# di zeri consecutivi con cui finisce.
# Esempi: lessZero(123) -> 0
#         lessZero(1200086000) -> 3
#         lessZero(-100) -> 2
#         lessZero(0) = 1
def lessZero(n: int) -> int:
    return len(n.__str__()) - len(n.__str__().rstrip("0"))

print(lessZero(123))
print(lessZero(1200086000))
print(lessZero(-100))
print(f"{lessZero(0)}\n")

#%%
# Scrivi una funziona che conta la frequenza di tutte la parole in una stringa
# input: stringa con parole separati da spazi 
# output: dizionario con coppie (parola, numero di occorenza)  
# Se str="mele  rab  dfgghh mele arance   ddfsfs arance"
# freq(str) => {'mele': 2, 'rab': 1, 'dfgghh': 1, 'arance': 2, 'ddfsfs': 1}
from collections import Counter

def freq(s: str) -> dict:
    return dict(Counter(s.split()))

print(freq("mele  rab  dfgghh mele arance   ddfsfs arance"))

#%%
# Crea una funzione che ha due parametri, assumi che siano stringhe.
# Ritorna una tupla con due stringhe che sono le due stringhe di input
# con il loro primo carattere swappato (l'uno con l'altro).
# Se uno dei due parametri e' una stringa vuota ritorna None
# Esempio: fn1('foo','bar') ritorna ('boo','far')
def fn1(s1: str, s2: str) -> tuple|None:
    if s1 == '' or s2 == '':
        return None
    else:
        temp = s1[0]
        s1 = s2[0] + s1[1:]
        s2 = temp + s2[1:]
        
        return s1, s2
    
print(fn1('foo','bar'))
        
#%%
# Data una stringa di lunghezza divisibile per 3, ritorna una tupla con 
# il primo terzo, il terzo di mezzo, e l'ultimo terzo della stringa.
# Se la lunghezza non e' divisibile per 3, oppure e' 0, ritorna None
# Esempio: fn('abcdef') => ('ab','cd','ef')
#    st = st + 'x' * ((3-len(st)) % 3)
def fn(s: str) -> tuple|None:
    if (len(s) % 3) == 0 and len(s) != 0:
        i = len(s) // 3
    
        return s[:i], s[i:(2*i)], s[(2*i):]
    
    else:
        return None

print(f"{fn('abcdef')}\n")

#%%   
# Scrivere una funzione che prende un parametro intero e una stringa produce
# lo shift della stringa a destra con ingresso di caratteri bianchi e perdita
# dei caratteri che eccedono la lunghezza
# Esempi:  spostaDx(6,'questaeraunastringa') ->  '      questaeraunas' 
#          spostaDx(2,'domani') ->  '  doma'
def spostaDx(n: int, s: str) -> str:
    return f"{' ' * n}{s[:(len(s) - n)]}"

print(spostaDx(2,'domani'))
print(spostaDx(6,'questaeraunastringa'))

#%%   
# Scrivere una funzione che prende un parametro intero e una stringa produce
# lo shift della stringa a sinistra con ingresso di caratteri bianchi e perdita
# dei caratteri che eccedono la lunghezza
# Esempi:  spostaSx(6,'questaeraunastringa') ->  'eraunastringa      ' 
#          spostaSx(2,'domani') ->  'mani  '

def spostaSx(n: int, s: str) -> str:
    return f"{s[n:]}{' ' * n}"

print(spostaSx(6,'questaeraunastringa'))
print(spostaSx(2,'domani'))
