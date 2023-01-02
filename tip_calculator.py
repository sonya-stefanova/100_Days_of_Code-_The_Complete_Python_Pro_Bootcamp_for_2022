#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("The bill is: $"))
people = int(input("People at the table are: "))
tip_percent = float(input("Choose between 10%, 12%, 15%: %"))
total_bill_with_tip = bill*(tip_percent/100+1)
split_bill = total_bill_with_tip/people
print(f"Each person should pay {split_bill:.2f}")