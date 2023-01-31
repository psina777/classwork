
def f (x, a1, a2):
    return  ((150 <= x <=390) <= (a1 <= x <= a2)) and ((440 <= x <=570)<= (a1 <= x <= a2))

m=1000
for a1 in range(100, 600):
    for a2 in range (a1 + 1, 600):
        if all(f(x, a1, a2 )== 1 for x in range (100, 600)):
            m = min(a2 - a1, m)
print(m/10)
