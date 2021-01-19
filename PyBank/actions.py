def print_and_save(data):
    months = data["total_months"]
    total = "${:,.2f}".format(data['total_amount'])
    average = "${:,.2f}".format(data['average_change'])
    increase = f"{data['increase_label']} (" + "${:,.2f}". format(data['greatest_increase']) + ")"
    decrease = f"{data['decrease_label']} (" + "${:,.2f}". format(data['greatest_decrease']) + ")"
    
    f = open("analysis.txt", "a")

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months: {months}")
    print(f"Total: {total}")
    print(f"Average  Change: {average}")
    print(f"Greatest Increase in Profits: {increase}")
    print(f"Greatest Decrease in Profits: {decrease}")

    f.write("Financial Analysis")
    f.write("\n----------------------------")
    f.write(f"\nTotal months: {months}")
    f.write(f"\nTotal: {total}")
    f.write(f"\nAverage  Change: {average}")
    f.write(f"\nGreatest Increase in Profits: {increase}")
    f.write(f"\nGreatest Decrease in Profits: {decrease}")

    f.close()
