import random

def randomlista(len_lista):
    szamok=[]
    for n in range(len_lista):
       r=random.randint(1,100)
       szamok.append(r)
       
    return szamok





rszamok=randomlista(20)
print("randomszamok",rszamok) 
a=(len(rszamok))-1




randszamok=randomlista(30)
print(randszamok)
    

def otvenelkisseb(rszamok):
    otvenelkissebrszamok=[]
    for n in range(a):
        if rszamok[n]<=50:
            otvenelkissebrszamok.append(rszamok[n])
    print(otvenelkissebrszamok)

otvenelkisseb(rszamok)
otvenelkisseb(randszamok)       




