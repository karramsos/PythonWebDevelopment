-- SQL for the Friends table


BEGIN TRANSACTION;
CREATE TABLE Friends(Id INTEGER PRIMARY KEY, 
        Name TEXT);
INSERT INTO "Friends" VALUES(1,'Tom');
INSERT INTO "Friends" VALUES(2,'Rebecca');
INSERT INTO "Friends" VALUES(3,'Jim');
INSERT INTO "Friends" VALUES(4,'Robert');
COMMIT;
