from models.expense import Expense
from repository.expense_repository import ExpenseRepository

class ExpenseService:

    def __init__(self,repositry:ExpenseRepository):
        self.repositry = repositry

    def add_expense(self,expense:Expense):
        expenses = self.repositry.get_all()
        expenses.append(expense)
        self.repositry.save_all(expenses)

    def get_all_expenses(self):
        return self.repositry.get_all()
