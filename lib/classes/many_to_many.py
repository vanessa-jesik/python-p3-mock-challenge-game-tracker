class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, "title"):
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(
            set([result.player for result in Result.all if result.game is self])
        )

    def average_score(self, player):
        return sum(
            [
                result.score
                for result in Result.all
                if result.player is player and result.game is self
            ]
        ) / len(
            [
                result.score
                for result in Result.all
                if result.player is player and result.game is self
            ]
        )


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and (2 <= len(username) <= 16):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(
            set([result.game for result in Result.all if result.player is self])
        )

    def played_game(self, game):
        if [
            result
            for result in Result.all
            if result.game is game and result.player is self
        ]:
            return True
        else:
            return False

    def num_times_played(self, game):
        if [
            result
            for result in Result.all
            if result.game is game and result.player is self
        ]:
            return len(
                [
                    result
                    for result in Result.all
                    if result.game is game and result.player is self
                ]
            )
        else:
            return 0


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if (
            isinstance(score, int)
            and (1 <= score <= 5000)
            and not hasattr(self, "score")
        ):
            self._score = score
