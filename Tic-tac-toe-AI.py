import random


class TicTacToe:
    def __init__(self, m_1, m_2):
        self.lis = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
        self.user_lis = [(1, 3), (2, 3), (3, 3),
                         (1, 2), (2, 2), (3, 2),
                         (1, 1), (2, 1), (3, 1)]

        self.move_lis = [(0, 0), (0, 1), (0, 2),
                         (1, 0), (1, 1), (1, 2),
                         (2, 0), (2, 1), (2, 2)]
        self.mode_1 = m_1
        self.mode_2 = m_2
        self.mov_ctr = 0
        self.ai = 'X'
        self.human = 'O'
        self.scores = {'X': 10, 'O': -10, 'Draw': 0}

    def printing(self):
        print(" ---------")
        print(" | {} {} {} |".format(self.lis[0][0], self.lis[0][1], self.lis[0][2]))
        print(" | {} {} {} |".format(self.lis[1][0], self.lis[1][1], self.lis[1][2]))
        print(" | {} {} {} |".format(self.lis[2][0], self.lis[2][1], self.lis[2][2]))
        print(" ---------")

    def result(self):
        flag_x = 0
        flag_o = 0
        for i in range(3):
            ch = self.lis[i][0]
            if ch == ' ':
                continue
            row_ctr = 0
            for j in range(3):
                if self.lis[i][j] == ch:
                    row_ctr += 1
            if row_ctr == 3:
                if ch == 'X':
                    flag_x = 1
                elif ch == 'O':
                    flag_o = 1
                break
        if flag_o == 1:
            return 'O'
        elif flag_x == 1:
            return 'X'

        for i in range(3):
            ch = self.lis[0][i]
            if ch == ' ':
                continue
            col_ctr = 0
            for j in range(3):
                if self.lis[j][i] == ch:
                    col_ctr += 1
            if col_ctr == 3:
                if ch == 'X':
                    flag_x = 1
                elif ch == 'O':
                    flag_o = 1
                break

        if flag_o == 1:
            return 'O'
        elif flag_x == 1:
            return 'X'

        if self.lis[0][0] == self.lis[1][1] == self.lis[2][2] or self.lis[0][2] == self.lis[1][1] == self.lis[2][0]:
            if self.lis[1][1] == 'X':
                flag_x = 1
            elif self.lis[1][1] == 'O':
                flag_o = 1
        if flag_o == 1:
            return 'O'
        elif flag_x == 1:
            return 'X'

        for i in self.lis:
            if ' ' in i:
                return ''
        return 'Draw'

    def mini_max(self, depth, maximizing):
        check_res = self.result()
        if check_res != '':
            return self.scores[check_res]
        if maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.lis[i][j] == ' ':
                        self.lis[i][j] = self.ai
                        score = self.mini_max(depth + 1, False)
                        self.lis[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score

        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.lis[i][j] == ' ':
                        self.lis[i][j] = self.human
                        score = self.mini_max(depth + 1, True)
                        self.lis[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = float('-inf')
        move = 0, 0
        if self.ai == 'X':
            self.scores = {'X': 10, 'O': -10, 'Draw': 0}
        else:
            self.scores = {'O': 10, 'X': -10, 'Draw': 0}
        for i in range(3):
            for j in range(3):
                if self.lis[i][j] == ' ':
                    self.lis[i][j] = self.ai
                    score = self.mini_max(0, False)
                    self.lis[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)

        return move
    
    def make_move(self, mode):
        if mode == 'user':
            while True:
                a, b = input("Enter the coordinates: ").split()
                a = int(a)
                b = int(b)
                if (a, b) in self.user_lis:
                    break
            self.user_lis.remove((a, b))
            self.move_lis.remove((3 - b, a - 1))
            return 3 - b, a - 1

        elif mode == 'easy':
            print('Making move level "easy"')
            ab = random.choice(self.move_lis)
            a = ab[0]
            b = ab[1]
            self.move_lis.remove((a, b))
            self.user_lis.remove((b + 1, 3 - a))
            return a, b

        elif mode == 'medium':
            print('Making move level "medium"')
            ab = random.choice(self.move_lis)
            a = ab[0]
            b = ab[1]
            self.move_lis.remove((a, b))
            self.user_lis.remove((b + 1, 3 - a))
            return a, b

        elif mode == 'hard':
            ab = self.best_move()
            print('Making move level "hard"')
            a = ab[0]
            b = ab[1]
            self.move_lis.remove((a, b))
            self.user_lis.remove((b + 1, 3 - a))
            return a, b

    def playing(self):
        res = ''
        self.printing()
        while res == '':
            if self.mode_1 == 'hard':
                self.ai = 'X'
                self.human = 'O'

            xy = self.make_move(self.mode_1)
            x = int(xy[0])
            y = int(xy[1])
            self.lis[x][y] = 'X'
            self.printing()
            res = self.result()

            if res != '':
                break

            if self.mode_2 == 'hard':
                self.ai = 'O'
                self.human = 'X'
            xy = self.make_move(self.mode_2)
            x = int(xy[0])
            y = int(xy[1])
            self.lis[x][y] = 'O'
            self.printing()
            res = self.result()
            if res != '':
                break
        print('Draw' if res == 'Draw' else res + ' wins')


while True:
    cmd = input().split()
    if cmd[0] == 'exit':
        break
    modes = ['user', 'easy', 'medium', 'hard']
    if cmd[0] == 'start':
        if len(cmd) == 1 or len(cmd) == 2:
            print('Bad parameters')
            continue
        elif cmd[1] not in modes or cmd[2] not in modes:
            print('Bad parameters')
            continue
    if cmd[0] != 'start':
        print('Bad parameters')
        continue

    tic = TicTacToe(cmd[1], cmd[2])
    tic.playing()
