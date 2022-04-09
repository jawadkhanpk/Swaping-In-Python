#swaping in  python
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5

# after swaping

# a = 5
# b = 3
# c = 1
# d = 2
# e = 4
# ------------------------------------------------------------------------

a = input("Enter value of A: ")
b = input("Enter value of B: ")
c = input("Enter value of C: ")
d = input("Enter value of D: ")
e = input("Enter value of E: ")

temp = a
a = e
e = c
c = temp
temp = b
b = e
e = d
d = temp
print(a,b,c,d,e)
