mylist = ["apple", 5, "cherry", True]
mylist2 = ["banna", 6, "lof", True]
mylist3 = [4,352,1,-35,75,113]
mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist5 = [1, 2, 3, 4, 5]

#print all the item 
print("The List:", mylist)

#print each item
for x in mylist:
    print(x)

#insert item at last
mylist.append("lemon")
print("Appended:", mylist)

#insert certain item at certain positon
mylist.insert(2, "blueberry")
print("Inserted:", mylist)

#remove the last item
mylist.pop()
print("Pooped:", mylist)

#remove the specific item
mylist.remove("cherry")
print("Removed:", mylist)

#remove all the item 
mylist2.clear()
print("Cleared:", mylist2)

#reverse the item 
mylist.reverse()
print("Reversed:", mylist)

#sort the item
new = sorted(mylist3)
print("New Sorted:", new)

#sort the original item
mylist3.sort()
print("Old Sorted:", mylist3)

#adding two list
new2 = mylist + mylist3
print("Plused list:", new2)

#slicing the list
a = mylist4[1:7]
a2 = mylist4[1:-3]
a3 = mylist4[3::2]
print("Sliced:", a)
print("Sliced:", a2)
print("2 steps:", a3)

#copy to prevent the modify the original
list_cp = mylist.copy()
list_cp2 = mylist[:]
list_cp3 = list(mylist)

list_cp.append("water")
list_cp2.append("water")
list_cp3.append("water")
print("The Original:", mylist)
print("Copied-1:", list_cp)
print("The Original:", mylist)
print("Copied-2:", list_cp2)
print("The Original:", mylist)
print("Copied-3:", list_cp3)

#square the list
b = [i*i for i in mylist5] 
print("Squared:", b)
