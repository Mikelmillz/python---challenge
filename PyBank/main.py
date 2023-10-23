#importing what we will need.
import os
import csv

#reading the file provided.
bank_csv = os.path.join("Resources", "budget_data.csv")

#opening the file that was privided.
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    #making sure the the header doesn't mess up my code
    next(csvreader)

    #creating empty arrays to hold lists
    profit_loss = []
    months = []

    #creating variables to hold the rows.
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    #creating the variable that will store the answers    
    total_months = len(months)
    sum_ammount = sum(profit_loss)
    amount = []
    
    #creating a for loop that will go through the profit/losses column and store the difference in the amount list.
    for i in range(1, total_months):
        amount.append(profit_loss[i] - profit_loss[i-1])

    #Making the variable that will hole then average change, max proffit and most lost in a month.
    ave_change = sum(amount) / len(amount)
    max_prof = max(amount)
    min_loss = min(amount)

    #creating the months that are based off the max profit and loss.
    max_month = months[amount.index(max_prof) + 1]
    min_month = months[amount.index(min_loss) + 1]

#displaying the data that we are wanting
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum_ammount}")
print(f"Average Change: ${round(ave_change, 2)}")
print(f"Greatest Increase in Profits: {max_month} ({max_prof})")
print(f"Greatest Decrease in Profits: {min_month} ({min_loss})")

#creating a file with our output data
file = open("Export.txt","w")
file.write("Financial Analysis" + '\n')
file.write(f"----------------------------\n")
file.write(f"Total Months: {total_months}"+"\n")
file.write(f"Total: ${sum_ammount}"+"\n")
file.write(f"Average Change: ${round(ave_change, 2)}"+"/n")
file.write(f"Greatest Increase in Profits: {max_month} ({max_prof})"+"\n")
file.write(f"Greatest Decrease in Profits: {min_month} ({min_loss})"+"\n")
file.close
