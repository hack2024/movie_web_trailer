class Movie():
    
    def __init__(self,json_movie_data):
        self.title = str(json_movie_data["Title"]).upper()
        self.short_description = json_movie_data["Plot"]
        self.poster_image_url = json_movie_data["posterImage"]
        self.trailer_youtube_url = json_movie_data["movieTrailer"]