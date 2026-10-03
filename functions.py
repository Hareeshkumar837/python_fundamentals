# def add(a,b):
#     sum = a+b
#     return sum
# print(add(7,8))


# def new(a):

#     b= round(a,2)
#     return b
# print(new(3.14567))


# def introduce(a,b):
    
#     return f"hi my name is{a} and Iam {b} years old"

# print(introduce("Ben",54))


# def even(a):

#     if a%2 ==0:
#         return True
#     else:
#         return False   

# print(even(5))        

# def palindrome(a=""):

#     if a==a[::-1]:
#         return True
#     else:
#         return False

# print(palindrome("racecar"))    

def price(a,b=10):

    final_price =a-(a*(b/100))
    print(final_price)

price(5)