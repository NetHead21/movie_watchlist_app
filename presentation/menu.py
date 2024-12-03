from collections import OrderedDict
from business_logic import (
    add_user_command,
    add_movie_command,
    add_user_movie_watch_command,
    list_movie_command,
    quit_command,
    list_user_movie_watched_command,
)
from persistence import MovieWatchlistDatabase
from presentation import (
    Option,
    get_new_movie,
    get_new_user,
    get_user_movie_watchlist,
    get_user_id,
)

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
            list_movie_command.ListMovieCommand(criteria="release_date > current_date"),
        ),
        "C": Option(
            "View All Movies",
            list_movie_command.ListMovieCommand(),
        ),
        "D": Option(
            "Add Watched Movie",
            add_user_movie_watch_command.AddUserMovieWatch(),
            prep_call=get_user_movie_watchlist,
            success_message="Watched Movie added successfully.",
        ),
        "E": Option(
            "View Watched Movies",
            list_user_movie_watched_command.ListUserMovieWatchedCommand(),
            prep_call=get_user_id,
        ),
        "F": Option(
            "Add New User",
            add_user_command.AddUserCommand(),
            prep_call=get_new_user,
            success_message="User added successfully.",
        ),
        "G": Option("Quit", quit_command.QuitCommand()),
    }
)
