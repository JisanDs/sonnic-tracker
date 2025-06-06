import datetime
import os

# Registration
def register_user():
    name = input("Enter your name: ")
    password = input("Set your password: ")
    per_day = input("Daily saving goal (৳): ")
    target = input("Total target (৳): ")

    with open("users.txt", "a") as f:
        f.write(f"{name},{password},{per_day},{target}\n")
    print(f"\nRegistration successful, {name}!\n")


# Dashboard (with optional full report)
def dashboard(name, per_day, target, full=False):
    filename = f"data_{name}.txt"
    total = 0
    days = 0
    history = []

    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                action, amount, date = line.strip().split(",")
                if action == "deposit":
                    total += int(amount)
                    days += 1
                elif action == "withdraw":
                    total -= int(amount)
                history.append((action, amount, date))
    else:
        print("\nNo transaction history yet. Start saving today!\n")

    remaining = int(target) - total
    print("\n===== Dashboard =====")
    print(f"Total Saved: ৳{total}")
    print(f"Days Saved: {days}")
    print(f"Target Remaining: ৳{remaining}")
    print("=====================")

    if full and history:
        print("\n=== Full Report ===")
        for h in history:
            print(f"{h[2]} — {h[0].capitalze()} ৳{h[1]}")
        print("===================")


# Deposit or Withdraw
def add_transaction(name, action):
    amount = input(f"Enter amount to {action}: ৳")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"data_{name}.txt"
    with open(filename, "a") as f:
        f.write(f"{action},{amount},{date}\n")
    print(f"{action.title()} of ৳{amount} added on {date}.\n")


# Login System
def login_user():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if not os.path.exists("users.txt"):
        print("No users found. Please register first.\n")
        return

    with open("users.txt", "r") as f:
        for line in f:
            uname, pwd, per_day, target = line.strip().split(",")
            if uname == name and pwd == password:
                print(f"\nWelcome back, {name}!")
                user_session(name, per_day, target)
                return

    print("Login failed. Incorrect name or password.\n")


# Logged-in User Menu
def user_session(name, per_day, target):
    while True:
        print("\n===== Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Dashboard")
        print("4. View Account Details")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(name, "deposit")
        elif choice == "2":
            add_transaction(name, "withdraw")
        elif choice == "3":
            dashboard(name, per_day, target)
        elif choice == "4":
            dashboard(name, per_day, target, full=True)
        elif choice == "5":
            print("Logging out...\n")
            break
        else:
            print("Invalid option.\n")


# Main Menu
def main():
    while True:
        print("\n===== Sonnic Tracker =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


# Run the program
main()