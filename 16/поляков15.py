k=[]
def F(n):
  if n > 0: G(n - 1)
def G(n):
    k.append("*")
    if n > 1: F(n - 3)
print(F(11), len(k))