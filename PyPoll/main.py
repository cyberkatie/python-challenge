#import dependencies
import os
import csv
import pandas as pd

#creates file path
file_path = "Resources/election_data.csv"

#reads in csv file and creates a list of all votes
vote_cast = []
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for line in csvreader:
        vote_cast.append(line[2])

#declare variables for candidates
charles = 0
diana = 0
raymon = 0

#loops through the votes and counts each candidates' votes
for i in range(len(vote_cast)):
    if (vote_cast[i] == 'Charles Casper Stockham'):
        charles += 1
    elif (vote_cast[i] == 'Diana DeGette'):
        diana += 1
    elif (vote_cast[i] == 'Raymon Anthony Doane'):
        raymon += 1
 #print each candidates results       
print(charles)
print(diana)
print(raymon)

#find the number of votes
num_vote = len(vote_cast)

number_of_votes = [charles, diana, raymon]
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

#finds the index of the max number of votes
ind = number_of_votes.index(max(number_of_votes))

#prints results
print(f"total votes: {len(vote_cast)}")
print(f"Charles Casper Stockham: {(charles/num_vote)*100}% ({charles})")
print(f"Diana DeGette: {diana/num_vote*100}% ({diana})")
print(f"Raymon Anthony Doane: {raymon/num_vote*100}% ({raymon})")
print(f"the winner is: {candidates[ind]}")

#export results as a .txt file
pypoll_output = open("pypoll.txt", "w")
L = ["election results", " ",
    f"total votes: {len(vote_cast)}", " ",
    f"Charles Casper Stockham: {(charles/num_vote)*100}% ({charles})", " ",
    f"Diana DeGette: {diana/num_vote*100}% ({diana})", " ",
    f"Raymon Anthony Doane: {raymon/num_vote*100}% ({raymon})", " ",
    f"the winner is: {candidates[ind]}"]

pypoll_output.writelines(L)
pypoll_output.close()

shutil.move("pypoll.txt", "analysis" )