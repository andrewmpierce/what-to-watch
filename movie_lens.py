import csv

class Movie:

    def __init__(self, item_id):
        self.item_id = item_id
        self.row = self.find_row(item_id)

    def find_row(self, item_id):
        """This finds the correct row in csv or value in dictionary that
        corresponds to the item_id passed in"""
        movies = open("ml-100k 2/u.info", 'rb')
        for row in movies:
            if row[0] == item_id:
                return row


    def title(self):
        """This method will find a movie title from a dictionary of
        movie id's and titles"""
        print(self.row)
        return self.row[1]


    def average_rating(self):
        pass

    def ratings(self):
        pass

movie = Movie(1)
print(movie.title())
