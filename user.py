class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_user_ratings(self, user_id, all_ratings):
        """This method will return a list of all the ratings from
        a user given their user_id"""
        value = all_ratings[user_id]
        return value

#
# user_ratings = {1:{"Toy Story":2, "The Lion King":5}, 2:{"Toy Story":5, "The Lion King":3}}
# user = User(1)
# user.get_user_ratings(1, user_ratings)

# if __name__ == '__main__':
#     main()
