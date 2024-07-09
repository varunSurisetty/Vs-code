def volume(l, b, h):
    return l * b * h

l = int(input("Enter length of prism -> \n"))
b = int(input("Enter Breadth of prism -> \n"))
h = int(input("Enter Height of prism -> \n"))

print("The volume of the prism is "+ str(volume(int(l), int(b), int(h))))