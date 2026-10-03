# a = "quiet down"
# print(a.upper())

# text = "i love pyton"
# print(text.replace("pyton","python"))

# quote = "may the force be with you"
# new = quote.split()
# num = len(new)
# print(new,num)


# transmission = "eagle has landed at midnight. execute the pyton protocol."

# def decode_msg(text):

#     a = text.replace("pyton","python")
#     b = a.upper()
#     c = b.split()
#     d = {"word_count":len(c),"content":b}

#     return d
# print(decode_msg(transmission))

# nums = [5,10,15]
# plus_five = [i+5 for i in nums]

# print(plus_five)

# letters = ["a","b","c","e","f","i"]
# new = [i for i in letters if i in "aeiou"]
# print(new)


# gear =["tent","sleeping bag","flashlight"]
# a = {i:50 for i in gear}
# print(a)

# sensor_readings = [45,999,50,-99,55,999,48]

# valid_readings = [i for i in sensor_readings if 0<i<100]
# print(valid_readings)

# print({i : "valid" for i in valid_readings})


# a =100
# b = 0

# try:
#     c = a/b
# except:
#     print("division error!")

# age = "ten"

# try:

#     d = int(age)

# except ValueError:
#     print("invalid age format")    


# student = {"name":"alex","grade":"A"} 
# try:
#     print(student["age"])
# except KeyError:
#     print("data not found")       

# with open("diary.txt","w")as file:

#     file.write("welcome.")

# with open("diary.txt","a")as file:
#     file.write("\n unstoppable")  

# with open("diary.txt","r")as file:
#     print(file.read())
         
import random

coin =["heads","tails"]
a = random.choice(coin)
print(a)

import random

b = [i for i in range (1,101)]
c = random.choice(b)
print(c)

from math import pi
r = 5
area = pi*(r**2)
print(area)