

def sum(x,y):
    return x+y
def diff(x,y):
    return y-x
def print_func(s):
    print(s)

def ans_func():
    if (sum(3,7)==9):
        print_func("Funtion sum is called")
    elif (diff(3,7)==4):
        print_func("Func diff is called")
    else:
        print_func("No func is called")
ans_func()
name='anitha'
if name.isalpha():
    print("Name is alpha")
else:
    print("Not a aplha")
new_name=name[1:len(name)]
print(new_name)
