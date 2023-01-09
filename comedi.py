 #Import necessary libraries
import csv

# Initialize variables
comedy_skits = []
votes = {}

# Read in the list of comedy skits from a CSV file
with open('comedy_skits.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        comedy_skits.append(row[0])
        votes[row[0]] = 0

# Prompt the user to vote for their favorite comedy skit
print("Which comedy skit is your favorite?")
for i, skit in enumerate(comedy_skits):
    print(f"{i+1}: {skit}")

# Get the user's vote
vote = input("Enter the number of your favorite skit: ")

# Add the vote to the tally
votes[comedy_skits[int(vote)-1]] += 1

# Print the results of the survey
print("Results:")
for skit, num_votes in votes.items():
    print(f"{skit}: {num_votes} votes")11