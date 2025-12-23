#tuples is one of the collection data type
#ordered, immutable, allows duplicate 
#objects that belongs together

mytup = {"Nafiul", 28, "Boston"}
mytup2 = tuple(["Nafiul", 28, "Boston"])
mytup3 = ('a','p','p','l','e')
mytup4 = (0,1,2,3,4,5,6,7,8,9)

#normal tuples
print("Tuples-1: ", mytup)

#tuples function
print("Tuples-2: ", mytup2)

#tuples item
item = mytup2[-1]
print("Tuple-2 Item: ", item)

#tuple items
for i in mytup:
    print("Tuple-1 Items:", i)

#Tuple checking
if "Tim" in mytup:
    print("Tim is present")
else:
    print("Tim is Absent")
    
#Number of Tuple Items
print("Number of Item in Tuple-3:", len(mytup3))

#count the number of item
print("Number of p in the Tuple-3:", mytup3.count('p'))

#index number of p 
print("Index of p in the Tuple-3:", mytup3.index('p'))

#unpack tuples
name, age, city = mytup2
print("Description of Nafiul.")
print("Name: ", name)
print("Age: ", age)
print("City: ", city)

#tuple to list
i1, *i2, i3 = mytup4
print("Item of Tuple-4: ")
print("First item:",i1)
print("Last item:",i3)
print("In between item to list:",i2)
