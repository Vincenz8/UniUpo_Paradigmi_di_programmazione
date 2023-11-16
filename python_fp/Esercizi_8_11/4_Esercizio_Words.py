F_STRINGHE = "WordSquare.txt"


def leggi_file(directory: str, nome_file: str) -> list[str]:
    file = directory + "/" + nome_file
    stringhe = []
    with open(file=file, mode="r") as f:
        for stringa in f:
            stringhe.append(stringa.rstrip())
    return stringhe


def cerca_in_righe(parola: str, righe: list[str]):
    for i, riga in enumerate(righe):
        i_inizio = riga.find(parola)
        offset = len(parola) - 1
        if i_inizio != -1:
            return [i, i_inizio], [i, i_inizio + offset]
        else:
            j = riga[::-1].find(parola)
            if j != -1:
                i_inizio = len(riga) - j  # indice corretto dato il controllo con la stringa reversed
                return [i, i_inizio], [i, i_inizio - offset]
    return -1


def cerca_in_colonne(parola: str, righe: list[str]):
    trasposta = []
    for riga in zip(*righe):
        trasposta.append("".join(riga))
    i_colonna = cerca_in_righe(parola=parola, righe=trasposta)
    if i_colonna != -1:
        i_colonna[0][0], i_colonna[0][1] = i_colonna[0][1], i_colonna[0][0]
        i_colonna[1][0], i_colonna[1][1] = i_colonna[1][1], i_colonna[1][0]
        
    return i_colonna


def cerca_parole(parole: list[str], righe: list[str]) -> dict:
    mappa = dict()
    for parola in parole:
        i_riga = cerca_in_righe(parola=parola, righe=righe)
        if i_riga != -1:
            mappa[parola] = i_riga
        else:
            mappa[parola] = cerca_in_colonne(parola=parola, righe=righe)
    
    return mappa


if __name__ == "__main__":
    parole = ['angelico',
              'ariosto',
              'baviera',
              'camilleri',
              'cassino',
              'corsica',
              'fenoglio',
              'maglia',
              'notaio',
              'olandesi',
              'pacifico',
              'palomar',
              'parise',
              'roncalli',
              'sciascia',
              'serao']
    
    righe = leggi_file(directory=".", nome_file=F_STRINGHE)
    print(cerca_in_colonne(parola="angelico", righe=righe))
    print(cerca_in_colonne(parola="ariosto", righe=righe))
    print(cerca_parole(parole=parole, righe=righe))
