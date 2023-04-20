a = [int(x) for x in open('reshuege48465.txt')]
# поиск минимального числа, оканчивающегося на 6
min6 = 10001
for i in range(len(a)):
    if abs(a[i]) % 10 == 6:
        min6 = min(min6, a[i])
# пары
ans = []
for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 == 6) and (abs(a[i + 1]) % 10 != 6) or (abs(a[i]) % 10 != 6 and (abs(a[i + 1]) % 10 == 6)) and ((a[i] ** 2 + a[i + 1] ** 2) < min6 ** 2)):
        ans.append(a[i] ** 2 + a[i + 1] ** 2)
print(len(ans), max(ans))
#неверно