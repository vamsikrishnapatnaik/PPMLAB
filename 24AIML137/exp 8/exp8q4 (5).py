def largest(m,n,o):
    if m>n and m>o:
        return m
    elif n>m and n>o:
        return n
    else:
        return o

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
print(f"The largest between {a},{b} and {c} is :{largest(a,b,c)}")