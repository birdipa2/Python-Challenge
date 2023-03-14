import os
import csv

# Set up the input and output files
input_filepath="PyBank/Resources/budget_data.csv"
output_filepath="PyBank/Analysis/budget_data.txt"

# Initialize the variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the input file and process the data
with open(input_filepath,"r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        # Count the total number of months
        total_months+=1
         # Calculate the total profit/loss over the entire period
        total_profit_loss += int(row[1])

        # Calculate the change in profit/loss from the previous month
        current_profit_loss = int(row[1])
        if total_months > 1:
            profit_loss_change = current_profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            
            # Update the greatest increase and decrease in profits
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change
            
        previous_profit_loss = current_profit_loss

# Calculate the average change in profit/loss over the entire period
average_profit_loss_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Generate the output summary | the triple quotes (""") around the f-string indicate that it spans multiple lines.
output_summary = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss:,.2f}
Average Change: ${average_profit_loss_change:,.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})
"""

# Print the output summary to the console and write it to the output file
print(output_summary)
with open(output_filepath, "w") as txtfile:
    txtfile.write(output_summary)