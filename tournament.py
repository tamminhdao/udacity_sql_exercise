#!/usr/bin/env python3
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM Matches");
    c.execute("UPDATE Players SET Wins = 0")
    c.execute("UPDATE Players SET Matches = 0")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM Players");
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM Players")
    rows = c.fetchall()
    return rows[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO Players(Name) VALUES ('{}')".format(name))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM Players ORDER BY Wins DESC")
    players = c.fetchall()
    return players

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO Matches(winner_id, loser_id) VALUES ({winner}, {loser})".format(winner=winner, loser=loser))
    c.execute("UPDATE Players SET Matches = Matches + 1 WHERE ID = {}".format(winner))
    c.execute("UPDATE Players SET Wins = Wins + 1 WHERE ID = {}".format(winner))
    c.execute("UPDATE Players SET Matches = Matches + 1 WHERE ID = {}".format(loser))
    db.commit()
    db.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    players = playerStandings()
    all_pairs = []

    for i in range (0,len(players),2):
        player1 = (players[i][0], players[i][1])
        player2 = (players[i + 1][0], players[i + 1][1])
        pair = player1 + player2
        all_pairs.append(pair)

    print(all_pairs)
    return all_pairs
