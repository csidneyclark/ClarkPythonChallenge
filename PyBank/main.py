import os
import csv
#locating data file
file = os.path.join("budget_data.csv")


#declaring variables
total_months = 0
total_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

#created prev_pl to track profit/loss of previous month
prev_pl = 0
#list of pl changes from month to month
changes = []

# open file and read data with csv.reader; save header row
with open(file) as data: 
    #readcsv
    csvreader = csv.reader(data, delimiter = ',')
    #skip header in csv data
    header = next(csvreader)

    #for loop to run through data
    for row in csvreader:
        date = row[0]
        pl = int(row [1])
        #take total profit, add pl, then store it back in total profit
        total_profit += pl
        #every time you go through row, adding 1 to the total_months count
        total_months += 1

        #taking the current month's P/L and comparing it to the month prior
        #if this is first month, get rid of value
        change = pl - prev_pl
        if total_months != 1:
        #every time we calculate a change from month to month it gets added to list
            changes.append(change)
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = date     
        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = date   
        #resetting to the next month
        prev_pl = pl 
         
#calculating average change
avg_change = (round(sum(changes)/len(changes), 2))

#calculating monthly average profit
monthlyaverage_profit =int(round(total_profit/total_months, 0))


analysis = (
f"Total Profit: ${total_profit}\n"
f"Total Months: {total_months}\n"
f"Average Monthly Change: ${avg_change}\n"
f"Greatest Increase: {greatest_inc_month}, ${greatest_inc}\n"
f"Greatest Decrease: {greatest_dec_month}, ${greatest_dec}")

print(analysis)

#export to text file
file = open("PyBankoutput.txt", "w")
file.write(analysis)
file.close()