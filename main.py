#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill= int(input("Bill please? \n"))
people= int(input("How many peopple?"))
bill = (bill+(12/100)*bill)
billperperson =round(bill/people,2)
final_amount= "{:.2f}".format(billperperson)
print(f"So each person is going to pay $ {billperperson}")