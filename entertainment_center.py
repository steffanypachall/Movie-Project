import fresh_tomatoes
import movie

ip_man = movie.Movie("Ip Man",
                        "A movie based on the grandmaster Ip Man",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Ipmanposter02.jpg/220px-Ipmanposter02.jpg",
                        "https://www.youtube.com/watch?v=1AJxXQ7xojE")


avatar = movie.Movie("Avatar",
                     "A marine on an alien plantet",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


mulan = movie.Movie("Mulan",
                    "A girl who pretends to be a man to take her fathers place in war",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Movie_poster_mulan.JPG/220px-Movie_poster_mulan.JPG",
                    "http://www.youtube.com/watch?v=wAbGAkkOgcM")



hunger_games = movie.Movie("Hunger Games",
                           "A girl who has to survive a fight for the death",
                           "http://www.myhungergames.com/wp-content/uploads/2012/01/the-hunger-games-the-world-will-be-watching-katniss-everdeen-shot-arrow-poster.jpg",
                           "http://www.youtube.com/watch?v=SMGRhAEn6K0")

saving_private_ryan = movie.Movie("Saving Private Ryan",
                                   "A mission to save private Ryan in WWII",
                                   "http://upload.wikimedia.org/wikipedia/en/thumb/a/ac/Saving_Private_Ryan_poster.jpg/220px-Saving_Private_Ryan_poster.jpg",
                                   "http://www.youtube.com/watch?v=zwhP5b4tD6g")

kung_fu_hustle = movie.Movie("Kung Fu Hustle",
                             "A trouble maker who becomes a master in martial arts",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/0/00/KungFuHustleHKposter.jpg/220px-KungFuHustleHKposter.jpg",
                             "http://www.youtube.com/watch?v=-m3IB7N_PRk")

movie_list = [ip_man, avatar, mulan, hunger_games, saving_private_ryan, kung_fu_hustle]
fresh_tomatoes.open_movies_page(movie_list)
#print (movie.Movie.VALID_RATINGS)
#print (movie.Movie.__doc__)
