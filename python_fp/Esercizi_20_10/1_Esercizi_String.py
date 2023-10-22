# -*- coding: utf-8 -*-
"""

@author: Paola
"""
#%%
a = "Winter"
b = "is coming"

#%%
# crea un variabile c con valore "Winter is coming" utilizzando string 
c = a + b
print(f"c: {c}")
# crea un variabile d con valore "WinterWinterWinter"
d = a * 3
print(f"d: {d}\n")
# stampa la lunghezza di c
print(f"Lunghezza di c: {len(c)}")
# controlla se c contiene il carattere 'a'
print(f"a presente in c: {'a' in c}")
# controlla se c contiene il carattere 'g'
print(f"g presente in c: {'g' in c}")
# controlla se c contiene il carattere 'w'
print(f"w presente in c: {'w' in c}\n")
# stampa il terzo e il terzultimo carattere di c
print(f"c[2]: {c[2]} e c[13]: {c[-3]}")
# provate cosa ritorna min(c) e max(c)

print(f"min di c:{min(c)} e max di c:{max(c)}")
# stampa quanti 'i' ci sono in c
print(f"occorrenze di i in c: {c.count('i')}")

# stampa l'indice del primo 'i' in c
print(f"indice prima occorrenza di 'i' in c: {c.index('i')}")

# stampa quanti 'in' ci sono in c
print(f"occorrenze di 'in' in c: {c.count('in')}\n")


#%%
# Crea una funziona che prende una stringa come parametro, e ritorna 
# la stringa in cui i caratteri di indice dispari sono rimossi. 
# Se la stringa e' vuota ritorna None
# Attenzione le stringhe sono immutabili
# Esempio: fn2('abcdefg') = 'aceg'
def fn2(s: str) -> str|None:
    return s[::2] if len(s) > 0 else None

print(f"Stringa: prova\tstringa senza indici dispari: {fn2('prova')}")
print(f"Stringa vuota \tstringa senza indici dispari: {fn2('')}")

#%% 
# Crea una funziona come quella sopra, ma rimuove i caratteri con indice
# pari e ritorna il resto in ordine inverso. Se la lista non ha almeno 
# 2 caratteri ritorna None    
# Esempio: fn3('abcdefg') = 'fdb'   
def fn3(s: str) -> str|None:
    return s[1::2][::-1] if len(s) >= 2 else None

print(f"Stringa: prova stringa nuova: {fn3('prova')}\n")
#%%
# Da fare dopo aver introdotto le liste
# Applica le due funzioni precedenti alla stringa 'teovruoj'
# Ora crea una funzione per fare l'inverso; cioe' per mescolare due 
# stringhe della stessa lunghezza, la prima nell'ordine originale
# e la seconda al rovescio. Se gli input non sono idonei, ritorna None
# Esempio: fn4(str1,str2) = 'teovruoj'
def fn4(s1: str, s2: str) -> str|None:
    ris = ""
    
    if len(s1) == len(s2):
        for caratteri in zip(s1, s2[::-1]):
            ris += ''.join(caratteri)
        return ris
    
    else:
        return None
    
str0 = 'teovruoj'
str1 = fn2(str0)
str2 = fn3(str0)

print(str1 + "  " + str2)
print(fn4(str1, str2))

    