class Person:
    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.email = first_name+"."+second_name+"@gmail.com"

    def print_details(self):
        return f"Your first name is set as{self.first_name} and last name set as{self.second_name}"
    
    def to_dict(self):
        return {
            "first_name":self.first_name,
            "second_name":self.second_name,
            "email":self.email 
        }