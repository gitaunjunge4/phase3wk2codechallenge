from restaurant import Restaurant
from customer import Customer

class Review(Restaurant, Customer):
    def __init__(self, rating):
        if isinstance(rating, int):
            self.rating = rating
        

rev1= Review("halal",3)