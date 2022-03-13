#if 10 
# output should be == 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155... 1 4 2 1 END HERE

x=10
a = int(2)
while a > 1:
    a = 3*x+1

    #Check div by 2
    remainder = a % 2
    isdvsbl = remainder == 0 
    if isdvsbl == True:
        print(a / 2)
    else:
        print(a)
    x=a

print(".")