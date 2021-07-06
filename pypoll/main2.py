#Import libraries os, and Csv
import os
import csv

#Give canidates a variable to add the canidates and vote count to
candidates = {}

#election_csv is a variable that calls for the election data file in the resources folder
election_csv = os.path.join('.','Resources','election_data.csv')
#With statement opens the election_csv variable as csvfile and is set to read mode
with open(election_csv, 'r') as csvfile:
#csvreader is a variable set to opening the csv file and reading each row of data 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #The header variable is set to equal the next object in each column
#For loop is used to input data into spots in the dictionary we started earlier in the program called candidates
    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else: #If no value is returned then it sets the value to default 
            candidates[row[2]] = 1
#Sets the total candidates value equal to total so we can call for it later
        total = candidates.values()
#Sets the variable total_votes equal to the sum of candidates value
        total_votes = sum(total)

#List_candidates is just the dictionary keywords             
        list_candidates = candidates.keys()
#Here a variable is set equal to the equation used to calculate the votes per candidate            
        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
            
#Winner is a variable set equal to whoever has the highest amount of votes saved to the dictionary and prints it
        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        winner
        

#Prints the final results to the terminal
#Extra print statements are used to space out the output in the terminal
print("Election results")

print("--------------------------------")

print(f" Total votes: {int(total_votes)}")

print("---------------------------------")
i = 0
#For loop runs for candidate votes and goes for the length of all the candidate items 
#Prints the candidate name, the vote count, and the vote percentage they received 
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote} , {votes_per[i]}') 
    i+=1
#Prints the final result of who won the election
print("------------------------------")

print(f" Winner: {winner}")

print("------------------------------")
