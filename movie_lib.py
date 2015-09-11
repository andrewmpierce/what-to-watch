import csv


with open("ml-100k 2/u.item", encoding = 'latin_1') as f:
    all_movies = {}
    reader1 = csv.reader(f, delimiter='|')
    for row in reader1:
        key = int(row[0])
        all_movies[key] = row[1]
    print(all_movies)



all_users = {}


class User:
    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self

class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user = user_id
        self.movie = movie_id
        self.stars = stars
        all_movies[self.movie].add_rating(self)

    def __str__(self):
        return 'Rating(user_id {}), movie_id {}, stars {}'.format(self.user, self.movie, self.stars)

    def __repr__(self):
        return self.__str__()


class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
        all_movies[self.id] = self
        self.ratings = {}

    def __str__(self):
        return 'Movie: movie_id = {}, title = {}'.format(self.movie_id, repr(self.title))

    def __repr__(self):
        return self.__str__()

    def get_ratings(self):
        return self.ratings.values()

    def add_rating(self, rating):
        self.ratings[rating.user] = rating
