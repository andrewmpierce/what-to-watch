import csv


with open("ml-100k 2/u.item", encoding = 'latin_1') as f:
    all_movies = {}
    reader1 = csv.reader(f, delimiter='|')
    for row in reader1:
        key = int(row[0])
        all_movies[key] = row[1]

with open("ml-100k 2/u.data", encoding = 'latin_1') as f:
    all_ratings = {}
    reader1 = csv.reader(f, delimiter='\t')
    for row in reader1:
        key = row[1]
        if key not in all_ratings:
            all_ratings[key] = list(row[2])
        else:
            all_ratings[key].append(row[2])



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
    def __init__(self, movie_id, title = None, ratings = None):
        self.id = movie_id
        self.title = all_movies[self.id]
        # self.ratings = all_ratings[self.id]
        all_movies[self.id] = self
        all_ratings[self.id] = self

    def __str__(self):
        return 'Movie: movie_id = {}, title = {}'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()

    def title(self):
        """This method will find a movie title from a dictionary of
        movie id's and titles"""
        return all_movies[self.id]

    def ratings(self):
        return all_ratings[self.id]

    def add_rating(self, rating):
        self.ratings[rating.user] = rating

movie1 = Movie(1)
print(movie1.title)
