
import random
# list1 = []
# a = int(input("Enter how many names"))
# b = int(input("Enter how many groups you want to divide them into"))
# # list1=["apples","bananas","oranges"]
# for i in range(a):
#     c = input("Enter the name")
#     list1.append(c)


# # print($"")


# dict1 = {}

# for i in range(b):
#     dict1[f"team{i}"] = "0"


# print(dict1)

# ason = True
# while True:
#     v = random.choice(list1)

#     for i in range(len(dict1)):
#         for i in dict1[f"team{i}"]:
#             if i != v:
#                 dict1[f"team{i}"] = ''.join(v)
#                 print(dict1)
#                 ason=False






      

# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list
     
# # Driver Code
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))

list1=[1,2,3,4,5,6,7,8]

listz=[]
asa=True
while asa:
    v=random.choice(list1)
    if v not in listz:
        listz.append(v)
    if len(listz)!=len(list1):
        asa=True
    else:
        asa=False

groups=3
print(listz)
iter=0
tex=[]
for i in listz:
    tex.append(i)
    iter+=1
    if iter %3==0:
        print(tex)
       
    









