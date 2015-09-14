# what-to-watch
This is a python program designed to work through data obtained from MovieLens and sort
it by popularity and then make recommendations to users based on their data.

##To Run:

To run the program you will need Python 3. The data is referred to as "ml-100k/u.item" and "ml-100k/u.data" in the program's internals. This is what it is pulling the data from. Add the ml-100k directory to the root of this directory.

Then simply run the file what_to_watch.py in your terminal. Ex. python what_to_watch.py.

##How it works

The program works by collecting quite a bit of movie review data (over 100k reviews!) from MovieLens and putting into dictionary data structures in Python. The user is then able to see a general top 50 highest rated movies, or look by individual user (aka pretend to be one of the 943 people who submitted reviews).

If operating as a particular user there is an option to see the top 50 highest rated movies that the user hasn't reviewed, so is presumed to have not seen. The final option is to suggest a list of movies based on preferences from similar users. By finding the Euclidian distance between the chosen user and the rest of the dataset, we are able to find similar users (throwing out users who have only seen 1 or 2 of the same movies) then recommend a list of these similar users 5 starred ratings. We then removed all the movies that the user has already seen to provide a recommendation list based on similar user's favorites.
