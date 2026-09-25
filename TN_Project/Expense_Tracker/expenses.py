import json

try:
    with open("output.json", "r") as json_file:
        expenses = json.load(json_file)
    print("Previous expenses loaded!")
except (FileNotFoundError,json.JSONDecodeError):
    expenses = []

print("==========================\nwelcome to EXPENSE TRACKER\n==========================")

def add_expense():
    while True:
        try:
            amount = int(input("Enter a positive number amount: "))
            if amount <= 0:
                print("That number you entered is not positive. Try again.\n")
                continue

        except ValueError:
            print("Invalid input. Please enter valid digits for the amount.\n")
            continue

        category = input("Enter category: \n").strip()
        if not category:
            print("Category cannot be empty. Try again.\n")
            continue
            
        description = input("Enter description: \n").strip()

        new_expense = {
            "id": len(expenses) + 1,
            "amount": amount,
            "category": category,
            "description": description,
        }
        expenses.append(new_expense)
        print("Expense added successfully!\n")
        save_data()
        break

def view_all():
    print("--- view expenses ---")
    if len(expenses) <= 0:
        print("no expenses to view ")
    else:
        for exp in expenses:
            print(f"ID:{exp['id']} | {exp['amount']} - {exp['category']} - {exp['description']}")
        print()

def view_single():
    target = input("Enter expense ID: \n").strip()

    if len(target)<= 0:
        print("please enter a value!!!")
    else:
        for exp in expenses :
            print(f"ID: {exp["id"]} | {exp['amount']} - {exp["category"]} - {exp['description']}")

def total_spending():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending = {total}\n")

def spending_by_category():
    target = input("Enter category to calculate: \n").strip()
    total = 0
    found = False
    for exp in expenses:
        if exp["category"].lower() == target.lower():
            total += exp["amount"]
            found = True
    if found:
        print(f"Total for {target} = {total}\n")
    else:
        print("Category not found\n")

def delete_expense():
    try:
        target = int(input("Enter expense ID to delete: \n"))
        found = False
        for exp in expenses:
            if exp.get("id") == target:
                expenses.remove(exp)
                found = True
                print("Expense successfully deleted\n")
                save_data()
                break
                
        if not found:
            print("ID not found\n")
                
    except ValueError:
        print("Please enter a valid numeric ID\n")

def save_data():
    with open("output.json", "w") as json_file:
        json.dump(expenses, json_file, indent=4)
    print("Data saved successfully!\n")

def main():
    while True:
        choice = input("Enter:\n 1. Add Expense \n 2. View all Expense \n 3. View single Expense \n 4. Calculate Total Expense \n 5. Total Expense by category \n 6. Delete Expense \n 7. Exit\n\n")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            view_single()
        elif choice == "4":
            total_spending()
        elif choice == "5":
            spending_by_category()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Bye-bye, thanks!")
            break
        else:
            print("Invalid option, enter 1-7\n")

main()