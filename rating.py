class Rating:
    def __init__:(self, user_id, item_id)
    self.user_id = user_id
    self.item_id = item_id

    def get_movie_ratings(self, item_id, all_movie_ratings_dict):
        """This method will return all the ratings associated with
        a movie id"""
        movie_r = []
        for x in all_movie_ratings_dict:
            if x == item_id:
                movie_r.append(x)
        return movie_r


    def get_movie_avg(self, item_id):
        """This method will return the average of all the ratings
        associated with a movie id. It will probably call
        get_movie_ratings"""
        ratings = get_movie_ratings(item_id, all_movie_ratings_dict)
        avg = ratings/len(ratings)
        return avg



if __name__ == '__main__':
    main()
