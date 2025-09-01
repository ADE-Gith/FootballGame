# FootballGame

This repository contains two applications:

## 1. Football Game Simulator
A Flask web application that simulates football matches between two teams.

### Usage
```bash
python3 test.py
```
Then visit `http://localhost:5000/simulate_game` to see a simulated game.

## 2. Monthly Spending Calculator
A Python application to track and calculate monthly expenses with category breakdown.

### Features
- Add expenses with categories and descriptions
- Calculate monthly totals
- Category-wise spending breakdown
- Recent expenses tracking
- Data persistence using JSON

### Usage
```bash
python3 spending_calculator.py
```

### Commands
1. **add** - Add a new expense
2. **summary** - Show monthly summary with category breakdown
3. **recent** - Show recent expenses (configurable days)
4. **total** - Show current month's total spending
5. **quit** - Exit the program

### Example
```bash
$ python3 spending_calculator.py
=== Monthly Spending Calculator ===
Enter command (1-5): 1
Enter amount: $50.00
Enter category: food
Enter description: Grocery shopping
Enter date (YYYY-MM-DD, or press Enter for today): 
Added expense: $50.00 for food on 2024-09-01
```