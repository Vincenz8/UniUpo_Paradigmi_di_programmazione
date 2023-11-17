def cubo_1_20() -> list[int]:
	return [(x ** 3) for x in range(1, 21)]


def cubo_1_20_div() -> list[int]:
	return [(x ** 3) for x in range(1, 21) if (x % 4) == 0]


def cubo_1_20_div2() -> list[int]:
	return [(x ** 3) for x in range(1, 21) if ((x ** 3) % 4) == 0]


def exps1(esponente: int, limite: int, base: int) -> list[int]:
	return [x for x in range(1, limite + 1) if x % (base ** esponente) == 0]
	
	
def exps2(esponente: int, limite: int, base: int) -> list[int]:
	return [(x ** esponente) for x in range(1, limite + 1) if x % base == 0]


def are_q(esponente: int, limite: int, base: int):
	return exps1(esponente, limite, base) == exps2(esponente, limite, base)


def check_are_q():
	return [(base, esponente) for base in range(2, 10) for esponente in range(2, 10) if are_q(esponente=esponente, limite=30, base=base) == False]


if __name__ == "__main__":
	print(cubo_1_20())
	print(cubo_1_20_div())
	print(cubo_1_20_div2())
	print(exps1(esponente=1, limite=10, base=2))
	print(exps2(esponente=2, limite=10, base=1))
	print(check_are_q())
	