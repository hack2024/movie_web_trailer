# FullStack Nanodegree Program - Movie Trailer Website Project

This project aims to demonstrate the faculties acquired so far for the Nanodegree FullStack Web Developer program.

### Goal

The goal of this project is to run server-side code to store a list of favorite movies, including box art images and a movie preview URL. Next, it will serve this data as a web page that allows visitors to review their movies and see the progress.
The project can be cloned or downloaded from the following URL.
https://github.com/hack2024/movie_web_trailer.git

### Installation (Unix)

This project requires Pyton 2.7 to run.

Install the Python interpreter.

```sh
$ brew install python@2
```

Because python@2 is a “keg”, we need to update our PATH again, to point at our new installation:

```sh
$ export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"
```
Homebrew names the executable python2 so that you can still run the system Python via the executable python.

```sh
$ python -V   # Homebrew installed Python 3 interpreter (if installed)
$ python2 -V  # Homebrew installed Python 2 interpreter
$ python3 -V  # Homebrew installed Python 3 interpreter (if installed)
```
### Installation (Windows)
Download and install python from the next link.
https://www.python.org/ftp/python/2.7.15/python-2.7.15rc1.amd64.msi
### Running the project

Now we can execute the project.

Unix
```sh
$ cd to_the_project_folder
$ python movie_website_project/app/app_main.py
```
Windows 

On windows is the same thing, go to the project folder and execute the app_main.py python script from the console.

At this moment the application should raise a browser and show the website with the favorite movies so you can see the title, art image, a short description and a trailer of the movie.

### Author
**Fernando Balmaceda - phantom2024@gmail.com**
