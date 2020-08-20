"""
Elo Rating Package v0.1.0
Created by Edward Ho on 3 March 2020

For detailed description of Elo Rating, please refer to
Wikipedia: https://en.wikipedia.org/wiki/Elo_rating_system

Elo Rating System is a method to calculate the relative
skills level of players.

The calculation is simply illustrated as below.

P_A(Win) = 1 / 1 + 10^((R_B - R_A) / 400))

Update formula

New rating = rating + 32 (Score - Expected Score)

Default Performance Rating Score: 400
"""

DEFAULT_PERFORMANCE_SCORE = 400
DEFAULT_BASE_NUMBER = 1000
DEFAULT_CUSTOM_FIXTURE = 0

class ELO():
    """Elo Rating System is a method to calculate the relative
skills level of players.
    """
    def __init__(
            self, fixture_ls, performance_score=DEFAULT_PERFORMANCE_SCORE,
            base_number=DEFAULT_BASE_NUMBER, custom_fixture=DEFAULT_CUSTOM_FIXTURE
    ):
        """
        Initialize the rating game, it accepts 3 parameters:

         - base_number :: input_type: int, list
        """
        self.players = {}
        self.performance_score = performance_score
        self.base_number = base_number
        self.custom_fixture = custom_fixture
        self.fixture_ls = fixture_ls

    def add_player(self, name, rating=None):
        """
        Add player into a dictionary
        """
        rating = rating or self.base_number
        self.players[name] = Player(name, rating)

    def get_players_ls(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.players

    def game(self, home, away, outcome, setting=None):
        """[summary]

        Args:
            home ([type]): [description]
            away ([type]): [description]
            outcome ([type]): [description]
            setting ([type], optional): [description]. Defaults to self.custom_fixture.

        Returns:
            [type]: [description]
        """
        setting = setting or self.custom_fixture
        if setting: # tournament
            results = self.fixture(self.fixture_ls)
        else: # single game
            results = self.result(home, away, outcome)

        return results

    def get_player(self, player_name):
        """[summary]

        Args:
            player_name ([type]): [description]

        Returns:
            [type]: [description]
        """
        player_1 = self.custom_fixture[player_name]
        return player_1

    def expected_score(self, home_rating, away_rating):
        """[summary]

        Args:
            home_rating ([type]): [description]
            away_rating ([type]): [description]

        Returns:
            [type]: [description]
        """
        score = 1 / (1 + 10 ** ((away_rating - home_rating) / self.performance_score))
        return score

    def result(self, home, away, outcome):
        """the forumla
           home and away are Player Object

        Args:
            home ([type]): [description]
            away ([type]): [description]
            outcome ([type]): [description]

        Returns:
            [type]: [description]
        """
        results = []
        ratings = {}

        player_1 = self.get_player(home)
        player_2 = self.get_player(away)
        home_score = self.expected_score(player_1.rating, player_2.rating)
        away_score = self.expected_score(player_2.rating, player_1.rating)

        #update score
        ratings[player_1.name] = home_score
        ratings[player_2.name] = away_score
        results.append([ratings, outcome])

        return results

    def fixture(self, fixture_ls):
        """Get Fixture

        Args:
            fixture_ls (list(str)): [description]

        Returns:
            [type]: [description]
        """

        for row in fixture_ls:
            home, away, outcome = row[0], row[1], row[2]
            results = self.result(home, away, outcome)

        return results

    def update_player(self, name, outcome):
        """[summary]

        Args:
            name ([type]): [description]
            outcome ([type]): [description]
        """
        player = self.get_player(name)
        outcome_ls = {'win' : 1, 'lose' : 0, 'draw' : 0.5}
        player.rating = player.rating + 32 * (outcome_ls[outcome] - 1)


class Player():
    """[summary]
    """
    def __init__(self, name, rating):
        self._name = name
        self._rating = rating

    @property
    def name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def rating(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        self._rating = new_rating
