class Rating:
    def __init__(self, user_id, item_id):
        self.user_id = user_id
        self.item_id = item_id

    def get_movie_ratings(self, item_id, all_movie_ratings_dict):
        """This method will return all the ratings associated with
        a movie id"""
        return all_movie_ratings_dict[item_id]


    def get_movie_avg(self, item_id, all_movie_ratings_dict):
        """This method will return the average of all the ratings
        associated with a movie id. It will probably call
        get_movie_ratings"""
        ratings = all_movie_ratings_dict[item_id]
        avg = sum(ratings)/len(ratings)
        return avg


# movie_ratings = {1:[1, 2, 3], 2:[4, 5, 6]}
# rating = Rating(1,1)
# rating.get_movie_ratings(1, movie_ratings)

# if __name__ == '__main__':
#     main()
