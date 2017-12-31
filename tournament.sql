-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE Players (ID SERIAL,
                      Name VARCHAR(255) NOT NULL,
                      Wins INTEGER DEFAULT 0,
                      Matches INTEGER DEFAULT 0,
                      PRIMARY KEY (ID)
                      );

CREATE TABLE Matches (ID SERIAL,
                      Winner_id INTEGER,
                      Loser_id INTEGER,
                      Winner_name VARCHAR(255),
                      Loser_name VARCHAR(255),
                      PRIMARY KEY (ID),
                      FOREIGN KEY (Winner_id) REFERENCES Players(ID),
                      FOREIGN KEY (Loser_id) REFERENCES Players(ID)
                      );
