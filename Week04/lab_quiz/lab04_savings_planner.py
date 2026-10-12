while True:
    starting_balance = float(input("Enter starting balance: "))
    if starting_balance >= 0:
        break
    print("Starting balance cannot be negative. Try again.")

while True:
    monthly_deposit = float(input("Enter monthly deposit: "))
    if monthly_deposit > 0:
        break
    print("Monthly deposit must be positive. Try again.")

while True:
    interest_rate = float(input("Enter monthly interest rate (%): "))
    if interest_rate >= 0:
        break
    print("Interest rate cannot be negative. Try again.")

while True:
    savings_goal = float(input("Enter savings goal: "))
    if savings_goal > 0:
        break
    print("Savings goal must be positive. Try again.")

if starting_balance >= savings_goal:
    print("\nStarting balance already meets or exceeds the savings goal!")
    print(f"Final Balance: ${starting_balance:.2f}")
else:
    balance = starting_balance
    total_interest = 0.0
    goal_reached = False
    months = 0

    print("\nMonth | Interest Earned | New Balance")
    print("-" * 38)

    for month in range(1, 61):
        months = month
        interest_earned = balance * (interest_rate / 100)
        total_interest += interest_earned
        balance += interest_earned + monthly_deposit

        print(f"{month:<5} | ${interest_earned:>14.2f} | ${balance:>10.2f}")

        
        if balance >= savings_goal:
            goal_reached = True
            break

    print("-" * 38)
    if goal_reached:
        print(f"Goal reached in {months} month(s)!")
    else:
        print("Goal was NOT reached within 60 months.")

    print(f"Final Balance: ${balance:.2f}")
    print(f"Total Interest Earned: ${total_interest:.2f}")
