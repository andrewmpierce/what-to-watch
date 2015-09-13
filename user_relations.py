from movie_lib import *
import math

def euclidian_distance(user1_id, user2_id):
    user1 = User(user1_id)
    user2 = User(user2_id)
    dict1 = user1.movies
    dict2 = user2.movies
    keys_to_del = []
    for k in dict1.keys():
        if k not in dict2.keys():
            keys_to_del.append(k)
    for k in dict2.keys():
        if k not in dict1.keys():
            keys_to_del.append(k)
    for x in keys_to_del:
        if x in dict1.keys():
            del dict1[x]
    for x in keys_to_del:
        if x in dict2.keys():
            del dict2[x]
    dict1 = {int(k):int(v) for k,v in dict1.items()}
    dict2 = {int(k):int(v) for k,v in dict2.items()}
    user1_sorted = sorted(dict1.items(), key = lambda c: c[0], reverse = False)
    user2_sorted = sorted(dict2.items(), key = lambda c: c[0], reverse = False)
    user1_ratings = [y for x,y in user1_sorted]
    user2_ratings = [y for x,y in user2_sorted]
    differences = [user1_ratings[idx] - user2_ratings[idx] for idx in range(len(user1_ratings))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)
    return 1 / (1 + math.sqrt(sum_of_squares))



print(euclidian_distance(1, 6))
