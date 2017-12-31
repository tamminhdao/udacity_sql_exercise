### Project Description: 
This is a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

### Project Requirement:
* Python 3
* Postgres
* psycopg2

### Create the database:
* `cd` to the project folder
* Open Postgres `psql postgres`
* `CREATE DATABASE Tournament`
* `\c tournament`
* `\i tournament.sql`

### Run the test:
`python3 tournament_test.py`
  
