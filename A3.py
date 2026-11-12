
# IRCTC Ticket Booking Eligibility

age = int(input("Enter passenger age: "))
gender = input("Enter gender (male/female): ").lower()
traveling_alone = input("Are you traveling alone? (yes/no): ").lower()
tatkal = input("Are you booking a Tatkal ticket? (yes/no): ").lower()
blackout = input("Is it a festival blackout date? (yes/no): ").lower()

is_senior = age >= 60
is_female_alone = gender == "female" and traveling_alone == "yes"

is_eligible = (is_senior or is_female_alone) and tatkal == "no" and blackout == "no"

print("\n----- Ticket Eligibility -----")
print("Senior Citizen:", is_senior)
print("Female Traveling Alone:", is_female_alone)
print("Eligible for Special Benefits:", is_eligible)

if is_eligible:
    print("Passenger is eligible for lower berth preference and discount.")
else:
    print("Passenger is not eligible for special benefits.")
