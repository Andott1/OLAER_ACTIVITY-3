# Program converts user input integer to minutes and seconds

# Prompts user to input an integer
Time = int(input("Enter an integer for seconds: "))

# Conversion rate
CONV1 = 60

# Calculation for minutes
Minutes = Time // CONV1

# Calculation for remainder seconds
Seconds = Time % CONV1

print(str(Time) + " seconds is " + str(Minutes) + " minutes," +
      " and " + str(Seconds) + " seconds.")
