from random import randrange
class jarvis : #ref: https://codereview.stackexchange.com/questions/202618/oop-othello-in-python-with-tkinter-ui-and-basic-ai
    def control_area(self,mark,possibleplay):
        othello_weights = [
            [100, -20, 10, 5, 5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [10, -2, 1, 1, 1, 1, -2, 10],
            [5, -2, 1, 1, 1, 1, -2, 5],
            [5, -2, 1, 1, 1, 1, -2, 5],
            [10, -2, 1, 1, 1, 1, -2, 10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10, 5, 5, 10, -20, 100]
            ]
        score = -100
        play = []
        for i in range (8):
            for j in range(8):
                if possibleplay[i][j]["image"] == mark:
                    value = othello_weights[i][j]
                    if value == score:
                        play.append([i,j])
                        score = value
                    if value > score:
                        play = [[i,j]]
                        score = value
        return play[randrange(len(play))]
    


