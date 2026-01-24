import csv
import os
from day11.expense_tracker.models.expense import Expense

class ExpenseRepositry:

    def __init__(self,file_path:str):
        self.file_path = file_path

    def _ensure_file_exist(self):
        if not os.path.exist(self.file_path):
            with open(self.file_path,mode = "w",newline="") as file:
                writer = csv.DictWriter(file,fieldnames=["id","date","category","amount","note"])
                writer.writeheader()
    
    def get_all(self):
        expenses = []
        with open (self.file_path,mode="r",newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense.from_dict(row)
                expenses.append(expense)

        return expenses
    
    def save_all(self,expenses:list[Expense]):
        with open(self.file_path,mode="w",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["id","date","category","amount","note"])
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())


        
    