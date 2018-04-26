import webbrowser
import os
import re
import app_view


def create_movie_tiles_content(movies):
    """Create a movie tile

    Create the tiles to be added to the main html page later

    Args:
        movies: an array of movie instances

    """
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += app_view.movie_tile_content.format(
            movie_title=movie.title,
            movie_short_description=movie.short_description,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_url=movie.trailer_youtube_url
        )
    return content


def open_movies_page(movies):
    """Render the index.html

    Open a web browser and display the movies information in the movies array

    Args:
        movies: an array of movie instances

    """
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = app_view.main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(app_view.main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
