import random

def randomlista(szamok):
    for n in range(20):
       r=random.randint(1,100)
       szamok.append(r)


rszamok=[]
randomlista(rszamok)   
print(rszamok)    



randszamok=[]
randomlista(randszamok)
print(randszamok)
    