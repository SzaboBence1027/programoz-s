from unicodedata import name


inputnumber=int(input("how much time print?"))

name=input("enter your name ")
print("your name is "+name)

age=int(input("enter your age "))
onehundred=(2022-age)+100

print("the year when you turn 100 is "+str(onehundred))

i=1
while(i<inputnumber):
    print("your name is "+name)
    print("the year when you turn 100 is "+str(onehundred))
    i=i+1
   
