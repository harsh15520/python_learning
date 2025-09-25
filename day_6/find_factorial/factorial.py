#5=5*4*3*2*1 
n=int(input('factorial number'))
value=1
if n<=0:
    print('invalid')
for i in range(n,0,-1):
    value*=i 
print(value)

value=1
while(n>0):
    value*=n
    n-=1
print(value)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
result=factorial(5)
print(result)
