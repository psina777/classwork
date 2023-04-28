def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(244143, 1367821 + 1):
    ans = []
    if len(div(i)) == 5:
        print(div(i)[-3], div(i)[-2])