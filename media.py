import webbrowser

class Movie():
   

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, tomatometer, movie_cast):
    	self.title = movie_title
    	self.storyline = movie_storyline
    	self.poster_image_url = poster_image
    	self.trailer_youtube_url = trailer_youtube
    	self.movie_rating = tomatometer   # Added tomatometer attribute to reflect movie rating
    	self.actors = movie_cast          # Added attribute for main cast listing

    def show_trailer(self):
	    webbrowser.open(self.trailer_youtube_url)	