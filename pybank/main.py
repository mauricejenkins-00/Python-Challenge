import os
import csv


budget_data = os.path.join("..","Resources","budget_data.csv")

with open(budget_data) as budget_reader:

    budget_reader = csv.reader(budget_data, delimiter=',')
    print(budget_reader)


    