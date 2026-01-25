from datetime import datetime


class Expense:

    def __init__(self,expense_id:int,date:str,category:str,amount:float,note: str = ""):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def _validate_date(self,date_str:str) -> str:
        try: 

            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD Format")
        
    def _validate_category(self,category_str:str) -> str:
        if not category_str or not category_str.strip():
            raise ValueError("Category can not be empty")
        return category_str.strip().lower()
    
    def _validate_amount(self,amount_int:float) -> float:
        if amount_int <= 0:
            raise ValueError("Amount must be Greator than zero")
        return round(float(amount_int),2)
    
    def to_dict(self) -> dict:

        return{
            "id":self.expense_id,
            "date" : self.date,
            "category":self.category,
            "amount":self.amount,
            "note":self.note}
    
    @classmethod
    def from_dict(cls,data:dict):

        return cls(
            expense_id = int(data["id"]),
            date = data["date"],
            category = data["category"],
            amount = data["amount"],
            note = data.get("note",""))
    
    def __repr__(self):
            return (
            f"Expense(id={self.expense_id}, "
            f"date='{self.date}', "
            f"category='{self.category}', "
            f"amount={self.amount}, "
            f"note='{self.note}')"
        )



