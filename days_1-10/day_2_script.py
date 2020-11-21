print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? : "))
people_to_split = int(input("How many people to split the bill? : "))
precentage = int(input("What precentage tip would you like to give? (10%, 12%, 15%) : "))

tip_precentage = precentage / 100
total_tip = bill * tip_precentage
total_bill = bill + total_tip
per_person = total_bill / people_to_split

print(f"Each person should pay {round(per_person,2)}$")