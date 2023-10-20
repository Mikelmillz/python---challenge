import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")
# print(bank_csv)

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

for row in csvreader:
   sum_row = sum(row)
   print(row)
