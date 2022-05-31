
#elsofeladat


aoldal=int(input('Add meg az egzenlo haromszog egzenlo oldalat'))
boldal=int(input('Add meg az egzenlo haromszog also oldalat'))
k=(aoldal+aoldal+boldal)/7
print(round(k,2))


#masodikfeladat
korsugar=int(input("kerem a kor sugarat"))
pi=3.14
korkerulet=(korsugar*2)*pi
print(round(korkerulet,2))

#harmadikfeladat
csillagokszama=int(input("Mennyi csillaga legyen belanak"))
print("Belanak",csillagokszama,"csillagja van")

#negyedikfeladat
lista=[]
egyikszam=int(input("Ad meg minel nagyobb szamok legyenek"))
masikszam=int(input("Ad meg minel kissebszamok legyenek"))
helyesbekeres=False
while helyesbekeres==False:
    if egyikszam>=masikszam:
        print("Nem lehet kisseb a masik szamnal")
        masikszam=int(input("Ad meg minel kissebszamok legyenek"))
    else:
        helyesbekeres=True

i=egyikszam+1
while i<masikszam:
    lista.append(i)
    i=i+1
print(sum(lista))    

#otodikfeladat

masodiklista=[]
nemoszthatotizel=False
while nemoszthatotizel==False:
    szam=int(input("Adj meg egy szamot"))
    if szam%10==0:
        nemoszthatotizel=True
    else:
        masodiklista.append(szam)   

print("szamok osszege",sum(masodiklista))