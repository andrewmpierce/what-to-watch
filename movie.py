class Movie:
    def __init__(self, item_id):
        self.item_id = item_id


    def title(self, item_id, id_title_dict):
        """This method will find a movie title from a dictionary of
        movie id's and titles"""
        return id_title_dict[item_id]



# sample = {1:"This is a movie", 2: "This is a second movie"}
# movie = Movie(1)
# movie.get_title(1, sample)


# if __name__ == '__main__':
#     main()
