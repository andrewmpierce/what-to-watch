from movie_lib import *
from user_relations import *
from what_to_watch import *



siskel = User(5)
ebert = User(12)
movie1 = Movie(1, "Toy Story")
movie2 = Movie(9, "Pretty Woman")



def test_user_creation():
    assert siskel.id == 5
    assert ebert.id == 12

def test_movie_creation():
    assert movie1.id == 1
    assert movie1.title == "Toy Story (1995)"

def test_movie_avg_rating():
    assert movie1.avg_rating() == 3.88

def test_all_reviewed():
    assert all_reviewed(888) == [69, 100, 111, 137, 153, 180, 191, 202, 237, 269, 274, 280, 286, 514, 535, 631, 644, 762, 792, 869]
    assert all_reviewed(777) == [1, 9, 15, 42, 56, 100, 117, 127, 135, 153, 157, 168, 180, 196, 202, 204, 205, 212, 216, 223, 238, 245, 273, 286, 288, 357, 509, 521, 522, 523, 527, 652, 690, 692, 818, 1079]

def test_compare_users():
    assert compare_users(777, 888) == [100, 153, 180, 202, 286]

def test_euclidian_distance():
    assert euclidian_distance(777, 888) == 0.17253779651421453
    assert euclidian_distance(666, 777) == 0.11881849050177154

def test_find_sim_users():
    assert find_sim_users(777) == []
    assert find_sim_users(888) == [2]
