##list
from operator import truediv

l = [1, 2, 3, 4, 5,]
print(l)
print("my List:", l)
# append
l.append(4)
#insert
l.insert(2, 10)
print("List after adding elements:",l)
#pop
l.pop()
popped_item = l.pop(2)
print("Popped item:", popped_item)
#sort
l.sort()
print("Sorted List:",l)
#Slicing
print("Slice of List (1 to 4):", l[1:5])
#remove
l.remove(4)
print("After Remove:", l)
#access by index
print("Element at index 3:", l[3])

# if condition
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

##tuple
t=(67,87,54,89,879)
print("my Tuple:", t)
#Access elements by index
print("Element at index 2:", t[2])
#slicing
sliced_tuple = t[1:3]
print("Sliced Tuple:", sliced_tuple)
#concatenation
new_tuple = t + (60,70)
print("New Tuple after concatenation:", new_tuple)
#if condition
t=(67,87,54,89,879)
if 54 in t:
    print("54 is in the tuple")
else:
    print("54 is not in the tuple")
#for loops
t=(67,87,54,89,879)
found = False
for item in t:
    if item == 87:
        found = True
        print("87 is in the tuple")
        break
if not item:
    print("87 is not in the tuple")
print()
#while loop
t=(67,87,54,89,879)
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

##dictionary
my_dict = {'name': 'Bhuvana', 'age': 21, 'city': 'Vijayawada'}
print("my Dictionary:", my_dict)
#add key-value pair
my_dict['state'] = 'AP'
print("Dictionary after adding new key-value:", my_dict)
#Update value of an existing key
my_dict['age'] = 20
print("After Updating Value for 'age':", my_dict)
# Remove
del my_dict['city']
print("After Removing Key 'city':", my_dict)
#if key exists or not
print("Is 'age' a key in the dictionary?", 'age' in my_dict)
print("Is 'b' a key in the dictionary?", 'b' in my_dict)
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
#while loops
# my_dict = {'name': 'Bhuvana', 'age': 21, 'city': 'Vijayawada'}
# index = 0
# found = False
# while index < len(my_dict):
#     if my_dict[index] == 'name':
#         found = True
#         print("name is in the Dict!")
#         break
#     index += 1
#
# if not found:
#     print("name is not in the Dict!")
##set
S = {40,89,90,94,96,67,23,82}
print("Original Set:", S)
# Remove an element
S.remove(90)
print("After Remove:", S)
# Add elements
S.add(6)
print("After Add:", S)
#if element exists or not
print("Is 4 in the set?", 4 in S)
print("Is 96 in the set?", 96 in S)
# union,intersection,difference
s = {41, 25, 96, 78}
print("Union of sets:", s.union(S))
print("Intersection of sets:", S.intersection(s))
print("Difference of sets:", S.difference(s))
print("Difference of sets:", s.difference(S))
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
# #while loop
# S = {40,89,90,94,96,67,23,82}
# index = 0
# found = False
# while index < len(S):
#     if S[index] == 94:
#         found = True
#         print("94 is in the set!")
#         break
#     index += 1
#
# if not found:
#     print("94 is not in the set!")

print()
print("List:", l)
print("Tuple:", t)
print("Set:", S)
print("another set:", s)
print("Dictionary:", my_dict)







