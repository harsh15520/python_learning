grade=input("enter your grade:A,B,C,D,E,F")
value=['a','b','c','d','e','f']
def grade_calculator(grade):
    if(grade.lower() in value):
        if(grade.lower() in value[:3]):
            if(grade.lower()=='a'):
                statement='topper'
                return statement
            elif(grade.lower()=='b'):
                statement='above average'
                return statement
            else:
                statement="average"
                return statement
        else:
            if(grade.lower()=='d'):
                statement='poor'
                return statement
            elif(grade.lower()=='e'):
                statement='very poor'
                return statement
            else:
                statement="fail"
                return statement

    else:
        statement="invalid input"
        return statement

# Call the function and print the result
result = grade_calculator(grade)
print(result)
