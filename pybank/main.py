#Imports the os system and csv library
import os
import csv

#Sets a variable equal to the file path to call upon a data set
budget_file = os.path.join("Resources","budget_data.csv")
#Sets the original variable contents equal to budget_reader to read through rows completely
with open(budget_file) as budget_reader:
    budget_reader = csv.reader(budget_file, delimiter = ',')
    header = next(budget_reader)
    print(f"{header}")
    
#Create empty lists to add the csv values to 
    month_count = []
    profit = []
    change_amount = []
   
#Iterate through the values and add them to the empty list 
    for row in budget_reader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_amount.append(profit[i+1]-profit[i])
