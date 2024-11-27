create table if not exists users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE if not exists movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    release_date DATE
);

create table if not exists user_watch_movie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    is_watched tinyint default 0,
    foreign key (user_id) references users(id),
    foreign key (movie_id) references movies(id)
);

INSERT INTO users (name) VALUES ('Alice');

INSERT INTO movies (name, release_date) VALUES
('The Shawshank Redemption', '1994-09-23'),
('The Godfather', '1972-03-15'),
('Pulp Fiction', '1994-10-07');

INSERT INTO user_watch_movie (user_id, movie_id, is_watched)
VALUES
(1, 1, TRUE),
(1, 2, FALSE),
(1, 3, TRUE);

select * from users;
select * from movies;
select * from user_watch_movie;