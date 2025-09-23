with open('input.txt' ,'r', encoding='utf-8') as fileinput, \
    open('output.txt','w', encoding='utf-8') as fileoutput:
    arr=[]
    lines=fileinput.read().split('\n')
    for line in lines:
        word=line.strip()
        arr.append("*"+word)
    value='\n'.join(arr)
    fileoutput.write(value)
