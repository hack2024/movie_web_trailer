import urllib, json

omdb_api_url = "http://www.omdbapi.com/?apikey=cfb8e64a&i="

#get alien movie data
response = urllib.urlopen(omdb_api_url + "tt2316204")
json_alien = json.loads(response.read())
json_alien["posterImage"] = "view/imgs/alien_2.jpg"
json_alien["movieTrailer"] = "https://www.youtube.com/watch?v=svnAD0TApb8"

#get predator movie data
response = urllib.urlopen(omdb_api_url + "tt0093773")
json_predator = json.loads(response.read())
json_predator["posterImage"] = "view/imgs/predator_2.jpg"
json_predator["movieTrailer"] = "https://www.youtube.com/watch?v=Y1txEAywdiw"

#get terminator movie data
response = urllib.urlopen(omdb_api_url + "tt0088247")
json_terminator = json.loads(response.read())
json_terminator["posterImage"] = "view/imgs/terminator.jpg"
json_terminator["movieTrailer"] = "https://www.youtube.com/watch?v=k64P4l2Wmeg"

#get star wars movie data
response = urllib.urlopen(omdb_api_url + "tt2527336")
json_star_wars = json.loads(response.read())
json_star_wars["posterImage"] = "view/imgs/starwars_2.jpg"
json_star_wars["movieTrailer"] = "https://www.youtube.com/watch?v=Q0CbN8sfihY"

#get back to future movie data
response = urllib.urlopen(omdb_api_url + "tt0088763")
json_back_to_the_future = json.loads(response.read())
json_back_to_the_future["posterImage"] = "view/imgs/backtofuture.jpg"
json_back_to_the_future["movieTrailer"] = "https://www.youtube.com/watch?v=jEnERs6GvDc"

#get transformers movie data
response = urllib.urlopen(omdb_api_url + "tt3371366")
json_transformers = json.loads(response.read())
json_transformers["posterImage"] = "view/imgs/transformers_3.jpg"
json_transformers["movieTrailer"] = "https://www.youtube.com/watch?v=6Vtf0MszgP8"