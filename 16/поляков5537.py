from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return n *f(n-1)


for n in range(2, 3000):
    f(n)


print(f(2023)/f(2020))
