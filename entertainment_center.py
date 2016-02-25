import fresh_tomatoes
import media


# Instances of class Movie:

friday = media.Movie("Friday", "16 hours in the lives of two" 
	" unemployed homies in the hood.", 
	"https://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg", 
	"https://www.youtube.com/watch?v=nH1Ulp4PBtA", "77%",
	"Ice Cube | Chris Tucker")

the_dark_knight = media.Movie("The Dark Knight", "Batman goes up" 
	" against the Joker to save Gotham", 
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", 
	"https://www.youtube.com/watch?v=EXeTwQWrcwY", "94%", 
	"Christian Bale | Heath Ledger")

gladiator = media.Movie("Gladiator", "The general who became a slave," 
	" the slave who became a gladiator", 
	"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg", 
	"https://www.youtube.com/watch?v=0BLZbrLogTo", "76%",
	"Russell Crowe | Joaquin Phoenix")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris.", 
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", 
	"https://www.youtube.com/watch?v=c3sBBRxDAqk", "96%",
	"Patton Oswalt | Brad Garrett")

malcolm_x = media.Movie("Malcolm X", "Biopic of civil rights leader, Malcolm X", 
	"https://upload.wikimedia.org/wikipedia/en/4/49/Malcolmxdvdset.jpg", 
	"https://www.youtube.com/watch?v=sx4sEvhYeVE", "91%",
	"Denzel Washington | Angela Bassett")

shawshank_redemption = media.Movie("The Shawshank Redemption", 
	"A story of friendship between 2 convicts in ugly prison life, who bond through hope" , 
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", 
	"https://www.youtube.com/watch?v=6hB3S9bIaco", "91%",
	"Tim Robbins | Morgan Freeman")

# movies in list format
movies = [friday, the_dark_knight, gladiator, ratatouille, malcolm_x, shawshank_redemption]

# Call to execute opening of movie trailer website
fresh_tomatoes.open_movies_page(movies)

