class calculator:
    @staticmethod
    def fn_calculator(value1:int,operator:str,value2:int):
        """ 
        calculating two operands through a operator
        Args:
        value1:operand1:int
        operator: do arithmetic operation between two numbers:str
        value2:operand2:int

        Result:
        result of arithmatic operation:int
        """
        if(operator=='add'):
            result=value1 + value2
            return result
        #checking operator and doing arithmatic operation
        elif(operator=='subtract'):
            result=value1-value2
            return result
        elif(operator=='multiply'):
            result=value1*value2
            return result
        elif(operator=='divide'):
            result=value1/value2
            return result
        else:
            return 'invalid operator'
    input1=int(input('first value :\n'))
    operator=input('operator:add,subtract,multiply,divide : \n')
    input2=int(input('second value :\n'))
    value=fn_calculator(input1,operator,input2)
    print(value)
