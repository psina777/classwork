
f = open('26_2686 (1).txt')
k = int(f.readline())
a = sorted([list(map(int, x.split())) for x in f])
count =0
for i in range(k - 1):
    if a[i][0] == a[i+1][0] and a[i][1] + 1 == a[i+1][1]:
        count +=1
        if count>= 5:
            print(a[i+1])
    else :
        count = 0