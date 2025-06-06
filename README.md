
# 💰 Sonnic Tracker v1

**Sonnic Tracker** is a simple command-line savings tracker application written in Python. It allows users to register with a savings goal, deposit or withdraw money daily, and view progress toward their target.

---

## 🚀 Features

- 📝 Register new users with password and savings goals
- 🔐 Login system with password check
- 💸 Deposit and withdraw money with timestamps
- 📊 Dashboard to show:
  - Total saved
  - Days saved
  - Remaining balance to reach target
- 📃 Full transaction history view
- 📁 Data stored in `.txt` files (user and transaction data)

---

## 🛠 How to Run

1. Install Python (if not already)
2. Save the code to a file called `sonnic_tracker.py`
3. Run the program using:

```bash
python3 sonnic_tracker.py
```

---

## 👨‍💻 How It Works

1. User registers with:
   - Name
   - Password
   - Daily saving goal
   - Total savings target

2. Once logged in, user gets access to the menu:
   - `1. Deposit` → Save money
   - `2. Withdraw` → Remove money
   - `3. Dashboard` → View total saved and remaining
   - `4. View Account Details` → Full history
   - `5. Logout`

3. All data is saved in:
   - `users.txt` for user credentials
   - `data_<username>.txt` for transaction records

---

## 📂 Project Structure

```
sonnic_tracker.py
users.txt
data_<username>.txt
```

---

## 💡 Example Output

```
===== Sonnic Tracker =====
1. Register
2. Login
3. Exit
Choose an option: 1

Enter your name: Jisan
Set your password: ********
Daily saving goal (৳): 200
Total target (৳): 10000

Registration successful, Jisan!
```

---

## 🧠 Future Ideas (for next versions)

- Auto login session system
- Withdraw reasons
- History filtering (only deposits / withdrawals)
- GUI (Tkinter / web-based)
- Data backup and export
- Target achieved notification 🎯

---

## 📜 License

Free to use for learning and personal projects. Just give credit if you fork! 😉

---

## 🙌 Created By

Built with ❤️ by [Jisan] and [Chat Gpt AI].
