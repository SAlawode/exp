# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:20:28 2022

@author: user
"""

class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
        #self.get_balance = get_balance
        
    def __str__(self):
        title = [self.category.center(30, "*")]
        for item in self.ledger:
            action = item["description"][:23].ljust(23) + ("{0:.2f}".format(item["amount"])[:7].rjust(7))
            title.append(action)
        return "\n".join(title) + "\n" + "Total: " + "{0:.2f}".format((self.get_balance()))
    
  
    def deposit(self, amount, description=""):
        try:
            self.ledger.append({"amount": (amount), "description": description})
            #self.get_balance += amount
        except ValueError:
            print("Invalid deposit amount")
            pass
        
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": (-amount), "description": description})
            #self.get_balance -= amount
            return True
        else:
            #raise ValueError("Insufficient funds")
            return False
        
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.category}")
            destination.deposit(amount, f"Transfer from {self.category}")
            return True
        
        return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False 
        return True
        
  

    def get_balance(self):
        balance = 0
        for x in self.ledger:
            balance += x["amount"]
        return balance
            


        
def create_spend_chart(categories):

  
    output = "Percentage spent by category\n"
    
    total = 0
    labels = []
    expenses = []
    len_labels = 0
    
    for item in categories:
        
        expense = sum([-x["amount"] for x in item.ledger if x["amount"] < 0])
        
        total += expense
        
        if len(item.category) > len_labels:
            len_labels = len(item.category)
            
        
        expenses.append(expense)
        labels.append(item.category)
        #print(expenses, item.category)
        
        
    #print(len_labels)
    expenses = [int(((x/total)*100))for x in expenses]
    labels   = [label.ljust(len_labels, " ") for label in labels]
    #print(labels)
    #print(expenses)
    
    
    for f in range(100, -1, -10):
        output += str(f).rjust(3, " ")  + "|"
        
        for p in expenses:
            output += " o " if p >= f else "   "
        output += " \n"
    
    output += "    " + "---"*len(labels) + "-\n"
    
    
    for i in range(len_labels):
        output += "    "
        for label in labels:
            output += " " + label[i] + " "
        output += " \n"

        
    return output.strip("\n")



    
                
    
    
        

def main():
    food = Category("Food")
    food.deposit(900, "deposit")
    entertainment = Category("Entertainment")
    entertainment.deposit(900, "deposit")
    business = Category("Business")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(create_spend_chart([business, food, entertainment]))

    
   
    
if __name__=="__main__":
    main()