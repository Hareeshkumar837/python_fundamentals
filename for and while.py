# timer = 5

# while timer>0:
#     print(f"timer is {timer}")
#     timer = timer -1
# print("go!")    


# for i in range(1,11):

#     if i%2==0:
#         print(i)

# word = "banana"
# count = 0
# for i in word:
    
#     if i == "a":
#         count+=1
# print(count)

list

# food = ["apple","cb","coffee"]
# print(food[2])

# gagdgets=["phone","laptop"]
# gagdgets.append("tablet")
# gagdgets[0]="smartwatch"
# print(gagdgets)

# num = [2,4,6,8,5]
# for i in num:
#     i*=10
#     print(i)    




# def score(a=[]):

#     winner=[]
#     for i in a:
#         if i >=50:
#             winner.append(i)
#     return winner
# print(score([23,45,65,78,98,67]))        


# user_info =("ben",28,"kannur")
# print(user_info[2])

# attendees=["alex","ben","mary","mary","priya","ben"]

# new_list = set(attendees)
# print(new_list)

# a = {1,2,3,4,5,}
# b = {9,8,7,6,5,4,3}
# c = a.intersection(b)
# print(c)

# dict={"alice":1234,"ben":4567,"status":"online"}
# print(dict["ben"])
# dict["status"]="offline"
# dict["level"]=1
# print(dict)

# inventory={"apple":4,"oranges":3,"mango":1}
# for fruit,num in inventory.items():
#     if num <2:
     
#      print(f"order more {fruit}")        


# aw_rwps=[("alice",25,"yes"),("bob",17,"yes"),("charlie",30,"no"),("alice",25,"yes"),("david",22,"yes")]

# def manage_party(rwps):
#     approved_name=[]
#     for i in aw_rwps:
#         if i[1] >= 18 and i[2]== "yes":
#             approved_name.append(i[0])

#     approved_name=set(approved_name) 
#     final_list={"total_guest":len(approved_name),"guest_names":approved_name}
#     return final_list
# print(manage_party(aw_rwps))       


user_cart = [("laptop",1000,1),("mouse",20,3),("keyboard",50,1),("mouse",20,1)]

def process_order(cart):
    total_cost = 0
    item_name =[]
    for i in cart:
        base_cost=i[1]*i[2]
        
        

        if i[2] >=3:
            base_cost -= 10
        total_cost += base_cost
        item_name.append(i[0])     
             
             

    item_name=set(item_name) 
    user_list={"amount_due":total_cost,"unique_items":item_name}
    return user_list
print(process_order(user_cart))

