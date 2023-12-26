from operator import itemgetter

def piu_alto(people: list[tuple]) -> tuple:
	# return max(people, key=lambda x: x[3])
	return max(people, key=itemgetter(3))


def piu_basso(people: list[tuple]) -> tuple:
	return min(people, key=itemgetter(3))


def ultimo_lessicografico(people: list[tuple]) -> tuple:
	return max(people, key=itemgetter(0))


def altezza_sort(people: list[tuple]) -> tuple:
	return sorted(people, key=itemgetter(3), reverse=True)


def p_televisivo_sort(people: list[tuple]) -> tuple:
	return sorted(people, key=itemgetter(2))


def cognome_nome_sort(people: list[tuple]) -> tuple:
	return sorted(people, key=itemgetter(1, 0))


def televisivo_cognome_nome_sort(people: list[tuple]) -> tuple:
	return sorted(people, key=itemgetter(2, 1, 0))

# sort generico
# def generico_sort(people: list[tuple], indici: tuple) -> tuple:
#	return sorted(people, key=itemgetter(*indici))


def main():
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
	
	print(f"Piu alto: {piu_alto(people)}")
	print(f"Piu alto: {piu_basso(people)}")
	print(f"Ultimo lessicografico per nome:{ultimo_lessicografico(people)}")
	print(f"Ordinati per altezza: {altezza_sort(people)}")
	print(f"ordinati per programma: {p_televisivo_sort(people)}")
	print(f"Ordinati per cognome e poi nome: {cognome_nome_sort(people)}")
	print(f"Ordinati per programma televisivo, poi cognome ed infine nome: {televisivo_cognome_nome_sort(people)}")


if __name__ == "__main__":
	main()
	