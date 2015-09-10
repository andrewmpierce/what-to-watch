import unittest
from movie-lens import *

movie_ids = {1: "This is a movie 1" 2:"This is a movie 2"}



class TestMovieLens(unittest.TestCase):

    def test_get_title(self):
        self.assertEqual(get_title(1, movie_ids)"This is a movie 1")








if __name__ == '__main__':
    unittest.main()
