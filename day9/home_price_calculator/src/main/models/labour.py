from day9.home_price_calculator.src.main.models.person import Person 






class Labour(Person):
    def __init__(self,first_name,last_name,wage,role,crud):
        super().__init__(first_name,last_name)
        self.wage = wage
        self.role = role
        self.crud = crud
        self.id = self.__save_to_database(self.crud)