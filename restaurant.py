from customer import Customer
from review import Review

class Restaurant:
    def __init__(self, res_name):
        if isinstance(res_name, str):
            self.res_name = res_name
        else:
            raise ValueError("Please put a valid restaurant name")

    def name(self):
        return self.res_name 
