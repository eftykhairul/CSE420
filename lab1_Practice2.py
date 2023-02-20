
file = open('read.txt','r')
lines_List = file.read().split()
file.close()
keywords = ['int', 'float', 'if', 'else', 'elif', 'str']
keyword_out = []
math_operators = ["+", "-", "*", "/", "="]
math_operator_out = []
logical_operators = ['>', '<', '==']
logical_operator_out = []
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numeric = []
others = [',',';', '(', ')', '{', '}', '[', ']']
other_out = []

for i in range(len(lines_List)):
    print(i)
    if lines_List[i] in keywords:
        #print(lines_List[i])
        if lines_List[i] not in  keyword_out:
            keyword_out.append(lines_List[i])
        #print(keyword_out)
    elif lines_List[i] in math_operators:
        #print(lines_List[i])
        if lines_List[i] not in math_operator_out:
            math_operator_out.append(lines_List[i])
        #print(math_operator_out)
    elif lines_List[i] in logical_operators:
        #print(lines_List[i])
        if lines_List[i] not in logical_operator_out:
            logical_operator_out.append(lines_List[i])
    #if other operator
    
    elif lines_List[i][-1] in others:
        print(lines_List[i][-1])
        if lines_List[i][-1] not in other_out:
            other_out.append(lines_List[i][-1])

