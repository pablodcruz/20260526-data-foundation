# Lab: Bank Account System (Simplified)

## Objectives
By completing this lab, students will be able to:
- Define classes with attributes and methods
- Use encapsulation (private attributes with getters/setters)
- Implement class inheritance
- Override methods in subclasses
- Use `@property` decorators

---

## Part 1: Base Class – `BankAccount`

### Instructions:
Create a `BankAccount` class with the following specifications:

#### Attributes (private)
- `__account_number` (string, readonly)
- `__owner_name` (string, readonly)
- `__balance` (float, private)

#### Methods
| Method | Description |
|--------|-------------|
| `__init__(account_number, owner_name, initial_balance=0)` | Constructor. Initializes all attributes. Print error if initial_balance < 0 and set balance to 0. |
| `deposit(amount)` | Adds amount to balance. Print error if amount ≤ 0. Returns new balance. |
| `withdraw(amount)` | Subtract amount if sufficient funds. Print error if amount ≤ 0 or insufficient balance. Returns new balance. |
| `get_balance()` | Returns current balance. |
| `get_account_info()` | Returns formatted string: `"Account X | Owner: Y | Balance: $Z"` |

#### Properties
- `account_number` (getter only – returns `__account_number`)
- `owner_name` (getter only – returns `__owner_name`)

### Test your class:
```python
# Example test code
acc = BankAccount("A123", "Alice", 100)
print(acc.get_account_info())     # Account A123 | Owner: Alice | Balance: $100
acc.deposit(50)                   # balance becomes 150
acc.withdraw(30)                  # balance becomes 120
print(acc.get_balance())          # 120

# Test error cases
acc.deposit(-10)                  # Should print error
acc.withdraw(500)                 # Should print error
```

---

## Part 2: Subclass – `SavingsAccount`

### Instructions:
Create a `SavingsAccount` class that **inherits** from `BankAccount`. Add:

#### Additional attributes
- `__interest_rate` (float, e.g., 0.03 for 3%)
- `__minimum_balance` (float, default = 50.0)

#### Overridden Methods
| Method | Behavior |
|--------|----------|
| `withdraw(amount)` | Prevent withdrawal if resulting balance < minimum_balance. Print error: `"Cannot withdraw. Minimum balance of $X must be maintained"` |
| `apply_interest()` | Adds interest to balance: `balance += balance * interest_rate` |

#### New Method
- `get_interest_rate()` – returns interest rate.

### Test your class:
```python
savings = SavingsAccount("S456", "Bob", 500, 0.05, 100)
print(savings.get_account_info())     # Account S456 | Owner: Bob | Balance: $500
savings.withdraw(450)                 # Should print error (minimum balance 100)
savings.apply_interest()              # Balance becomes 525
print(savings.get_balance())          # 525
```

---

## Part 3: Subclass – `CheckingAccount`

### Instructions:
Create a `CheckingAccount` class that inherits from `BankAccount`. Add:

#### Additional attributes
- `__overdraft_limit` (float, default = 100.0)

#### Overridden Method
| Method | Behavior |
|--------|----------|
| `withdraw(amount)` | Allows withdrawal below zero, but not below `-overdraft_limit`. Print error: `"Cannot withdraw. Overdraft limit would be exceeded"` |

#### New Methods
- `set_overdraft_limit(new_limit)` – updates the limit.
- `get_overdraft_limit()` – returns current limit.

### Test your class:
```python
checking = CheckingAccount("C789", "Carol", 50, 200)
checking.withdraw(100)                # balance becomes -50 (within overdraft)
print(checking.get_balance())         # -50
checking.withdraw(200)                # Should print error (-250 < -200 limit)
```

---

## Part 4: Bank Class (Composition)

### Instructions:
Create a `Bank` class that **manages multiple accounts**.

#### Attributes
- `__name` (string, bank name)
- `__accounts` (dictionary: account_number → account object)

#### Methods
| Method | Description |
|--------|-------------|
| `add_account(account)` | Adds account to bank. Print error if account_number already exists. |
| `find_account(account_number)` | Returns account object or `None`. |
| `transfer(from_acc_num, to_acc_num, amount)` | Transfer between accounts. Print error if either account not found or insufficient funds. |
| `get_total_balance()` | Returns sum of all account balances. |
| `get_accounts_by_type(account_type)` | Returns list of accounts of given type (e.g., `SavingsAccount`). |
| `display_all_accounts()` | Prints info for all accounts. |

### Test your class:
```python
my_bank = Bank("Python Federal Bank")
my_bank.add_account(BankAccount("A1", "Alice", 200))
my_bank.add_account(SavingsAccount("S1", "Bob", 300, 0.03, 50))
my_bank.add_account(CheckingAccount("C1", "Carol", 100, 150))

my_bank.display_all_accounts()

my_bank.transfer("A1", "S1", 50)      # Alice → Bob
print(f"Total bank balance: ${my_bank.get_total_balance()}")

savings_acc = my_bank.find_account("S1")
print(f"Bob's new balance: ${savings_acc.get_balance()}")  # Should be 350

# Test error cases
my_bank.transfer("A1", "X99", 10)     # Account not found error
my_bank.transfer("A1", "S1", 1000)    # Insufficient funds error
```