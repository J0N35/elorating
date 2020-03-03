"""
Elo Rating Package v0.1 
Created by Edward Ho on 3 March 2020

For detailed description of Elo Rating, please refer to
Wikipedia: https://en.wikipedia.org/wiki/Elo_rating_system

Elo Rating System is a method to calculate the relative 
skills level of players. 

The calculation is simply illustrated as below.

P_A(Win) = 1 / 1 + 10^((R_B - R_A) / 400))

Update formula

New rating = rating + 32 (Score - Expected Score)

Default Performate Rating Score: 400

"""

class elo():

    def __init__(performance_score = 400, base_number = 1000, custom_fixture = 0, self, fixture_ls):

        """
        Initialize the rating game, it accepts 3 parameters:
        
         - base_number :: input_type: int, list

        """
        self.players = {}
        self.performance_score = performance_score
        self.base_number = base_number
        self.custom_fixture = custom_fixture
        self.fixture_ls = fixture_ls

    def add_player(self, name, rating = self.base_number):
        """
        Add player into a dictionary
        """
        self.player[name] = Player(name, rating)

    def get_players_ls(self):
        for player in self.players



    def game(self, home, away, setting = self.custom_fixture, outcome):
        if setting: # tournament
            results = self.fixture(self.fixture_ls)

        else: # single game
            results = self.result(home, away, outcome)



        return results

    
    def get_player(self, player_name):
        player_1 = self.custom_fixture[player_name]
        return player
        

    def result(self, home, away, outcome):
        # the forumla 
        # home and away are Player Object
        
        results = []
        ratings = {}

        player_1 = self.get_player(away)
        player_2 = self.get_player(away)
        home_score = 1 / 1 + 10 ** ((player_2.rating - player_1.rating) / self.performance_score)
        away_score = (1 - home_win)
        #update score

        ratings[player_1.name] = home_rating
        ratings[player_2.name] = away_rating

        results.append([ratings, outcome])

        return results

    def fixture(self, fixture_ls):
        # Get Fixture
        # :input: list(str)

        for row in fixture_ls:
            home = row[0]
            away = row[1]
            outcome = row[2]
            results = self.result(home, away, outcome)

        return results
    
    def update_player(self, name, outcome):
        player = self.get_player(name)
        outcome_ls = {'win' : 1, 'lose' : 0, 'draw' : 0.5}
        player.rating = player.rating + 32(outcome_ls[outcome] - 1) 

        

class Player():
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating 
