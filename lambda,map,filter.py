# final =lambda x : x-5
# print(final(20))

# data = ["apple","banana","cherry"]

# print(list(map(lambda x: x+"pie",data)))

# readings = [15,-2,8,-99,42,-5]

# print(list(filter(lambda i: i>=0,readings)))

num  = [12,5,8,9,21,3,7,10,25,4]

# print(list(filter(lambda a: a>10 and a%2==0,num)))

# for i in num:
#     if i>10 and i%2==0:
#         print(list(i))

# print(list(i for i in num if i>10 and i%2==0 ))

# stud = {"arun":78,"rahul":92,"akhil":65,"vishnu":88,"nikhil:":54}
# print({n:s for n,s in stud.items() if s>80})

# def ave(x=[]):
#     sum = 0

#     for i in x:
#         sum+=i
#     average=sum/len(x) 
#     print(average)
#     return average

# ave([10,20,30,40,50])


def maths(y):
    e=[]
    o=[]
    for n in y:
        if n%2==0:
            e.append(n)
        else:
            o.append(n)
    print(e,o,sum(e),sum(o)) 
    return e,o
maths([10,15,22,33,40,51,60,73,84,91])           
        


   

