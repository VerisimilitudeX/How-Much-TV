"""
LESSON: 1.3 - Expressions
EXERCISE: How Much TV?
"""

#### ---- INPUT ---- ####

# Get INPUT asking the user's age, then ASSIGN to
# the variable age
age = input("How old are you? ")

# Get INPUT asking for the average number of hours per
# day they spend watching videos, then ASSIGN to the
# variable hours
# ---> TEST AFTER THIS LINE <--- #
hours = input("How may hours do you spend each day watching TV? ")


#### ---- HOURS CALCULATION ---- ####

# MULTIPLY the number of hours per day (float) by the
# age of the person (int) by 365 (days in a year).
# ASSIGN to the variable total (Hint: TYPECAST)
# ---> TEST AFTER THIS LINE <--- #
total = float(hours) * int(age) * 365

# PRINT "Hours spent watching videos: " CONCATENATED
# with the total result (Hint: TYPECAST)
# ---> TEST AFTER THIS LINE <--- #
print("Hours spent watching videos: " + str(total))


#### ---- DAYS CALCULATION ---- ####

# DIVIDE the total result by 24 (hours in a day) to
# get how many days' worth of time that is. ASSIGN
# to a variable called days.
days = int(total/24)

# PRINT "That's " CONCATENATED with the days variable
# CONCATENATED with " days" (Hint: TYPECAST)
# ---> TEST AFTER THIS LINE <--- #
print("That's " + str(days) + " days!")


# Turn in your Coding Exercise.

