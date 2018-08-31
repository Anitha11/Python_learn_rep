my_String='Anitha Kalidass'
print(my_String[0]) #using index
print(my_String[0:7])# using index range
print(my_String[0:7:2])# prints 0-6 skipping every2nd letter
print(my_String.find('t'))
print(my_String.replace('n','z'))
print(len(my_String))
print(my_String.count('A'))
print(my_String.upper())
print(my_String.lower())

name='Mike'
age=25
salary=9000.45
manager=my_String
print("Hello %s" %(name))
print("Hello %s %d %f %s" %(name,age, salary,manager))
