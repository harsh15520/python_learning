multiplier1=int(input("enter multiplier1:\n"))
multiplier2=int(input("enter multiplier 2:\n"))
ranges=int(input("enter range:\n"))
print("     ", end='')
for header in range(1,ranges+1):
    print(f"{header:2}", end=' ')
print()  # Header row
print("     " + ("--- " * (ranges+1)))
for i in range(multiplier1,multiplier2+1):
    print(f"{i:2} | ", end='')
    for j in range(1, ranges+1):
        print(f"{i*j:2}", end=' ')
    print()
