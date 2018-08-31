# very similar to list with some differences
# declared with () insead of [] as in lists
# tuples cannot be edited, wheras lists can be edited
# tuples are immutable, lists are mutable
t =(2,5,4,6)
l=[3,4,5,6,7]
s_list=['a','b','c','d','e']
print(t[2])
print ("length of tuple",len(t))
print("list length before appending", len(l))
l.append(20)
print("list length after appending",len(l))
print("list data",l)
print("to print specific vakues form given index range 0:2, 2:4",l[0:2], l[2:4])
print("1: prints 1 to end, :3 prints, 0-2", l[1:], "&" ,l[:3])
print("To remove an item from the list l.remove(item name) ")
l.remove(5)
print("list data after removal",l)
print("string list", s_list)
s_list.remove("c")
print("list data after removal",s_list)
l_index=l.index(4)
print("to get the index number of an item e.g:4 is ",l_index )
