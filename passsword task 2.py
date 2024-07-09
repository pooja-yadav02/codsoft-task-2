print ("WELCOME TO PASSWORD GENERATOR BY POOJA")
import random
number=["1","2","3","4","5","6","7","8","9"]
letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
 "a", "b", "c"," d", "e", "f" ,"g", "h", "i"," j"," k"," l", "m"," n"," o", "p"," q ","r ","s"," u"," v", "w" ,"x", "y", "z" ]
symbol=["!","@","#","$","%","^","&","*","(",")","_","+"]
n_letter=int(input("How many letter you want in your password :-"))
# suppose you took 3 letter to generate your password 
n_symbols=int(input("How many symbols you want in your password :-"))
# here you take 4 symbol to generate your passwrord 
n_numbers=int(input("How many number  you want in your password :-"))
# Here you took 2 number to generate your password 
empty_list=[]
for i in range(1,n_letter+1):
    value= random.choice(letter)
    empty_list+=value
for i in range (1,n_symbols+1):
     value=random.choices(symbol)
     empty_list+=value
for i in range (1,n_numbers+1):
     value=random.choices(number)
     empty_list+=value
random.shuffle(empty_list)
your_password=""
for value in empty_list:
    your_password += value
print("your password is here:- ",your_password)    
     
     
     



