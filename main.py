n, m1,m2, g = map(int,input().split())
zetoni = []
for i in range(0,n):
    zetoni.append(i+1)
i = 0
while i < g:
    sk1, sk2 = map(int, input().split())
    j = 0
    while j< len(zetoni):
        if zetoni[j] >= sk1 and zetoni[j] <= sk2:
            zetoni[j] = 0
        j+=1
    i+=1
labu_skaits = 0
for zeton in zetoni:
    if (zeton%m1 == 0 or zeton%m2==0) and zeton != 0:
        labu_skaits += 1

print(labu_skaits)