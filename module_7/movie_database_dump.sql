BEGIN TRANSACTION;
CREATE TABLE genres (
    name TEXT PRIMARY KEY
);
INSERT INTO genres VALUES('Action');
INSERT INTO genres VALUES('Action/Comedy');
INSERT INTO genres VALUES('Comedy');
INSERT INTO genres VALUES('Comedy/Horror');
INSERT INTO genres VALUES('Comedy/Mockumentary');
INSERT INTO genres VALUES('Comedy/Sci-Fi');
INSERT INTO genres VALUES('Drama');
INSERT INTO genres VALUES('Fantasy/Adventure');
INSERT INTO genres VALUES('Horror');
INSERT INTO genres VALUES('Romance');
INSERT INTO genres VALUES('Sci-Fi');
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    release_year INTEGER,
    rating INTEGER,
    genre TEXT
);
INSERT INTO movies VALUES(1,'Shaun of the Dead',2004,6,'Comedy/Horror');
INSERT INTO movies VALUES(2,'Hot Fuzz',2007,6,'Action/Comedy');
INSERT INTO movies VALUES(3,'The World''s End',2013,5,'Comedy/Sci-Fi');
INSERT INTO movies VALUES(4,'Blade Runner',1982,6,'Sci-Fi');
INSERT INTO movies VALUES(5,'Blade Runner 2049',2017,6,'Sci-Fi');
INSERT INTO movies VALUES(6,'The Princess Bride',1987,6,'Fantasy/Adventure');
INSERT INTO movies VALUES(7,'This Is Spinal Tap',1984,5,'Comedy/Mockumentary');
INSERT INTO movies VALUES(8, 'Monty Python and the Holy Grail',1975,6,'Comedy');
INSERT INTO movies VALUES(9, 'Monty Python''s Life of Brian',1979,6,'Comedy');
CREATE TABLE credits (
    movie_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    PRIMARY KEY(movie_id, name, role)
);
INSERT INTO credits VALUES(1,'Simon Pegg','Actor');
INSERT INTO credits VALUES(1,'Nick Frost','Actor');
INSERT INTO credits VALUES(1,'Kate Ashfield','Actor');
INSERT INTO credits VALUES(1,'Edgar Wright','Director');
INSERT INTO credits VALUES(1,'Nira Park','Producer');
INSERT INTO credits VALUES(2,'Simon Pegg','Actor');
INSERT INTO credits VALUES(2,'Nick Frost','Actor');
INSERT INTO credits VALUES(2,'Timothy Dalton','Actor');
INSERT INTO credits VALUES(2,'Edgar Wright','Director');
INSERT INTO credits VALUES(2,'Nira Park','Producer');
INSERT INTO credits VALUES(3,'Simon Pegg','Actor');
INSERT INTO credits VALUES(3,'Nick Frost','Actor');
INSERT INTO credits VALUES(3,'Martin Freeman','Actor');
INSERT INTO credits VALUES(3,'Edgar Wright','Director');
INSERT INTO credits VALUES(3,'Nira Park','Producer');
INSERT INTO credits VALUES(4,'Harrison Ford','Actor');
INSERT INTO credits VALUES(4,'Rutger Hauer','Actor');
INSERT INTO credits VALUES(4,'Sean Young','Actor');
INSERT INTO credits VALUES(4,'Ridley Scott','Director');
INSERT INTO credits VALUES(4,'Michael Deeley','Producer');
INSERT INTO credits VALUES(5,'Ryan Gosling','Actor');
INSERT INTO credits VALUES(5,'Harrison Ford','Actor');
INSERT INTO credits VALUES(5,'Ana de Armas','Actor');
INSERT INTO credits VALUES(5,'Denis Villeneuve','Director');
INSERT INTO credits VALUES(5,'Andrew Kosove','Producer');
INSERT INTO credits VALUES(6,'Cary Elwes','Actor');
INSERT INTO credits VALUES(6,'Robin Wright','Actor');
INSERT INTO credits VALUES(6,'Mandy Patinkin','Actor');
INSERT INTO credits VALUES(6,'Rob Reiner','Director');
INSERT INTO credits VALUES(6,'Andrew Scheinman','Producer');
INSERT INTO credits VALUES(7,'Christopher Guest','Actor');
INSERT INTO credits VALUES(7,'Michael McKean','Actor');
INSERT INTO credits VALUES(7,'Harry Shearer','Actor');
INSERT INTO credits VALUES(7,'Rob Reiner','Director');
INSERT INTO credits VALUES(7,'Karen Murphy','Producer');
INSERT INTO credits VALUES(8, 'Graham Chapman', 'Actor');
INSERT INTO credits VALUES(8, 'John Cleese', 'Actor');
INSERT INTO credits VALUES(8, 'Eric Idle', 'Actor');
INSERT INTO credits VALUES(8, 'Terry Gilliam', 'Actor');
INSERT INTO credits VALUES(8, 'Terry Jones', 'Actor');
INSERT INTO credits VALUES(8, 'Michael Palin', 'Actor');
INSERT INTO credits VALUES(8, 'Terry Gilliam', 'Director');
INSERT INTO credits VALUES(8, 'Terry Jones', 'Director');
INSERT INTO credits VALUES(8, 'Mark Forstater', 'Producer');
INSERT INTO credits VALUES(9, 'Graham Chapman', 'Actor');
INSERT INTO credits VALUES(9, 'John Cleese', 'Actor');
INSERT INTO credits VALUES(9, 'Eric Idle', 'Actor');
INSERT INTO credits VALUES(9, 'Terry Gilliam', 'Actor');
INSERT INTO credits VALUES(9, 'Terry Jones', 'Actor');
INSERT INTO credits VALUES(9, 'Michael Palin', 'Actor');
INSERT INTO credits VALUES(9, 'Terry Jones', 'Director');
INSERT INTO credits VALUES(9, 'John Goldstone', 'Producer');
COMMIT;
