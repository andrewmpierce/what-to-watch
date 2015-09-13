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
        key = int(row[1])
        if key not in all_ratings:
            all_ratings[key] = list(row[2])
        else:
            all_ratings[key].append(row[2])
    all_ratings = {k:[int(x) for x in values] for k,values in all_ratings.items()}


with open("ml-100k 2/u.data", encoding = 'latin_1') as f:
    all_users = {}
    reader1 = csv.reader(f, delimiter='\t')
    for row in reader1:
        key = int(row[0])
        if key not in all_users:
            all_users[key] = {int(row[1]): int(row[2])}
        else:
            all_users[key].update({int(row[1]): int(row[2])})


class User:
    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self

    def all_ratings(self):
        return all_users[self.id]


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user = user_id
        self.movie = movie_id
        self.stars = stars


    def __str__(self):
        return 'Rating(user_id {}), movie_id {}, stars {}'.format(self.user, self.movie, self.stars)


    def __repr__(self):
        return self.__str__()


class Movie:
    def __init__(self, movie_id, title = None, ratings = None):
        self.id = movie_id
        self.title = all_movies[self.id]
        self.ratings = all_ratings[self.id]
        all_movies[self.id] = self
        all_ratings[self.id] = self


    def __str__(self):
        return 'Movie: movie_id = {}, title = {}, ratings = {}'.format(self.id, repr(self.title), repr(self.ratings))


    def __repr__(self):
        return self.__str__()


    def avg_rating(self):
        avg = round(sum(self.ratings)/len(self.ratings), 2)
        return avg
