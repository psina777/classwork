a = [int(x) for x in open('polyakov4496.txt')]
ans = []
for i in range (len(a)-1):
    if (a[i] - a[i+1]) % 2 == 0 and (a[i] - a[i+1]) % 37 == 0:
        ans.append(a[i]+ a[i+1])
print(len(ans), max(ans))