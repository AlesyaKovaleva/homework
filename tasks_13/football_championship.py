import uuid


class Team:
    all_teams = []

    def __init__(self, name):
        self._uid = uuid.uuid4()
        self._name = name
        self._players = []
        Team.all_teams.append(self)

    def add_player(self, player):
        if player._team is None:
            self._players.append(player)
            player._team = self
        else:
            print(
                f'Невозможно добавить игрока в команду, '
                f'т.к. он игрок команды {player._team}'
            )

    def delete_player(self, player):
        if player in self._players:
            self._players.remove(player)
            player._team = None
        else:
            print(
                f'{player._name} не является игроком команды {self._name}'
            )

    @property
    def all_players(self):
        return self._players if self._players else 'В команде нет игроков.'

    def __repr__(self):
        return f'{self._name}'

    def __str__(self):
        return f'{self._name}'


class Player:
    all_players = []

    def __init__(self, name, team=None):
        self._uid = uuid.uuid4()
        self._name = name
        self._team = team
        Player.all_players.append(self)
        if self._team is not None:
            if self._team in team.all_teams:
                team._players.append(self)
            else:
                return 'Такой команды не существует!'

    def delete(self):
        if self._team is not None:
            self._team._players.remove(self)
            self._team = None
        self.all_players.remove(self)
        del self

    def set_team(self, team):
        if self._team is None:
            if team in team.all_teams:
                self._team = team
                team._players.append(self)
            else:
                print('Такой команды не существует.')
        else:
            print(
                f'Невозможно поменять команду, т.к. '
                f'игрок состоит в команде {self._team}'
            )

    @property
    def team(self):
        if self._team is None:
            return 'У этого игрока нет команды!'
        else:
            return f'{self._name} игрок команды {self._team}.'

    def __str__(self):
        return f'{self._name}'

    def __repr__(self):
        return f'{self._name}'


class Match:
    def __init__(self):
        self.uid = uuid.uuid4()

# id, date, location, result, team1, team2, players


first_team = Team('First')
second_team = Team('Second')
third_team = Team('Third')

player1 = Player('Papa Carlo', first_team)
player2 = Player('Mama Darlo', second_team)
player3 = Player('Bla Bla')
