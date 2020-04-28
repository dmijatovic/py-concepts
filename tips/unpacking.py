# Unpacking values from list, tuple 

# unpack in a b
a,b = (1,2)
print("simple unpack")
print(a,b)

# unpack first two in separate vars and the rest in c
a,b,*c = (1,2,3,4,5,6)
print("partial unpack")
print(a)
print(b)
print(c)

# unpack first two and ignore rest
a,b,*_ = (1,2,3,4,5,6)
print("partial unpack with ignore")
print(a)
print(b)

# unpack first two, middle group and last
a,b,*c,d = (1,2,3,4,5,6)
print("partial unpack with selection")
print(a)
print(b)
print(c)
print(d)