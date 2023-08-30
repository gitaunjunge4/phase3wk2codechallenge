class Customer:
    all = []

    def __init__(self, first_name, last_name):
        if isinstance(first_name and last_name, str):
            self.first_name = first_name
            self.last_name = last_name
            Customer.all.append(self)
        else:
            raise ValueError("Please put a valid name")

    def given_name(self):
        return self.first_name

    def family_name(self):
        return self.last_name

    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

cus1 = Customer("Gitau", "Njung'e")
print(Customer.all)

