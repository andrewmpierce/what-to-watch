from movie_lib import *

siskel = User(5)
ebert = User(12)
movie1 = Movie(3, "Toy Story")
movie2 = Movie(9, "Pretty Woman")
rating1 = Rating(5, 3, 5)
rating2 = Rating(12, 9, 5)
rating3 = Rating(5, 9, 3)



def test_user_creation():
    assert siskel.id == 5
    assert ebert.id == 12

def test_movie_creation():
    assert movie1.id == 3
    assert movie1.title == "Toy Story"
    assert movie2.id == 9
    assert movie2.title == "Pretty Woman"

def test_rating_creation():
    assert rating1.user == siskel.id
    assert rating2.user == ebert.id
    assert rating1.movie == movie1.id
    assert rating1.stars == 5

def test_find_ratings_for_movies():
    # toy_story_ratings = movie1.get_ratings_for_movie(movie1.id)
    toy_story_ratings = all_movies[movie1.id].get_ratings()
