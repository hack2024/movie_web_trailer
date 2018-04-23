from app_model import Movie
import app_controller,app_json_movies_data


alien = Movie(app_json_movies_data.json_alien)
predator = Movie(app_json_movies_data.json_predator)
terminator = Movie(app_json_movies_data.json_terminator)
star_wars = Movie(app_json_movies_data.json_star_wars)
back_to_future = Movie(app_json_movies_data.json_back_to_the_future)
transformers = Movie(app_json_movies_data.json_transformers)

movies = [alien,predator,terminator,star_wars,back_to_future,transformers]

app_controller.open_movies_page(movies)