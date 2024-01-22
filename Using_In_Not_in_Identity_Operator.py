#Python Program to illustrate
#Finding common member in list
#Without using 'in' Operator
#Define a funcion() that take two lists
print("Practical No 7A:Membership and identity Operators in,not in")
print("Practical perform by Roll No :04,Om Solanki")
def overlapping(list1,list2):
 for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if(list1[i]==list2[j]):
            return 1
    return 0
list1 = [2,3,4,5]
list2 = [6,7,8,9]
if(overlapping(list1,list2)):
 print("Overlapping :")
else:
 print("Not Overlapping !")
