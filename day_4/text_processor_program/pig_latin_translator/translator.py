def pig_latin(value):
    vowels = ['a','e','i','o','u']
    value = value.lower()
    if value[0] in vowels:
        return value + 'yay'
    else:
        for i, char in enumerate(value):
            if char in vowels:
                return value[i:] + value[:i] + 'ay'
        return value + 'ay'  # if no vowels found

def tokenizer(sentence):
    arr2=[]
    arr=sentence.split(" ")
    for word in arr:
        arr2.append(pig_latin(word))
    statement=" ".join(arr2)
    return statement
phrase=input("enter your sentence here \n ")
print(tokenizer(phrase))
