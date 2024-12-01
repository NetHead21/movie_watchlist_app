from collections import OrderedDict
from business_logic import (
    add_user_command,
    add_movie_command,
    add_user_movie_watch_command,
    list_movie_command,
    quit_command,
)
from persistence import MovieWatchlistDatabase
from presentation import Option, get_new_movie, get_new_user, get_user_movie_watchlist

movie_watchlist = MovieWatchlistDatabase()

options = OrderedDict(
    {
        "A": Option(
            "Add New Movie",
            add_movie_command.AddMovieCommand(),
            prep_call=get_new_movie,
            success_message="Movie added successfully.",
        ),
        "B": Option(
            "View Upcoming Movies",
            list_movie_command.ListMovieCommand(criteria={""}),
        ),
    }
)
