bekert=int(input("melyik szamnak keresem meg az osztojat?"))
x=list(range(2,bekert+1))
print(x)
osztok=[]
for n in x:
    if bekert%n==0:
        osztok.append(n)
print(osztok)