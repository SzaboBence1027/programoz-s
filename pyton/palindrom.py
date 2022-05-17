bekert=input("adj meg egy tetszoleges hosszusagu szot ")
jo=True

for n in range(round((len(bekert)/2)+1)):
    if bekert[n]!=bekert[len(bekert)-n-1]:
        jo=False  


if jo==True:
    print("ez egy  palindrom ")  
else:
    print("ez nem egy  palindrom")      


  