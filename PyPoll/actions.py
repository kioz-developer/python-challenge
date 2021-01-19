def print_and_save(data):
    total_votes = data["total_votes"]
    percentage_khan = "{:,.3f}%".format((data['khan']*100)/total_votes) + f" ({data['khan']})"
    percentage_correy = "{:,.3f}%".format((data['correy']*100)/total_votes) + f" ({data['correy']})"
    percentage_li = "{:,.3f}%".format((data['li']*100)/total_votes) + f" ({data['li']})"
    percentage_tooley = "{:,.3f}%".format((data['tooley']*100)/total_votes) + f" ({data['tooley']})"
    winner = data["winner"]

    f = open("analysis.txt", "a")

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    print(f"Khan: {percentage_khan}")
    print(f"Correy: {percentage_correy}")
    print(f"Li: {percentage_li}")
    print(f"O'Tooley: {percentage_tooley}")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

    f.write("Election Results")
    f.write("\n----------------------------")
    f.write(f"\nTotal Votes: {total_votes}")
    f.write(f"\n----------------------------")
    f.write(f"\nKhan: {percentage_khan}")
    f.write(f"\nCorrey: {percentage_correy}")
    f.write(f"\nLi: {percentage_li}")
    f.write(f"\nO'Tooley: {percentage_tooley}")
    f.write(f"\n----------------------------")
    f.write(f"\nWinner: {winner}")
    f.write(f"\n----------------------------")

    f.close()
