import csv
import os

#Assign a variable to load a file from a  path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare dictionary to hold candidate name and votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)
    
    # Iterate through the data in CSV file 
    for row in file_reader:
        # Add to total vote count
        total_votes += 1

        # Get the candidate name from each row 
        candidate_name = row[2]
       
        # Add to candidate list , if candidate not in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Set votes to zero for the new candidate
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save results as a text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)  

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
            
        # Print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
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
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    