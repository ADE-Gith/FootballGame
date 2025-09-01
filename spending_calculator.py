#!/usr/bin/env python3
"""
Monthly Spending Calculator

A simple Python application to track and calculate monthly expenses.
"""

import json
import os
from datetime import datetime, date
from collections import defaultdict
from typing import Dict, List, Tuple


class SpendingCalculator:
    """A class to manage and calculate monthly spending."""
    
    def __init__(self, data_file: str = "spending_data.json"):
        """Initialize the spending calculator.
        
        Args:
            data_file: Path to the JSON file for storing expense data
        """
        self.data_file = data_file
        self.expenses = self.load_data()
    
    def load_data(self) -> List[Dict]:
        """Load expense data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_data(self) -> None:
        """Save expense data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=2, default=str)
    
    def add_expense(self, amount: float, category: str, description: str = "", date_str: str = None) -> None:
        """Add a new expense.
        
        Args:
            amount: The expense amount
            category: Category of the expense (e.g., 'food', 'transport', 'entertainment')
            description: Optional description of the expense
            date_str: Date in YYYY-MM-DD format, defaults to today
        """
        if date_str is None:
            expense_date = date.today()
        else:
            expense_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        expense = {
            "amount": float(amount),
            "category": category.lower(),
            "description": description,
            "date": expense_date.isoformat()
        }
        
        self.expenses.append(expense)
        self.save_data()
        print(f"Added expense: ${amount:.2f} for {category} on {expense_date}")
    
    def get_monthly_total(self, year: int = None, month: int = None) -> float:
        """Calculate total expenses for a specific month.
        
        Args:
            year: Year (defaults to current year)
            month: Month (1-12, defaults to current month)
            
        Returns:
            Total expenses for the month
        """
        if year is None:
            year = date.today().year
        if month is None:
            month = date.today().month
        
        total = 0.0
        for expense in self.expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
            if expense_date.year == year and expense_date.month == month:
                total += expense["amount"]
        
        return total
    
    def get_category_breakdown(self, year: int = None, month: int = None) -> Dict[str, float]:
        """Get spending breakdown by category for a specific month.
        
        Args:
            year: Year (defaults to current year)
            month: Month (1-12, defaults to current month)
            
        Returns:
            Dictionary with categories as keys and totals as values
        """
        if year is None:
            year = date.today().year
        if month is None:
            month = date.today().month
        
        breakdown = defaultdict(float)
        for expense in self.expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
            if expense_date.year == year and expense_date.month == month:
                breakdown[expense["category"]] += expense["amount"]
        
        return dict(breakdown)
    
    def get_monthly_summary(self, year: int = None, month: int = None) -> str:
        """Generate a summary report for monthly spending.
        
        Args:
            year: Year (defaults to current year)
            month: Month (1-12, defaults to current month)
            
        Returns:
            Formatted summary string
        """
        if year is None:
            year = date.today().year
        if month is None:
            month = date.today().month
        
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        
        total = self.get_monthly_total(year, month)
        breakdown = self.get_category_breakdown(year, month)
        
        summary = f"\n=== Monthly Spending Summary for {month_names[month-1]} {year} ===\n"
        summary += f"Total Spending: ${total:.2f}\n\n"
        
        if breakdown:
            summary += "Category Breakdown:\n"
            summary += "-" * 30 + "\n"
            for category, amount in sorted(breakdown.items()):
                percentage = (amount / total * 100) if total > 0 else 0
                summary += f"{category.capitalize():<15}: ${amount:>8.2f} ({percentage:>5.1f}%)\n"
        else:
            summary += "No expenses recorded for this month.\n"
        
        return summary
    
    def list_recent_expenses(self, days: int = 7) -> List[Dict]:
        """Get recent expenses within the specified number of days.
        
        Args:
            days: Number of days to look back
            
        Returns:
            List of recent expenses
        """
        cutoff_date = date.today()
        recent_expenses = []
        
        for expense in self.expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
            days_ago = (cutoff_date - expense_date).days
            if days_ago <= days:
                recent_expenses.append(expense)
        
        return sorted(recent_expenses, key=lambda x: x["date"], reverse=True)


def main():
    """Main CLI interface for the spending calculator."""
    calculator = SpendingCalculator()
    
    print("=== Monthly Spending Calculator ===")
    print("Commands:")
    print("1. add - Add a new expense")
    print("2. summary - Show monthly summary")
    print("3. recent - Show recent expenses")
    print("4. total - Show monthly total")
    print("5. quit - Exit the program")
    
    while True:
        try:
            command = input("\nEnter command (1-5): ").strip().lower()
            
            if command in ['1', 'add']:
                amount = float(input("Enter amount: $"))
                category = input("Enter category (e.g., food, transport, entertainment): ").strip()
                description = input("Enter description (optional): ").strip()
                
                date_input = input("Enter date (YYYY-MM-DD, or press Enter for today): ").strip()
                date_str = date_input if date_input else None
                
                calculator.add_expense(amount, category, description, date_str)
            
            elif command in ['2', 'summary']:
                print(calculator.get_monthly_summary())
            
            elif command in ['3', 'recent']:
                days = input("Enter number of days to look back (default 7): ").strip()
                days = int(days) if days else 7
                
                recent = calculator.list_recent_expenses(days)
                if recent:
                    print(f"\n=== Recent Expenses (Last {days} days) ===")
                    for expense in recent:
                        print(f"{expense['date']}: ${expense['amount']:.2f} - {expense['category']} - {expense['description']}")
                else:
                    print(f"No expenses found in the last {days} days.")
            
            elif command in ['4', 'total']:
                total = calculator.get_monthly_total()
                month_name = date.today().strftime("%B %Y")
                print(f"\nTotal spending for {month_name}: ${total:.2f}")
            
            elif command in ['5', 'quit', 'exit']:
                print("Goodbye!")
                break
            
            else:
                print("Invalid command. Please enter 1-5.")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()