class Category:
  def __init__(self,budget_category) -> None:
      self.budget_category = budget_category #food, clothing, and entertainment. 
      self.ledger = []

  def deposit(self,amount,description=""):
      self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount,description=""):
      if self.check_funds(amount): 
          self.ledger.append({"amount": -amount, "description": description})
          return True
      else:
          return False

  def get_balance(self):
      amount_sum = 0
      for action in self.ledger:
          amount_sum+=action["amount"]
      return amount_sum

  def transfer(self,amount,budget_category):
      if self.check_funds(amount):
          self.withdraw(amount,f"Transfer to {budget_category.budget_category}")
          budget_category.deposit(amount,f"Transfer from {self.budget_category}")
          return True
      else:
          return False

  def check_funds(self,amount):
      if (self.get_balance() - amount) >=0: 
          return True
      else:
          return False

  def __str__(self):
      total_width = 30
      category_width = len(self.budget_category)

      # Calculate padding for centering
      padding = (total_width - category_width) // 2

      # Create centered title
      title_line = "*" * padding + self.budget_category + "*" * padding 

      items_list = ""

      for item in self.ledger:
          description_width_max = 24

          amount = "{:.2f}".format(item["amount"])

          description = (item["description"])[:23]
          description_width = len(description)

          # Calculate padding
          padding_description = (description_width_max - description_width)

          description_string = description + " " * padding_description
          amount_string = str(amount) #contain two decimal

          items_list += description_string + amount_string + "\n"

      return title_line + "\n" + items_list + "Total: " + str(self.get_balance())



def create_spend_chart(categories):
  chart_list = []
  number_list = []

  #insert number of percentages to the list (100,90,80..0)
  for num in range(100,-10,-10):
    number_list.append(num)

  total_withdraws = 0
  
  for category in categories:
    category_name = category.budget_category
    ledger = category.ledger
    for item in ledger:
      if item["amount"] < 0:
        total_withdraws+=item["amount"] * -1
        
  for category in categories:
    category_name = category.budget_category
    ledger = category.ledger
    
    total_withdraw=0
    total_withdraw=round(total_withdraw/10)*10 #round to the nearest 10
    #get all the withdraw amount and calculate the total
    for item in ledger:
      if item["amount"] < 0:
        total_withdraw+=item["amount"] * -1

    percentage_spent = (total_withdraw/total_withdraws)*100
    chart_list.append({"name": category_name, "percentage": percentage_spent})

  
  #print the chart
  result_str ="Percentage spent by category\n"
  for num in number_list:
    if num == 0:
      result_str += "  0|"
    else: 
      if num == 100:
        result_str += str(num)+"|"
      else:
        result_str += " "+str(num)+"|"
    
    for item in chart_list:
      if item["percentage"] >= num:
        result_str+=" o "
      else:
        result_str+="   "
    result_str+=" \n"
  result_str+="    "+"---"*(len(chart_list))+"-"+"\n"

  #print the names of the categories
  category_names = []
  for item in chart_list:
    name = item["name"]
    category_names.append(name[::-1])#append the string reversed 

  #print the strings upside down with spaces
  for i in range(len(max(category_names, key=len))):
    name_string="    "
    for n in category_names:
      name_string+=" "
      name_string += n[-(i + 1)] if i < len(n) else " "
      name_string += " "
    if i != range(len(max(category_names, key=len)))[-1]:
      result_str+=name_string+" \n"
    else:
      result_str+=name_string+" "

  return result_str
