import csv

# Set the input path for the CSV file
input_filepath = "PyPoll/Resources/election_data.csv"

# Create variables to store the data
total_votes = 0
candidates = []
votes_by_candidate = {}

# Read in the CSV file
with open(input_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    next(csvreader)
    # Loop through each row of the CSV file
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        # Get the candidate's name from the row
        candidate_name = row[2]
        # If we haven't seen this candidate before, add them to the list of candidates
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            votes_by_candidate[candidate_name] = 0
        # Count the number of votes for this candidate
        votes_by_candidate[candidate_name] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Calculate the Vote Percentage
for candidate in candidates:
    votes = votes_by_candidate[candidate]
    vote_percentage = round(votes/total_votes*100, 3)
    print(f"{candidate}: {vote_percentage}% ({votes})")
print("-------------------------")
winner = max(votes_by_candidate, key=votes_by_candidate.get)
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file and define the output path
with open("PyPoll/Analysis/election_results.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate in candidates:
        votes = votes_by_candidate[candidate]
        vote_percentage = round(votes/total_votes*100, 3)
        textfile.write(f"{candidate}: {vote_percentage}% ({votes})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")