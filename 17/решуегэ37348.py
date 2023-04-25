a = [int(x) for x in open('17reshuege37348.txt')]
ans = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] * a[j]) % 34 != 0:
            ans.append((a[i] + a[j]))
print(len(ans), max(ans))
