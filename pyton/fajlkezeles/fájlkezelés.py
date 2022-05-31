with open("vb2018.txt","r") as f:
    next(f)
    varos = []
    nev1 = []
    nev2 = []
    ferohely = []
    sor = []
    for i in f:
        sor = i.split(";")
        varos.append(sor[0])
        nev1.append(sor[1])
        nev2.append(sor[2])
        ferohely.append(int(sor[3].strip()))
print("3. feladat")
print(f"stadionok száma: {len(nev1)}")
print("4. feladat")
print(f"\tVárosnév: {varos[ferohely.index(min(ferohely))]}\n\tStadion neve: {nev1[ferohely.index(min(ferohely))]}  (aka. {nev2[ferohely.index(min(ferohely))]})\n\tFérőhelye: {ferohely[ferohely.index(min(ferohely))]}")
print("5. feladat")
print(f"A férőhelyek átlaga: {round(sum(ferohely)/len(ferohely),1)}")
print("6. feladat")
darab=0
for i in range(len(varos)):
    if "n.a." in nev2[i]:
        darab=darab+1
print(f"{len(nev2)-darab} db stadiumnak van második neve")
print("7.feladat")
nev=(input("Kérek egy városnevet!"))
while len(nev)<3:
    nev=(input("Kérek egy városnevet!"))
if nev in varos:
    print("A megadott város VB helyszín.")
else:
    print("8. feladat: A megadott város NEM VB helyszín.")
print("8.feladat")
db=[]
for i in range(len(varos)):
    if varos[i] not in db:
        db.append(varos[i])
print(len(db))