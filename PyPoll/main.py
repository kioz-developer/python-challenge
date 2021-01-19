import os
import summary
import actions

path_csv = os.path.join("Resources", "election_data.csv")

# Create the summary over the dataset
data = summary.create(path_csv)

# Print to the terminal and export a text file
actions.print_and_save(data)