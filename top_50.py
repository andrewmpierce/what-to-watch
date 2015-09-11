from movie_lib import *



def main():
    print("Okay let's see the top 50 movies! At least according to Movie Lens...")
    popularity = {}
    for key, value in all_ratings.items():
        if len(value) >= 20:
            popularity[key] = sum(value)/len(value)
    sorted_list = sorted(popularity.items(), key = lambda c: c[1], reverse = True)
    top_50 = sorted_list[:50]
    counter = 0
    for x in top_50:
        print(str(all_movies[top_50[counter][0]]) + ' ' + str(top_50[counter][1]))
        counter += 1
main()
