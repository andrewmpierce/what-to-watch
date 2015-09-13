from movie_lib import *
import math


#Your program is probably not working because the dictionary is being recycled
# every time it runs. I think if you break it up into smaller helper methods,
#You should be okay. the euclidian distance should take the two lists of equal
#length


def euclidian_distance(user1_id, user2_id):
    user1 = User(user1_id)
    user2 = User(user2_id)
    dict1 = user1.movies
    dict2 = user2.movies
    safe_dict1 = dict1.copy()
    safe_dict2 = dict2.copy()
    for k,v in dict1.items():
        if k not in dict2.keys():
            del safe_dict1[k]
    for k,v in dict2.items():
        if k not in dict1.keys():
            del safe_dict2[k]
    safe_dict1 = {int(k):int(v) for k,v in safe_dict1.items()}
    safe_dict2 = {int(k):int(v) for k,v in safe_dict2.items()}
    user1_sorted = sorted(safe_dict1.items(), key = lambda c: c[0], reverse = False)
    user2_sorted = sorted(safe_dict2.items(), key = lambda c: c[0], reverse = False)
    user1_ratings = [y for x,y in user1_sorted]
    user2_ratings = [y for x,y in user2_sorted]
    differences = [user1_ratings[idx] - user2_ratings[idx] for idx in range(len(user1_ratings))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)
    return 1 / (1 + math.sqrt(sum_of_squares))



def find_sim_users():
    similar_users = []
    counter = 1
    counter1 = 100
    for x in range(900):
        #if x != user_id:
        print(counter)
        print(counter1)
        sim = euclidian_distance(counter1, counter)
        similar_users.append(sim)
        print(sim)
        counter += 1
        counter1 += 1
    return similar_users

print(find_sim_users())
