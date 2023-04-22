import random
letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','^','&','*','+','?']
print("welcome to password generator !")
nr_letter = (int(input("How many letters would you like in password ?\n")))
password =[]
for char in range (1,nr_letter+1):
    password.append(random.choice(letters))

nr_symbols = int(input(f"how many symbols would you like ? \n "))
for char in range (1,nr_symbols+1):
    password += random.choice(symbols)

nr_numbers = int(input(f"how many number would you like ? \n"))
for number in range (1,nr_numbers+1):
    password += random.choice(numbers)
    
random.shuffle(password) 

passwor =" "
for character in password:
    passwor += character 
print(passwor)