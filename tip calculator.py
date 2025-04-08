print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#calculation

bill_with_tip = tip /100 * bill + bill
print(bill_with_tip)
bill_per_person = bill_with_tip/people
print(bill_per_person)
final_amount = round(bill_per_person, 2)

print(f"each person should pay ${final_amount}")

#using number system
a = int("5") / int(2.7)
b=int("5")
print(b)
c=int(2.7)
print(c)
print(a)
print(type(a))
