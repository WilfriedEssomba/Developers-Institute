# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty', 'huzoi']
values = [10, 20, 30]
dico = dict(zip(keys, values))
print(dico)
# Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8, 'Essomba': 11}
x = 0 #price
for key,value in family.items():
    if value < 3:
        print(key, 0)
        x+=0
    elif 3 <= value <= 12:
        print(key, 10)
        x+= 10
    else:
        print(key, 15)
        x+= 15
print(x)

name = input("enter the names with spaces ")
age = input("enter the ages with spaces ")
list1 = name.split()
list2 = age.split()
list2_int = [int(x) for x in list2]
print(list2_int)
family2 = dict(zip(list1, list2_int))
print(family2)
# Exercise 3

# Exercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
numbers = [0, 1, 2, 3, 4]
disney_user_A = dict(zip(users, numbers))
disney_user_B = dict(zip(numbers, users))
print(disney_user_A)
print(disney_user_B)
