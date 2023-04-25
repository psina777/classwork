a = [int(x) for x in open('17-4.txt(4312)')]
#m = 10001
#k = 0
ans =[] #или так
for i in range(len(a)):
    if (a[i] % 3 == a[i] % 5) and (a[i] % 31 == 0 or a[i] % 47 == 0 or a[i] % 53 == 0):
        ans.append(a[i])# или так
        #k+=1
       # m = min(m, a[i])
#print(k,m)
print(len(ans), min(ans)) #или так