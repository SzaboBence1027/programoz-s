#kő papír olló

helyesbekeres=True
elsojatekos=input("kő papír vagy olló?")
while helyesbekeres==True:
    if elsojatekos=="kő" or elsojatekos=="papír" or elsojatekos=="olló":
        helyesbekeres=False
    else:
        elsojatekos=input("kő paír vagy olló?")
        helyesbekeres=False
print(elsojatekos)        

for n in range(80):
    print('nem leskelődünk')
helyesbekeres=True
masodikjatekos=input("kő papír vagy olló?")
while helyesbekeres==True:
    if masodikjatekos=="kő" or masodikjatekos=="papír" or masodikjatekos=="olló":
        helyesbekeres=False
    else:
        masodikjatekos=input("kő paír vagy olló?")
        helyesbekeres=False
print(masodikjatekos)   


if elsojatekos=="kő":
    if masodikjatekos=="kő":
        print("Senki nem nyert")
    elif masodikjatekos=="papír":
        print("A masodik jatekos nyert")
    else:
        print("elsojatekosnyert")        
elif elsojatekos=="papír":  
    if masodikjatekos=="papír":
        print("Senki nem nyert")
    elif masodikjatekos=="olló":
        print("A masodik jatekos nyert")
    else:
        print("elsojatekosnyert")  
elif elsojatekos=="olló":  
    if masodikjatekos=="olló":
        print("Senki nem nyert")
    elif masodikjatekos=="kő":
        print("A masodik jatekos nyert")
    else:
        print("elsojatekosnyert")  


