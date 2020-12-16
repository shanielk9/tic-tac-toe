class Game:
    def __init__(self, player_x, player_o):
        self.board = Board()
        self.players = [player_x, player_o]
        self.turn = False
        self.start_msg = '\n= = = = = = = = = = = = = = = = = = = = = = = =\n' \
                         '= = = = = = = = = = = = = = = = = = = = = = = =\n' \
                         '  _   _   _   _   _   _   _   _   _   _   _ \n ' \
                         '/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ \n' \
                         '( T | i | c | - | t | a | c | - | t | o | e )\n' \
                         ' \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \n'\
                         '= = = = = = = = = = = = = = = = = = = = = = = =\n' \
                         '= = = = = = = = = = = = = = = = = = = = = = = =\n' \

        self.start_info = f'Hey {self.players[0].name} and {self.players[1].name},\n' \
                          f'The first who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.\n' \
                          f'Let\'s start play!\n'\
                          f'\t\t\t\t=>There is a matrix on the right that illustrates the location of the indexes\n'


    def play(self):
        print(self.start_msg)
        print(self.start_info)

        while True:
            current_player = self.players[int(self.turn)]

            print(self.board.to_string())
            move = input(f'{current_player.name} ({current_player.sign}) make a move : select 0-8: ')

            while True:
                try:
                    move = int(move)
                    is_winner = self.board.make_move(current_player, move)
                    break
                except (ValueError, IndexError):
                    move = input(f'Illegal move, try again\n{current_player.name} make a move : select 0-8: ')

            if is_winner:
                print(self.board.to_string())
                print(f'Player {current_player.name} is the winner!\n')
                break

            if self.board.is_draw():
                print(self.board.to_string())
                print('It\'s a draw..!\n')
                break

            self.turn = not self.turn

        print('Do you want to start Again? Y - for yes\\else - for no:')
        answer = str(input())
        if answer.lower() == 'y':
            Game(Player('Shani', 'X'), Player('Asaf', 'O')).play()



class Board:
    def __init__(self):
        self.board = [' '] * 9

    def to_string(self):
        return '{}|{}|{}      0|1|2\n-----\n{}|{}|{}      3|4|5\n-----\n{}|{}|{}      6|7|8\n'.format(*self.board)

    def make_move(self, player, place):
        if self.board[place] != ' ':
            raise ValueError(f'place {place} is already taken.')
        self.board[place] = player.sign
        return self.is_winner(player.sign)

    def is_winner(self, sign):
        winning_position = [
             [0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]
        ]

        """
        all = if all 3 of indexes in pos are true
        any = if at least one of the values are true
        this returns if there a position in board that represent wining for player
        """

        return any(all([self.board[x] == sign for x in pos]) for pos in winning_position)

    def is_draw(self):
        return ' ' not in self.board


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


Game(Player('Shani', 'X'), Player('Asaf', 'O')).play()