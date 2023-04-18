a = [int(x) for x in open('reshuege37340')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] - a[j]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0):
            ans.append((a[i] + a[j]))
print(len(ans), max(ans))
