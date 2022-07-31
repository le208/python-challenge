import os
import csv
import textwrap

csvpath = "/Users/ninale/Desktop/python_challenge/python-challenge/PyBank/Resources/budget_data.csv"

total_months =[]
total_profit_loss = []
monthly_profit_change =[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        total_profit_loss.append(int(row[1]))

    for i in range(len(total_profit_loss)-1): 
        monthly_profit_change.append(total_profit_loss[i+1]-total_profit_loss[i])

    greatest_increase_value = max(monthly_profit_change)
    greatest_decrease_value = min(monthly_profit_change)

    greatest_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
    
print("Financial Analysis")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit_loss)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")

textpath = "/Users/ninale/Desktop/python_challenge/python-challenge/PyBank/Analysis/Financial_analysis.txt"

with open(textpath,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit_loss)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")