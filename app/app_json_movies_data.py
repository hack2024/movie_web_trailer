"""
This module connects to a REST API to obtain information about favorite movies
and stores them in the corresponding variable.
Only the posterImage and the movieTrailer are filled in this module.
"""

import urllib
import json

omdb_api_url = "http://www.omdbapi.com/?apikey=cfb8e64a&i="


def get_movies_data():
    """Get movies data from API

    Fetch the movie data, and return an array to the controller

    Return:
        json_movies_response: an array of movies fetched from the API

    """

    # get alien movie data
    response = urllib.urlopen(omdb_api_url + "tt2316204")
    json_alien = json.loads(response.read())
    json_alien["posterImage"] = "./imgs/alien_2.jpg"
    json_alien["movieTrailer"] = "https://www.youtube.com/watch?v=svnAD0TApb8"

    # get predator movie data
    response = urllib.urlopen(omdb_api_url + "tt0093773")
    json_predator = json.loads(response.read())
    json_predator["posterImage"] = "./imgs/predator_2.jpg"
    json_predator["movieTrailer"] = "https://www.youtube.com/watch?v=Y1txEAywdiw"

    # get terminator movie data
    response = urllib.urlopen(omdb_api_url + "tt0088247")
    json_terminator = json.loads(response.read())
    json_terminator["posterImage"] = "./imgs/terminator.jpg"
    json_terminator["movieTrailer"] = "https://www.youtube.com/watch?v=k64P4l2Wmeg"

    # get star wars movie data
    response = urllib.urlopen(omdb_api_url + "tt2527336")
    json_star_wars = json.loads(response.read())
    json_star_wars["posterImage"] = "./imgs/starwars_2.jpg"
    json_star_wars["movieTrailer"] = "https://www.youtube.com/watch?v=Q0CbN8sfihY"

    # get back to future movie data
    response = urllib.urlopen(omdb_api_url + "tt0088763")
    json_back_to_the_future = json.loads(response.read())
    json_back_to_the_future["posterImage"] = "./imgs/backtofuture.jpg"
    json_back_to_the_future["movieTrailer"] = "https://www.youtube.com/watch?v=jEnERs6GvDc"

    # get transformers movie data
    response = urllib.urlopen(omdb_api_url + "tt3371366")
    json_transformers = json.loads(response.read())
    json_transformers["posterImage"] = "./imgs/transformers_3.jpg"
    json_transformers["movieTrailer"] = "https://www.youtube.com/watch?v=6Vtf0MszgP8"

    json_movies_response = [json_alien, json_predator, json_terminator,
                            json_star_wars, json_back_to_the_future, json_transformers]

    return json_movies_response
