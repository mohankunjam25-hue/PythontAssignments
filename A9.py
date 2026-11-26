
goals = []

def add_goal():
    title = input("Enter your goal: ")

    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")

    choice = input("Select goal type: ")

    if choice == "1":
        category = "Daily"
    elif choice == "2":
        category = "Weekly"
    elif choice == "3":
        category = "Monthly"
    else:
        print("Invalid choice!")
        return

    goal = {
        "title": title,
        "category": category,
        "status": "Pending"
    }

    goals.append(goal)
    print("Goal added successfully!")


def view_goals():
    if len(goals) == 0:
        print("No goals available.")
        return

    for index, goal in enumerate(goals, start=1):
        print(f"\n{index}. {goal['title']}")
        print("Category:", goal["category"])
        print("Status:", goal["status"])


def complete_goal():
    view_goals()

    if len(goals) == 0:
        return

    number = int(input("\nEnter goal number to complete: "))

    if 1 <= number <= len(goals):
        goals[number - 1]["status"] = "Completed"
        print("Goal completed successfully!")
    else:
        print("Invalid goal number.")


def delete_goal():
    view_goals()

    if len(goals) == 0:
        return

    number = int(input("\nEnter goal number to delete: "))

    if 1 <= number <= len(goals):
        goals.pop(number - 1)
        print("Goal deleted successfully!")
    else:
        print("Invalid goal number.")


while True:
    print("\n===== GOAL SHARING TODO APP =====")
    print("1. Add Goal")
    print("2. View Goals")
    print("3. Complete Goal")
    print("4. Delete Goal")
    print("5. Exit")

    option = input("\nEnter your choice: ")

    if option == "1":
        add_goal()

    elif option == "2":
        view_goals()

    elif option == "3":
        complete_goal()

    elif option == "4":
        delete_goal()

    elif option == "5":
        print("Thank you for using Goal Sharing App!")
        break

    else:
        print("Invalid option. Try again.")
