-- SQL code for the Authors and Books tables

BEGIN TRANSACTION;
DROP TABLE IF EXISTS Authors;
CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name TEXT);
INSERT INTO Authors VALUES(1, 'Jane Austen');
INSERT INTO Authors VALUES(2, 'Leo Tolstoy');
INSERT INTO Authors VALUES(3, 'Joseph Heller');
INSERT INTO Authors VALUES(4, 'Charles Dickens');
COMMIT;


BEGIN TRANSACTION;
DROP TABLE IF EXISTS Books;
CREATE TABLE Books(BookId INTEGER PRIMARY KEY, Title TEXT, 
    AuthorId INTEGER, FOREIGN KEY(AuthorId) 
    REFERENCES Authors(AuthorId));
    --REFERENCES Authors(AuthorId) ON DELETE SET NULL);
INSERT INTO Books VALUES(1, 'Emma', 1);
INSERT INTO Books VALUES(2, 'War and Peace', 2);
INSERT INTO Books VALUES(3, 'Catch XXII', 3);
INSERT INTO Books VALUES(4, 'David Copperfield', 4);
INSERT INTO Books VALUES(5, 'Good as Gold', 3);
INSERT INTO Books VALUES(6, 'Anna Karenina', 2);
INSERT INTO Books VALUES(7, 'Pride and Prejudice', 1);
INSERT INTO Books VALUES(8, 'Sense and Sensibility', 1);
COMMIT;
