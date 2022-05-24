import imp


import random

osszesszam=[]
for n in range(100):
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



