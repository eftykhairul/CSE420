# reading file input
file = open('read.txt','r')
line = str(file.read()).split()
#print(line)

# appending all the attributes in arrays
keywords = ['int', 'float', 'double', 'str', 'if', 'else', 'elif', 'for',
            'while', 'continue', 'break', 'pass', 'print']
math_operators = ['+', '-', '*', '/', '//', '=']
logical_operators = ['<', '<=', '>', '>=', '==', '!=']
numerical_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
others = [',', ';', '(', ')', '{', '}', '[', ']']

# for appending the outputs
store_key = []
store_id = []
store_mathop = []
store_logop = []
store_num = []
store_other = []


for i in line:

# keywords:
    if i in keywords:
        if i not in store_key:
            store_key.append(i)


    # math operators
    elif i in math_operators:
        if i not in store_mathop:
            store_mathop.append(i)


    # logical operators:
    elif i in logical_operators:
        if i not in store_logop:
            store_logop.append(i)


    # numerical values:
    if '0' < i[0] < '9':
        #print(i[0])
        if i[0:-1] not in store_num:
            store_num.append(i[0:-1])

    #other
    elif i[-1] in others:
        if i[-1] not in store_other:
            store_other.append(i[-1])

    #for identifier
        if i[0:-1] not in store_id:
            store_id.append(i[0:-1])



# for printing the output

print("Keywords: ", end="") 
print(*store_key, sep=", ")

print("Identifiers: ", end="")
print(*store_id, sep=" ")

print("Math Operators: ", end="")
print( *store_mathop, sep=", ")
print("Logical Operators: ", end="")
print( *store_logop, sep=", ")

print("Numerical Values: ", end="")
print(*store_num, sep=", ")

print("Others: " , end="" )
print(*store_other,sep=" ")