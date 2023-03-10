import re

file = open('read.txt','r')
read_file = str(file.read())
reSp = read_file.split()

arr_key = ['int', 'float', 'if', 'else', 'elif', 'str']
keywords = []
math_ope = ["+", "-", "*", "/", "="]
math_operation = []
log_ope = ['>', '<', '==']
logic_Operator = []
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '6.0', '2.0']
numeric = []
other = [',',';', '(', ')', '{', '}', '[', ']']
others = []
identifier_out = []


for i in reSp:
    #for keywords
    if i in arr_key:
        if i not in keywords:
            keywords.append(i)
        else:
            pass
    #for mathmetical Operator
    elif i in math_ope:
        if i not in math_operation:
            math_operation.append(i)
        else:
            pass
    #for Logical operator
    elif i in log_ope:
        if i not in logic_Operator:
            logic_Operator.append(i)
        else:
            pass
    #for numerical number
    elif i[0] in digit:
        if i[0:-1] not in numeric:
            numeric.append(i[0:-1])
        else:
            pass
    #for other
    elif i[-1] in other:
        if i[-1] not in others:
            others.append(i[-1])
    #for identifier
    else:
        x = re.findall("[a-zA-Z]", i)
        if x not in identifier_out:
            identifier_out.append(x)

print("keywords:", *keywords)
print("Identifiers:",','.join(''.join(i) for i in identifier_out))
print("Math Operators:",','.join(math_operation))
print("Logical Operators:",','.join(logic_Operator))
print("Numerical Values:",','.join(numeric))
print("Others:",' '.join(others))
