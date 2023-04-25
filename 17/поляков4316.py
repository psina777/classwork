a = [int(x) for x in open('17-4.txt(4316)')]
ans = []
for i in range (len(a)):
    s = sum(list(map(int,str(a[i]))))
    if s % 5 == 0 and a[i] % 3**2 != 0:
        ans.append(a[i])
print(len(ans), max(ans))