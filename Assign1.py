import time

# initial prompting + title
print("Inflation Calculator\n\n\n\n")
time.sleep(1)

year = int(input("Please input the year you would like to calculate the personal interest for:  "))
pre = year - 1

excat = int(input("Please input the number of expenditure categories:  "))

# constants
count = 0
tocuryearex = 0
topreyearex = 0

# input loop
while count != excat:
    curyearex = int(input("Please enter the expenses for %d : " % year))
    preyearex = int(input("Please enter the expenses for %d : " % pre))
    count = count + 1

    # current and previous year accumulators
    tocuryearex = tocuryearex + curyearex
    topreyearex = topreyearex + preyearex


# the formula
inflation = ((tocuryearex - topreyearex) / tocuryearex) * 100


# making it only have 2 decimal places
final = inflation // 1
print("The inflation rate for {} is {}%.".format(year, final))

# inflation level
if final < 3:
    print("Inflation rate level: low")
elif 3 <= final < 5:
    print("Inflation rate level: moderate")
elif 5 <= final < 10:
    print("Inflation rate level: high")
elif final >= 10:
    print("Inflation rate level: hyper")

# if something somehow goes wrong
else:
    print("Unknown levels of inflation")
