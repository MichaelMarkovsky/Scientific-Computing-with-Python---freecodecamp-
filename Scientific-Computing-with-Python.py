import re
def arithmetic_arranger(problems_list,answer=False):
    #Number of problems check:
    if len(problems_list)>5:
        return print("Error: Too many problems.")

    output1 = []
    output2 = []
    output3 = []
    output4 = []

    for problem in problems_list:
        problem_split = re.split("\s",problem)#Split at each white-space character
        
        num1= problem_split[0]
        p= problem_split[1]
        num2= problem_split[2]

        #Error checks:
        if p =="*" or p =="/" or p==":":
            return print("Error: Operator must be '+' or '-'.")
        if type(num1) is not int or type(num2) is not int:
            return print("Error: Numbers must only contain digits.")
        len_max = max(len(num1),len(num2))
        if len_max>4:
            return print("Error: Numbers cannot be more than four digits.")

        seperator = ""
        for i in range(len_max+2):
            seperator = seperator+"-"

        solution = eval(problem)

        output1.append(f'{int(num1):{len_max+2}}')
        output2.append(f'{p}{int(num2):{len_max+1}}')
        output3.append(f'{seperator}')
        output4.append(f'{solution:{len_max+2}}')
        #print(f'{int(num1):{len_max+2}}\n{p}{int(num2):{len_max+1}}\n{seperator}\n{solution:{len_max+2}}')

    for problem in output1:
        print(problem+"    ",end="")
    print("")
    for problem in output2:
        print(problem+"    ",end="")
    print("")
    for problem in output3:
        print(problem+"    ",end="")
    
    if answer:
        print("")
        for problem in output4:
            print(problem+"    ",end="")


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","523 - 49",], True)
