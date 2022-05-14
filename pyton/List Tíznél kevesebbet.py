lista=[1,2,3,4,5,8,13,21,34,55,89]

i=0
while i<len(lista):
    if lista[i]<5:
        print(lista[i])
    i=i+1   

otoslista=[]      
i=0
while i<len(lista):
    if lista[i]<5:
        otoslista.append(lista[i])
    i=i+1

print(otoslista)     

bekertszam=int(input("add meg a szamot aminel kissab szamokat irja ki a program"))
i=0
while i<len(lista):
    if lista[i]<bekertszam:
        print(lista[i])
    i=i+1   


felhasznaloslista=[]      
i=0
while i<len(lista):
    if lista[i]<bekertszam:
        felhasznaloslista.append(lista[i])
    i=i+1
print(felhasznaloslista)  