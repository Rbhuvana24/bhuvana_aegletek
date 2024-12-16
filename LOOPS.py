#LIST
l = [1, 2, 3, 4, 5,]
if 4 in l:
    print("4 is in the list!")
else:
    print("4 is not in the list!")
#for loops
l = [1, 2, 3, 4, 5,6,7,8,9]
found = False
for item in l:
    if item == 7:
        found = True
        print("7 is in the list!")
        break
if not item:
    print("7 is not in the list")
print()
#while loops

l = [1, 2, 3, 4, 5,6,7,8,9]
index = 0
found = False
while index < len(l):
    if l[index] == 6:
        found = True
        print("6 is in the list!")
        break
    index += 1

if not found:
    print("6 is not in the list!")

# if condition
    t = (67, 87, 54, 89, 879)
    if 54 in t:
        print("54 is in the tuple")
    else:
        print("54 is not in the tuple")
    # for loops
    t = (67, 87, 54, 89, 879)
    found = False
    for item in t:
        if item == 87:
            found = True
            print("87 is in the tuple")
            break
    if not item:
        print("87 is not in the tuple")
    print()
    # while loop
    t = (67, 87, 54, 89, 879)
    index = 0
    found = False
    while index < len(t):
        if t[index] == 89:
            found = True
            print("89 is in the tuple!")
            break
        index += 1
        if not found:
            print("89 is not in the tuple!")

#dictionary
#if condition
my_dict = {'name': 'Bhuvana', 'age': 21, 'city': 'Vijayawada'}
if 'age' in my_dict:
    print("age is in my_dict")
else:
    print("age is not in my_dict")
#for loops
my_dict = {'name': 'Bhuvana', 'age': 21, 'city': 'Vijayawada'}
found = False
for item in my_dict:
    if item == "city":
        found = True
        print("city is in the dict")
        break
if not item:
    print("city is not in the dict")
print()

#set
#if condition
S = {40,89,90,94,96,67,23,82}
if 23 in S:
    print("23 is  in the set")
else:
    print("23 is not in the set")
#for loops
S = {40,89,90,94,96,67,23,82}
found = False
for item in S:
    if item == 67:
        found = True
        print("67 is in the set!")
        break 
if not item:
    print("67 is not in the set")