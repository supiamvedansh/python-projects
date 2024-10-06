import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","&","*"]
print("Welcome to the password generator")
nr_letters=int(input("How many letters would you like in your password\n"))
nr_symbols=int(input("How many symbols would you like in your passoword\n"))
nr_numbers=int(input("How many numbers would you like in your password\n"))
#password in a mixed randoom order
password_list=[]
for char in range(1,nr_letters+1):

    password_list.append(random.choice(letters))
    
for char in range(1,nr_symbols+1):
     password_list.append(random.choice(symbols))
   
for char in range(1,nr_numbers+1):
     password_list.append(random.choice(numbers))
print(password_list)

passs=""
for char in password_list:
    passs=passs+char
    print(f"Your password is :{passs}")