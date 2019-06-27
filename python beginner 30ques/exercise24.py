x=int(input("enter the dimension:"))
def print_horiz_line():
    print(" --- " * x)

def print_vert_line():
    print("|    " * (x + 1))
for index in range(x):
    print_horiz_line()
    print_vert_line()
print_horiz_line()
