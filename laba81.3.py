n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for k in range(2, n + 1):
    b = []
    for i in range(k):
        for j in range(k):
            b.append(a[i][j])
    unique_b = sorted(list(set(b))) 
    print(unique_b[-2]) 