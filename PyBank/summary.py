import csv

def create(path_csv):
    row_counter = 0
    total = 0
    greatest_increase = 0
    greatest_decrease = 0
    increase_label = ""
    decrease_label = ""

    # Open and read the csv file
    with open(path_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")

        # Skipping the header
        next(csv_file)

        for row in csv_reader:
            row_counter = row_counter + 1
            row_amount = int(row[1])
            total = total + row_amount

            if (greatest_increase < row_amount):
                greatest_increase = row_amount
                increase_label = row[0]

            if (greatest_decrease > row_amount):
                greatest_decrease = row_amount
                decrease_label = row[0]

    average_change = total / row_counter

    data = {
        'total_months': row_counter,
        'total_amount': total,
        'average_change': average_change,
        'greatest_increase': greatest_increase,
        'greatest_decrease': greatest_decrease,
        'increase_label': increase_label,
        'decrease_label': decrease_label
    }
    return data