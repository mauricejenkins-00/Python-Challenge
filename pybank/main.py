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
        
#Evaluate the max and min from the list made
increase = max(change_amount)
decrease = min(change_amount)

#Using the index, 
monthly_increases = change_amount.index(max(change_amount))+1
monthly_decreases = change_amount.index(min(change_amount))+1

output = (
   f"\n Financial Analysis \n"
   f"------------------------------\n"
   f"Total Months: {month_count}\n"
   f"Total: ${profit}\n"
   f"Average  Change: ${change_amount:}\n"
   f"Greatest Increase in Profits: {monthly_increases[0]} (${monthly_increases[1]})\n"
   f"Greatest Decrease in Profits: {monthly_decreases[0]} (${monthly_decreases[1]})\n")

with open(budget_file, "w") as txt_file_output:
   txt_file_output.write(output)  
   txt_file_output


