class Movie():

    """Class that represent the movie blueprint

    Attributes:
        title: the title of the movie
        short_description: short description of a movie
        poster_image_url: the poster image of the movie
        trailer_youtube_url: the movie trailer of the movie
    """

    def __init__(self, json_movie_data):
        """
        Initialize the Movie instance
        """

        self.title = str(json_movie_data["Title"]).upper()
        self.short_description = json_movie_data["Plot"]
        self.poster_image_url = json_movie_data["posterImage"]
        self.trailer_youtube_url = json_movie_data["movieTrailer"]
