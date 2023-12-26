from functools import reduce


def fattoriale(n: int) -> int:
	return reduce(lambda n1, n2: n1 * n2, range(2, n + 1))


def c_equivalente() -> list:
	return [x ** 3 for x in range(3, 20, 3) if (x % 5) != 0]


def diff(seq: list):
	return [x for x in map(lambda x: x[0] - x[1], zip(seq, seq[1:]))]


def main():
	print(f"Fattoriale di 5: {fattoriale(5)}")
	print(f"Comprehension equivalente: {c_equivalente()}")
	print(f"Diff([3,2,7,4,4]): {diff([3, 2, 7, 4, 4])}")
	print("conta_vocali non implementata")


if __name__ == "__main__":
	main()
