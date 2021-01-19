import csv

def create(path_csv):
    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    tooley = 0
    winner = ""

    # Open and read the csv file
    with open(path_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")

        # Skipping the header
        next(csv_file)

        for row in csv_reader:
            total_votes = total_votes + 1

            if row[2] == "Khan":
                khan = khan + 1
            elif row[2] == "Correy":
                correy = correy + 1
            elif row[2] == "Li":
                li = li + 1
            elif row[2] == "O'Tooley":
                tooley = tooley + 1

        if khan > correy and khan > li and khan > tooley:
            winner = "Khan"
        
        if correy > khan and correy > li and correy > tooley:
            winner = "Correy"

        if li > khan and li > correy and li > tooley:
            winner = "Li"

        if tooley > khan and tooley > li and tooley > correy:
            winner = "Correy"

    data = {
        'total_votes': total_votes,
        'khan': khan,
        'correy': correy,
        'li': li,
        'tooley': tooley,
        'winner': winner
    }
    return data