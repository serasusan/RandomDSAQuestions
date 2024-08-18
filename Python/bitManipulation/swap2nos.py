a = 10
b = 5

# a,b = b,a
# print(a,b)

# using XOR
a = a^b
b = a^b
a = a^b
print(a,b)