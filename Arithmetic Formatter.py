import re
def arithmetic_arranger(problems_list,answer=False):

  #Number of problems check:
  if len(problems_list)>5:
      return "Error: Too many problems."

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
          return "Error: Operator must be '+' or '-'."
      try:
          # Try to convert the value to an integer
          int_value1 = int(num1)
          int_value2 = int(num2)
      except:
          return "Error: Numbers must only contain digits."

      len_max = max(len(num1),len(num2))
      if len_max>4:
          return "Error: Numbers cannot be more than four digits."

      seperator = ""
      for i in range(len_max+2):
          seperator = seperator+"-"

      solution = eval(problem)

      output1.append(f'{int(num1):{len_max+2}}')
      output2.append(f'{p}{int(num2):{len_max+1}}')
      output3.append(f'{seperator}')
      output4.append(f'{solution:{len_max+2}}')

  o1 = '    '.join(map(str, output1))
  o2 = '    '.join(map(str, output2))
  o3 = '    '.join(map(str, output3))
  Output_final=""
  if answer:
    o4 = '    '.join(map(str, output4))
    Output_final = f'{o1}\n{o2}\n{o3}\n{o4}'
  else:
    Output_final = f'{o1}\n{o2}\n{o3}'

        
  return Output_final
