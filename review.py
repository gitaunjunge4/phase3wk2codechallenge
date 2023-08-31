class Review:

    _all_reviews = []

    def __init__(self, customer, restaurant, res_rating):
        if isinstance(res_rating, int):
            self.customer = customer
            self.restaurant = restaurant
            self.res_rating = res_rating
            Review.all(self)

    def rating(self):
        return self.res_rating
    
    @classmethod
    def all(cls, review):
        return Review._all_reviews.append(review)
    
    def customeR(self):
        return self.customer
    
    def restauranT(self):
        return self.restaurant
     

rev_1= Review("halal", "jokke", 3)
rev_2= Review("dodo", "ginger", 4)
rev_3= Review("not", "hail", 9)

print(Review._all_reviews)
