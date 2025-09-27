class convertor:
    @staticmethod
    def temperature_convertor(temperature:int,unit1:str,unit2:str):
        """ 
        convert given temperature from unit 1 to unit 2
        Args:
        -temperature:int:value of temperature
        -unit1:str:current unit of temperature
        -unit2:str:to be converted in this unit
        Result:
        -temperature provided in converted unit
        """
        if(unit1=='F' and unit2=='C'):
            value=(temperature-32)*5/9
            return value
        elif(unit1=='C' and unit2=='F'):
            value=temperature+273.15
            return value
        else:
            return 'wrong unit'
