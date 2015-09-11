class User:
    def__init__(self, user_id):
        self.id = user_id

class Rating:
    def__init__(self, user, movie, stars):
        self.user = user
        self.movie = movie
        self.stars = stars

class Movie:
    def__init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
