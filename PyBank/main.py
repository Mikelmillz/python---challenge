import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")
# print(bank_csv)

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    

    next(csvreader)

    profit_loss = []
    months = []


    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
    total_months = len(months)
    sum_ammount = sum(profit_loss)
    ammount = []

    for i in range(1, total_months):
        ammount.append(profit_loss[i] - profit_loss[i-1])

    ave_change = sum(ammount) / len(ammount)
    max_prof = max(ammount)
    min_loss = min(ammount)

    max_month = months[ammount.index(max_prof) + 1]
    min_month = months[ammount.index(min_loss) + 1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum_ammount}")
print(f"Average Change: ${round(ave_change, 2)}")
print(f"Greatest Increase in Profits: {max_month} ({max_prof})")
print(f"Greatest Decrease in Profits: {min_month} ({min_loss})")

file = open("Export.txt","w")
file.write("Financial Analysis" + '\n')
file.write(f"----------------------------\n")
file.write(f"Total Months: {total_months}"+"\n")
file.write(f"Total: ${sum_ammount}"+"\n")
file.write(f"Average Change: ${round(ave_change, 2)}"+"/n")
file.write(f"Greatest Increase in Profits: {max_month} ({max_prof})"+"\n")
file.write(f"Greatest Decrease in Profits: {min_month} ({min_loss})"+"\n")
file.close
