import unittest
from movie import *
from rating import *
from user import *


movie_ids = {1: "This is a movie 1", 2:"This is a movie 2"}
movie_ratings = {1:[1, 2, 3], 2:[4, 5, 6]}
user_ratings = {1:{"Toy Story":2, "The Lion King":5}, 2:{"Toy Story":5, "The Lion King":3}}

movie = Movie(1)
rating = Rating(1,1)
user = User(1)

class TestMovieLens(unittest.TestCase):

    def test_get_title(self):
        self.assertEqual(movie.get_title(1, movie_ids), "This is a movie 1")

    def test_get_movie_ratings(self):
        self.assertEqual(rating.get_movie_ratings(1, movie_ratings), [1, 2, 3])

    def test_get_movie_avg(self):
        self.assertEqual(rating.get_movie_avg(1, movie_ratings), 2)

    def test_get_user_ratings(self):
        self.assertEqual(user.get_user_ratings(1, user_ratings), {'Toy Story':2, 'The Lion King':5})









if __name__ == '__main__':
    unittest.main()
