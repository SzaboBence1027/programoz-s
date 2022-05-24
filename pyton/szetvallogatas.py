import imp


import random

osszesszam=[]
for n in range(101):
    r=random.randint(0,100)
    osszesszam.append(r)

huszonotnelkisseb=[]
otvenelkisseb=[]
hetvenotnelkisseb=[]
szaznalkisseb=[]


for n in osszesszam:
    if n<=25 and n>=0:
        huszonotnelkisseb.append(n)
    elif n>25 and n<=50:
        otvenelkisseb.append(n)    
    elif n>50 and n<=75:
        hetvenotnelkisseb.append(n) 
    else:
        szaznalkisseb.append(n)   


print(huszonotnelkisseb)
print(otvenelkisseb)
print(hetvenotnelkisseb)
print(szaznalkisseb)

print(osszesszam)

talalt=False
i=0
while i<100 and talalt==False:
    if osszesszam[i]==69:
        talalt=True
        print("megtalaltam a 69 ami a lista ",i+1,"elemen van")
    else:
        i=i+1  

if talalt==False:
    print("nincs benne a 69 szam a listba")



