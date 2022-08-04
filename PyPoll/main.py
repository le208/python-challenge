import os
import csv
import textwrap


total_votes = 0
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

csvpath = "/Users/ninale/Desktop/python_challenge/python-challenge/PyPoll/Resources/election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes +1

        if row[2] == "Charles Casper Stockham":
            Charles_votes = Charles_votes +1
        elif row[2] == "Diana DeGette":
            Diana_votes = Diana_votes +1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_votes = Raymon_votes +1

names = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_votes, Diana_votes,Raymon_votes,]

dict_names_and_votes = dict(zip(names,votes))
winner = max(dict_names_and_votes, key=dict_names_and_votes.get)

Charles_percent = Charles_votes/total_votes*100
Diana_percent = Diana_votes/total_votes * 100
Raymon_percent = Raymon_votes/total_votes* 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

textpath = "/Users/ninale/Desktop/python_challenge/python-challenge/PyPoll/Analysis/Election_results.txt"

with open(textpath,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doan: {Raymon_percent:.3f}% ({Raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")




