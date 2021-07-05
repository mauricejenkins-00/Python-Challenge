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
    
