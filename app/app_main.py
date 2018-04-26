"""
This is the main module, the entry point. 
This module gets all the information about the movies and then passes them in
an array of movie instances to the controller module of the application.
"""

from app_model import Movie
import app_controller
import app_json_movies_data

# Create all the favourite movie instances
alien = Movie(app_json_movies_data.json_alien)
predator = Movie(app_json_movies_data.json_predator)
terminator = Movie(app_json_movies_data.json_terminator)
star_wars = Movie(app_json_movies_data.json_star_wars)
back_to_future = Movie(app_json_movies_data.json_back_to_the_future)
transformers = Movie(app_json_movies_data.json_transformers)

movies = [alien, predator, terminator, star_wars, back_to_future, transformers]

# Call the open_movies_page that render the page whit all the movies
app_controller.open_movies_page(movies)
