from models.expense import Expense
from repository.expense_repository import ExpenseRepository


class ExpenseService:
    def __init__(self, repository: ExpenseRepository):
        self.repository = repository

    def add_expense(self, expense: Expense):
        expenses = self.repository.get_all()
        expenses.append(expense)
        self.repository.save_all(expenses)

    def get_all_expenses(self):
        return self.repository.get_all()

    def update_expense(self, expense_id: int, new_data: dict):
        expenses = self.repository.get_all()
        updated = False

        for i, expense in enumerate(expenses):
            if expense.expense_id == expense_id:
                updated_expense = Expense(
                    expense_id=expense.expense_id,
                    date=new_data.get("date", expense.date),
                    category=new_data.get("category", expense.category),
                    amount=new_data.get("amount", expense.amount),
                    note=new_data.get("note", expense.note),)
                expenses[i] = updated_expense
                updated = True
                break

        if not updated:
            raise ValueError(f"Expense with id {expense_id} not found")

        self.repository.save_all(expenses)


    def delete_expense(self, expense_id: int):
        expenses = self.repository.get_all()
        new_expenses = [e for e in expenses if e.expense_id != expense_id]

        if len(new_expenses) == len(expenses):
            raise ValueError(f"Expense with id {expense_id} not found")

        self.repository.save_all(new_expenses)
