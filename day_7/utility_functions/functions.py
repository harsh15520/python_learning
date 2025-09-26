class Patterns:
    @staticmethod
    def pyramid(user_input):
        for i in range(1,user_input+1):
            print(' '*(user_input-i) + "* "*i)
    @staticmethod
    def inv_ryt_triangle(user_input):
        for i in range(user_input,0,-1):#numbers in one line
            for j in range(i,0,-1):#gets the values in each line
                print(j,end='')
            print()
    @staticmethod
    def ryt_triangle(user_input):
        for i in range(1,user_input+1):
            for j in range(1,i+1):
                print(i,end='')
            print()
class numbers:
    @staticmethod
    def multiplication(user_input1,user_input2,ranges):
        print("     ", end='')
        for i in range(1,ranges+1):
            print(f"{i:2}",end=' ')
        print()
        print('     '+('--- '*(ranges+1)))
        for j in range(user_input1,user_input2+1):
            print(f'{j:2} | ',end='')
            for i in range(1,ranges+1):
                print(''+f"{i*j:2}", end=' ')
            print()
