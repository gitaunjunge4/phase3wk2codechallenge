class Customer:
    _all_customers = []

    def __init__(self, first_name, last_name):
        if isinstance(first_name and last_name, str):
            self.first_name = first_name
            self.last_name = last_name
            Customer.all(self)
        else:
            raise ValueError("Please put a valid name")

    def given_name(self):
        return self.first_name

    def family_name(self):
        return self.last_name

    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
    
    @classmethod
    def all(cls, self):
        Customer._all_customers.append(self)

cus_1 = Customer("Gitau", "Njung'e")
cus_2 = Customer("John", "Doe")
cus_3 = Customer("Kyle", "Jumper")

print(Customer._all_customers)

