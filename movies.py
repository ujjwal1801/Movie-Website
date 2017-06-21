import media
import fresh_tomatoes

the_prestige = media.Movie("The Prestige","Two friends and fellow magicians become bitter enemies after a sudden tragedy. As they devote themselves to this rivalry, they make sacrifices that bring them fame but with terrible consequences.","https://i.jeded.com/i/the-prestige.14577.jpg","https://www.youtube.com/watch?v=o4gHCmTQDVI")

interstellar = media.Movie("Interstellar","In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.","https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=0vxOhd4qlnA")

dark_knight = media.Movie("The Dark Knight","The Joker, a psychopath, terrorises Gotham so he can prove that even the most incorruptible people can become evil. However, Batman, Gordon and Dent stand against him.","https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=EXeTwQWrcwY")

twenty_one_jumpstreet = media.Movie("21 Jump Street","Schmidt and Jenko are high school friends who go onto become police officers. The two rookie cops go undercover as students in order to bust a drug ring and find the source of a synthetic drug.","https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3NzQ3OTg3NF5BMl5BanBnXkFtZTcwMjk5OTcxNw@@._V1_UY1200_CR85,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=ISJR4rVO0TQ")

begin_again = media.Movie("Begin Again","Gretta, a budding songwriter, finds herself alone after being ditched by her boyfriend. But things change when Dave, a record label executive, notices her talent.","https://images-na.ssl-images-amazon.com/images/M/MV5BNjAxMTI4MTgzMV5BMl5BanBnXkFtZTgwOTAwODEwMjE@._V1_UY1200_CR86,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=uTRCxOE7Xzc")

saving_private_ryan = media.Movie("Saving Private Ryan","During the Normandy invasion of World War II, Captain John Miller is assigned the task of searching for Private James Ryan, whose three brothers have already been killed in the war.","http://fontmeme.com/images/Saving-Private-Ryan-Poster.jpg","https://www.youtube.com/watch?v=h5p5j_K0CsY")

films = [the_prestige, interstellar, dark_knight, twenty_one_jumpstreet, begin_again, saving_private_ryan]

fresh_tomatoes.open_movies_page(films)





