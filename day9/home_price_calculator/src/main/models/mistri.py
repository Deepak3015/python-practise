from day9.home_price_calculator.src.main.models.labour import Labour 


 


class Mistri(Labour):
    def__init__(self,fisrt_name,last_name,wage,role,skill.crud):
        super().init(first_name,last_name,wage,role,crud)
        self.wage = wage
        self.role = role
    def to_dict(self):
        data = super().to_dict()
        data.update({"wage":self.wage,"role":self.role})
        return data