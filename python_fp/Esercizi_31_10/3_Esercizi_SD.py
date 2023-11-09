# Cosa ritornano queste espressioni. Provate a capirlo prima di eseguire!


# zip(range(5),range(5,10))

# list(zip(range(5),range(5,10)))

# list(zip("spam","eggs","spam"))

# ' and '.join(['one','two','three'])

# ord('a')

# chr(97)

# chr(ord('a') + 1)

# chr(ord('b') - 1)

# data questa definizione di fn:
def fn(a, b=7):
    print(a, b)


# cosa viene stampato quando valuti queste chiamate?
# fn(1,2,3)
fn(1, 2)
fn(1)
# fn()8
fn(a=3)
fn(b=1, a=2)
# fn(b=3)
# fn(7,a=5)
fn(*[1, 3])
fn([1, 3])
# fn(3,c=5)
fn(2, **{'b': 5})

# che valori hanno le variabili a,b e c dopo questi assegnamenti?
a, b, c = [1, 2, 3]
a, b, c = "foo"

a, b, *c = "foobar"

a, *b, c = range(4)
print(c)

# %%Eserczio 1
# Scrivi una funzione che prende una stringa e ritorna True 
# se e' un palindrome. Ignorate i caratteri che non sono lettere
# del'alfabeto e il test deve essere case-insensitive.
# isPal('A man, a plan, a canal: Panama!') => True
# isPal('Ettore evitava le madame lavative e rotte.') => True
# isPal('Bolton') => false
import re
import string


def is_pal(s: str) -> bool:
    s = s.translate(s.maketrans("", "", string.punctuation + string.whitespace)).lower()
    return s == s[::-1]


print(is_pal('A man, a plan, a canal: Panama!'))
print(is_pal('Ettore evitava le madame lavative e rotte.'))
print(is_pal('Bolton'))

# %%Eserczio 2
# Scrivere una funzione righeColonne che prende in input una lista 
# di stringhe [r1,...,rn] tutte della stessa lunghezza m, e ritorna 
# la lista di stringhe [c1,...,cm] dove  ci=r1[i]r2[i]....rn[i]
# Se

ls = ['olandesirap',
      'iiseraoimaa',
      'angelicosio',
      'tnvghrrcrtc',
      'oaacaeaeoai',
      'nrroilgonef',
      'ieirolagcei',
      'siosaiavaec',
      'svsirmaglia',
      'aatcramolap',
      'cboaicsaics'
      ]


def righe_colonne(s: list[str]) -> list[str]:
    ris = []
    stringa = ""
    for i in range(len(ls[0])):
        for j in range(len(ls[0])):
            stringa += s[j][i]
        ris.append(stringa)
        stringa = ""

    return ris


print(righe_colonne(ls))
# righeColonne(ls) deve ritornare


# ['oiatonissac',
# 'linnareivab',
# 'asgvariosto',
# 'neegcorsica',
# 'drlhaioarri',
# 'eairellimac',
# 'socragaaams',
# 'iioceogvgoa',
# 'rmsroncalli',
# 'aaitaeeeiac',
# 'paocificaps']

# SUGGERIMENTO: Come potete ottenere dalla lista inziale una sequenza
# che raggruppi i caratteri che stanno in una specifica colonna??

# %% Eserczio 3

# Assumendo di avere una lista di triple (stringa, booleano, lista persone) in cui
# una tripla rappresenti una persona (nome, sesso, lista dei figli) con Donna associata 
# True e Uomo a False ad esempio:

paola = ("Paola", True, [])
andrea = ("Andrea", True, [paola])
peter = ("Peter", False, [])
giulia = ("Giulia", True, [paola, peter])
persone = [paola, peter, giulia]


# scrivere due funzioni che ritornano rispettivamente
# 1) la lista delle persone il cui nome inizia con un certo carattere (parametro)
# 2) la lista delle coppie (nome madre, nome figlia/o)  
def cerca(persone: list, carattere: str) -> list:
    return [p for p in persone if p[0].startswith(carattere)]


def mamma_figli(persone: list) -> list:
    coppie = []
    for p in persone:
        if (p[1] and len(p[2]) > 0):
            for figlio in p[2]:
                coppie.append((p[0], figlio[0]))

    return coppie


print(cerca(persone, "P"))
print(mamma_figli(persone))
