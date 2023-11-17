from types import FunctionType
from typing import Sequence


def comp(f: FunctionType, g: FunctionType):
    return lambda x: f(g(x))


def max_func(*funzioni, n: int):
    max_f = funzioni[0]
    max_n = funzioni[0](n)
    
    for func in funzioni[1:]:
        tmp = func(n)
        if tmp > max_n:
            max_n = tmp
            max_f = func
    
    return max_f


def iter_check(*arg_iter, iteratore: FunctionType, f1: FunctionType, f2: FunctionType):
    return (elem for elem in iteratore(*arg_iter) if (f1(elem) and f2(elem)) is True)


def make_fn(seq1: Sequence, seq2: Sequence):
    def mapping(x: int):
        i = seq1.index(x) if x in seq1 else None
        if i is not None:
            return seq2[i]
        else:
            return i
    return mapping
    
    
if __name__ == "__main__":
    # Esercizio 1
    test_comp = comp(lambda x: x ** 2, lambda x: x + x)
    print(test_comp(2))

    # Esercizio 2
    # Purtroppo non ho capito la consegna
    
    # Esercizio 3
    test_f = max_func(lambda x: x ** 2, lambda x: x + x, n=3)
    print(test_f(3))
    
    # Esercizio 4
    test_iter = iter_check(1, 10, iteratore=range, f1=lambda x: (x % 2) == 0, f2=lambda x: (x % 2) == 0)
    for elem in test_iter:
        print(elem)
        
    # Esercizio 5
    foo = make_fn([1, 2, 3, 4, 6], (7, 6, 5, 4, 3))
    print(list(map(foo, range(10))))
    

