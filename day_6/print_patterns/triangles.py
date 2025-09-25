rows=int(input('enter values'))
print('\n right angle with each row same number increasing row because of printing outer loop')
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
print('\n inverted right angle with each row same number when ranges start from end ')
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(i,end='')
    print()

print('\n right angle with each row same number decreasing row because of printing rows-outer loop')
for i in range(rows):
    for j in range(i+1):
        print(rows-i,end='')
    print()

print('\n right angle with each row trail of numbers because printing inner loop')
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end='')
    print()


print('\n reversed right triangle of numbers when ranges start from end ')
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
