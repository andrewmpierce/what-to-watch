class Movie:
    def __init__(self, item_id):
        self.item_id = item_id


    def title(self, all_movies):
        """This method will find a movie title from a dictionary of
        movie id's and titles"""
        return all_movies[item_id]



# sample = {1:"This is a movie", 2: "This is a second movie"}
# movie = Movie(1)
# movie.get_title(1, sample)


# if __name__ == '__main__':
#     main()
