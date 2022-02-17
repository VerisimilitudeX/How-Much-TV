age = input("How old are you? ")

hours = input("How may hours do you spend each day watching TV? ")

total = float(hours) * int(age) * 365

print("Hours spent watching videos: " + str(total))

days = int(total/24)

print("That's " + str(days) + " days!")
