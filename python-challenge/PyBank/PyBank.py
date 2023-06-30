import os
import csv

budget_data_2_csv = os.path.join("Resources", "budget_data.csv")
output_file = "financial_analysis.txt"

with open(budget_data_2_csv) as my_file, open(output_file, "w") as output:
    csv_reader = csv.reader(my_file, delimiter=",")

    # 1. CANTIDAD DE MESES EN LA DATA
    next(csv_reader, None)

    all_months = []

    for row in csv_reader:
        date = row[0]
        month = date.split("-")[0]  # para separar la data de fechas
        all_months.append(month)

    total_months = len(all_months)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months: {total_months}")
    print("Total months: {total_months}", file=output)

    my_file.seek(0)  # para mover el puntero de nuevo al inicio del file csv
    total = 0
    next(csv_reader, None)

    for row in csv_reader:
        profit_loss = int(row[1])
        total += profit_loss
    print(f"Total:  ${total}")
    print(f"Total:  ${total}", file=output)

    # 2. Sacar el change individual de cada periodo

    my_file.seek(0)
    changes = []
    next(csv_reader, None)

    previous_profit_loss = None
    percentage_changes = []

    for row in csv_reader:
        profit_loss = int(row[1])

        if previous_profit_loss is not None:
            percentage_change = (profit_loss - previous_profit_loss)
            percentage_changes.append(percentage_change)

        previous_profit_loss = profit_loss

    # Imprimir los porcentajes de cambio
    '''
    for percentage_change in percentage_changes:
        print(percentage_change)

    total_changes = len(percentage_changes)
    print(total_changes)
    '''
    # 3. promedio de total changes

    my_file.seek(0)
    changes_2 = []
    next(csv_reader, None)

    previous_profit_loss_2 = None
    percentage_changes_2 = []

    for row in csv_reader:
        profit_loss_2 = int(row[1])

        if previous_profit_loss_2 is not None:
            percentage_change_2 = (profit_loss_2 - previous_profit_loss_2)
            percentage_changes_2.append(percentage_change_2)

        previous_profit_loss_2 = profit_loss_2

    average_change = sum(percentage_changes_2) / len(percentage_changes_2)
    print("Average Change: $" + str(round(average_change, 2)))
    print("Average Change: $" + str(round(average_change, 2)), file=output)

    # 4.0 EL MAXIMO PROFIT DEL PERIODO - EXTRA

    my_file.seek(0)
    profits_looses = []
    next(csv_reader, None)

    for row in csv_reader:
        profit_loss_3 = int(row[1])
        profits_looses.append(profit_loss_3)

    max_profits = max(profits_looses)
    print(f"Greatest profit of the whole period (EXTRA): ${max_profits}")
    print(f"Greatest profit of the whole period (EXTRA): ${max_profits}", file=output)

    # 4. REAL The greatest increase in profits (date and amount) over the entire period

    my_file.seek(0)
    changes_4 = []
    next(csv_reader, None)

    previous_profit_loss_4 = None
    percentage_changes_4 = []

    for row in csv_reader:
        profit_loss_4 = int(row[1])

        if previous_profit_loss_4 is not None:
            percentage_change_4 = profit_loss_4 - previous_profit_loss_4
            percentage_changes_4.append(percentage_change_4)

        previous_profit_loss_4 = profit_loss_4

    max_profits_4 = max(percentage_changes_4)
    max_profits_date = ''

    # 4.1 REAL The greatest increase in profits (date and amount) over the entire period

    my_file.seek(0)
    next(csv_reader, None)

    for row in csv_reader:
        profit_loss_4 = int(row[1])

        if profit_loss_4 - previous_profit_loss_4 == max_profits_4:
            max_profits_date = row[0]
            break

        previous_profit_loss_4 = profit_loss_4

    print(f"Greatest Increase in Profits: {max_profits_date} {max_profits_4}")
    print(f"Greatest Increase in Profits: {max_profits_date} {max_profits_4}", file=output)

    # 5. REAL The greatest decrease in profits (date and amount) over the entire period

    my_file.seek(0)
    changes_5 = []
    next(csv_reader, None)

    previous_profit_loss_5 = None
    percentage_changes_5 = []

    for row in csv_reader:
        profit_loss_5 = int(row[1])

        if previous_profit_loss_5 is not None:
            percentage_change_5 = profit_loss_5 - previous_profit_loss_5
            percentage_changes_5.append(percentage_change_5)

        previous_profit_loss_5 = profit_loss_5

    min_profits_5 = min(percentage_changes_5)

    # 5.1 REAL The greatest decrease in profits (date and amount) over the entire period

    my_file.seek(0)
    next(csv_reader, None)

    for row in csv_reader:
        profit_loss_5 = int(row[1])

        if profit_loss_5 - previous_profit_loss_5 == min_profits_5:
            min_profits_date = row[0]
            break

        previous_profit_loss_5 = profit_loss_5

    print(f"Greatest Increase in Profits: {min_profits_date} {min_profits_5}")
    print(f"Greatest Increase in Profits: {min_profits_date} {min_profits_5}", file=output)
