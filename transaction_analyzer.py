data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

#print_transactions(data)

def print_summary(transactions):
  # Calculating total deposits by going through the data
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposits = sum(deposits)
  print(f'The total deposits are {total_deposits}')
  # Calculating total withdraws by going through the data  
  withdraws = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdraws = sum(withdraws)
  print(f' The total withdraws are {total_withdraws}')
  # Calculating final balance from withdraws and deposits  
  balance = total_deposits + total_withdraws
  print(f'The total balance is {balance}')

#print_summary(data)

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdraw = transactions[0]
  largest_deposit = transactions[-1]
  print(f'The largest withdraw is {largest_withdraw}')
  print(f'The largest deposit is {largest_deposit}')
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  if len(deposits) == 0:
    avg_deposits = 0
  else:
    total_deposits = sum(deposits)
    avg_deposits = total_deposits/ len(deposits)
  print(f'The average deposit is {avg_deposits}')
  withdraws = [transaction[0] for transaction in transactions if transaction[0] < 0]
  if len(withdraws) == 0:
    avg_withdraws = 0
  else:
    total_withdraws = sum(withdraws)
    avg_withdraws = total_withdraws/ len(withdraws)
  print(f'The average withdraws is {avg_withdraws}')

#analyze_transactions(data)

print("\nTransaction Analyzer")
while True:
  choice = input("Choose to 'print' a summarized statement, 'analyze' transactions, or 'stop' the program: ").strip().lower()
  if choice == "print":
    print()
    print_summary(data)
    print()
  elif choice == 'analyze':
    print()
    analyze_transactions(data)
    print()
  elif choice == 'stop':
    break
  else:
    print()
    print('Not a valid request.')
    print()
