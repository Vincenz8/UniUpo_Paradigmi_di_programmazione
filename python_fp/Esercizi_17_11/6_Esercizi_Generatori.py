def mio_range(start: int, end: int, step: int):
	if (start - end) * step < 0:
		while start != end:
			yield start
			start += step


def gen_fib(n: int):
	fib_1, fib_2 = 0, 0
	fib = 1
	
	while n != 0:
		yield fib
		fib_1, fib_2 = fib_2, fib
		fib = fib_1 + fib_2
		n -= 1


def gen_fib_inf():
	fib_1, fib_2 = 0, 0
	fib = 1
	
	while True:
		yield fib
		fib_1, fib_2 = fib_2, fib
		fib = fib_1 + fib_2


def gen_fib_n(n: int):
	fib = [0 for _ in range(n + 1)]
	fib[n] = 1
	print(fib)
	while True:
		yield fib[n]
		tmp = 0
		for i in range(n):
			fib[i] = fib[i + 1]
			tmp += fib[i]
		fib[n] = tmp


if __name__ == "__main__":
	#  Esercizio 1
	print(list(mio_range(start=3, end=7, step=1)))
	print(list(mio_range(start=7, end=3, step=1)))
	print(list(mio_range(start=3, end=7, step=2)))
	print(list(mio_range(start=3, end=7, step=-2)))
	print(list(mio_range(start=7, end=3, step=-1)))
	print(list(mio_range(start=3, end=7, step=-2)))
	print(list(mio_range(start=7, end=3, step=-2)))
	
	# Esercizio 2
	for x in gen_fib(7):
		print(x)
		
	# Esercizio 3
	fib = gen_fib_inf()
	for x in range(1, 10):
		print(next(fib))
	
	# Esercizio 4
	test = gen_fib_n(4)
	for _ in range(10):
		print(next(test))
		