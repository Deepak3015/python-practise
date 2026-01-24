from repository.expense_repository import ExpenseRepository
from services.expense_service import ExpenseService
from models.expense import Expense

repo = ExpenseRepository("expenses.csv")
service = ExpenseService(repo)

expense = Expense(3, "2024-01-25", "travel", 300, "auto")
service.add_expense(expense)

all_expenses = service.get_all_expenses()
print(all_expenses)
