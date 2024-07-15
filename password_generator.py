import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

special_char=['!','@','#','$','%','^','&','*','(',')',]

numbers=['1','2','3','4','5','6','7','8','9',]

print("Welcome to password generator!!")

n_letters=int(input("Enter no of letters you want in your password = "))
n_special_char=int(input("Enter no of special char you want in your password = "))
n_numbers=int(input("Enter no of number you want in your passoword = "))

password=""
for i in range(1,n_letters+1):
    char=random.choice(numbers)
    password += char

for i in range(1,n_special_char+1):
    char=random.choice(special_char)
    password += char

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password += char

print(password)