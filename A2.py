
# 1. Myntra Shopping Discount Cart

print("Myntra Shopping Cart")

price1 = float(input("Enter first item price: "))
price2 = float(input("Enter second item price: "))

total = price1 + price2
discount = total * 15 / 100
delivery = 99
final_amount = total - discount + delivery

print("First item price:", price1)
print("Second item price:", price2)
print("Total price:", total)
print("Discount:", discount)
print("Delivery charge:", delivery)
print("Final amount to pay:", final_amount)


# 2. Cafe Outing Split-Bill Calculator

print("\nCafe Bill Calculator")

bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

tip = bill * 10 / 100
total_bill = bill + tip
per_person = total_bill / friends

print("Original bill:", bill)
print("Tip amount:", tip)
print("Total bill with tip:", total_bill)
print("Number of friends:", friends)
print("Amount per person:", round(per_person, 2))


# 3. Instagram Reel Engagement Tracker

print("\nInstagram Reel Report")

views = int(input("Enter total views: "))
likes = int(input("Enter total likes: "))
comments = int(input("Enter total comments: "))

engagement = ((likes + comments) / views) * 100

print("Total views:", views)
print("Total likes:", likes)
print("Total comments:", comments)
print("Total engagement:", likes + comments)
print("Engagement rate:", round(engagement, 2), "%")


# 4. Monthly Allowance and Savings Planner

print("\nMonthly Savings Planner")

pocket_money = float(input("Enter your monthly pocket money: "))

canteen = float(input("Enter canteen expenses: "))
transport = float(input("Enter transport expenses: "))
shopping = float(input("Enter shopping expenses: "))

total_expenses = canteen + transport + shopping
savings = pocket_money - total_expenses

is_budget_safe = savings >= 0

print("Monthly pocket money:", pocket_money)
print("Canteen expenses:", canteen)
print("Transport expenses:", transport)
print("Shopping expenses:", shopping)
print("Total expenses:", total_expenses)
print("Remaining savings:", savings)
print("Is budget safe:", is_budget_safe)
