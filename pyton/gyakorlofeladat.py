import random 
szam = random.randint(1, 100)
print("Gondoltam egy számra 1 és 100 között.")
tipp=0
while (szam!=tipp):
    tipp = int(input("Adj meg egy szamot"))
    if (tipp>szam):
        print("Nem, ennél kisebbre gondoltam.")
    else:
        if (tipp<szam):
            print("Nem, ennél nagyobbra gondoltam.")
        else:
            print("Igen, eltaláltad!") 





#masodikfeladat


def szamlalo():
    szoveg=input("milyen szo ")
    kulonbozokarakterek=input("milyen betu ")
    szamlal=0
    szoveghossz=len(szoveg)
    for n in range(szoveghossz):
        if szoveg[n]==kulonbozokarakterek:
            szamlal+=1
    print("a szoban ennyiszer vann benne a betu: ",szamlal)

szamlalo()  



#harmadikfeladat





    