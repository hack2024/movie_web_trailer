"""
This is the main module, the entry point. 
This module gets all the information about the movies and then passes them in
an array of movie instances to the controller module of the application.
"""

from app_model import Movie
import app_controller
import app_json_movies_data

try:
    # Gets movie data from API
    movies_data = app_json_movies_data.get_movies_data()

    # Create all the favourite movie instances
    movies = []
    for movie in movies_data:
        movie_instance = Movie(movie)
        movies.append(movie_instance)

    # Call the open_movies_page that render the page whit all the movies
    app_controller.open_movies_page(movies)
except IOError:
    # If the connection whit the API throws an Exception
    # show an error page
    app_controller.open_error_page()
