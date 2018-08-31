a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=a+b # new list concatinated from a and b
print(a)
print(b)
print(c)

s='a b c d e f'
z=s.split() # converts the string to list using the space as delimeter
print(s)
print(z)

if('a' in z):
    print("A is present in z")
else:
    print("A Not in Z")
if ('g' not in z):
    print("G is not in z")
else:
    print("G is in z")
for i in a:
    print(i)
q=[3,6,1,0,5,2,0]
print ("original list: ", q)
q.sort()
print("Sorted list: ",q)
q.reverse()
print("Reversed list: ",q)
print("num of 0's in the list",q.count(0))
print("index value of 1 in the list", q.index(1))
print("length of list",len(q))
print("min value in the list",min(q))
print("max value in the list",max(q))
