import string
import random

s1 = list(string.ascii_uppercase) #30%
s2 = list(string.ascii_lowercase) #30%
s3 = list(string.digits) #20%
s4 = list(string.punctuation) #20%

passNumber = input("how many number of chars you want: ")

while True:
    try:
        passNumber = int(passNumber)
        if passNumber < 6:
            print("number must be greater than 6")
            passNumber = input("please try again: ")
        else:
            break
    except:
        print("please enter a number: ")
        passNumber = input("please try again: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

p1 = round(passNumber * (30/100))
p2 = round(passNumber * (20/100))

password = []

for i in range(p1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(p2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password)

print("password: ", password)