from restaurant import Restaurant
from customer import Customer

class Review(Restaurant, Customer):
    def __init__(self, rating):
        super().__init__(self.res_name)
        super().__init__(self.full_name)
        self.rating = rating
        

rev1= Review("halal",3)