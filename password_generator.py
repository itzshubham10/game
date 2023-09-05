import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


numbers= [1,2,3,4,5,6,7,8,9,0]

symbols=['!','@','#','$','%','^','&','*','(',')','_','+','=']

print("Welcome To Password Generator!!!")

n_letters= int(input("How many letters you want in your password\n")) #4

n_numbers=int(input("How many numbers you want in your password\n"))

n_symbols= int(input("How many symbols you want in your password\n"))



password = ''

for i in range(1,n_letters+1):
    char =random.choice(letters)
    password = password + char

for j in range (1, n_numbers+ 1 ):
    num = random.choice(numbers)
    password = password + str(num)

for k in range(1,n_symbols +1):
    sym = random.choice(symbols)
    password +=sym


strong_password =''.join(random.sample(password,len(password)))

print(f"Random generated paaword is :{strong_password}")

