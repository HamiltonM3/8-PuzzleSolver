#Option #2: Stepwise Refinement Approach
#Develop a check writer that, given a numeric dollar amount, will print the amount in words normally required on a check.

#Written by Michael Hamilton
#July 29, 2022
#CSC 505-1 

#Welcome Message

from num2words import num2words

print("Welcome to your Module 6 Check Writer:") 
Pay = input("Enter who the check will be written out to: ")
UserInput = input("Enter the amount of the checkin Euros: ")
print(num2words(UserInput, to = 'currency'))
print("The check is paid to",Pay,"in the amount of",num2words(UserInput, to = 'currency'))
Close = input("Press Enter to end the session")

