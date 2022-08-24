import csv
import os

# get current working directory
#current_directory = os.getcwd()
#print(current_directory)

#get the contents of directory
#contents = os.listdir(current_directory)
#print(contents)

#Assign a variable for the file to load from a  path
#file_to_load = "/Users/sandeep/Desktop/Analysis Projects/Election_Analysis/Resources/election_results.csv" 
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
#file_to_save = "/Users/sandeep/Desktop/Analysis Projects/Election_Analysis/analysis/election_analysis.txt"
file_to_save = os.path.join("analysis", "election_analysis.txt")

#total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read and print the header row
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.    
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print the candidate name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        # Determine winning data
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)    

#print(candidate_votes);


    

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-----------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    