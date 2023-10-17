import tkinter as tk

class Othello:
    def __init__(self):
        self.window_game = tk.Tk()
        self.window_game.geometry("900x600+400+200")
        self.black = tk.PhotoImage(file='1.png')
        self.white = tk.PhotoImage(file='2.png')
        self.pre = tk.PhotoImage(file='3.png')
        self.board = tk.PhotoImage(file='4.png')
        self.listboard = []

        for x in range(8):
            self.listboard.append([])
            for y in range(8):
                self.listboard[x].append(None)

        self.create_widgets()

    def create_widgets(self):
        self.area_board = tk.Frame(self.window_game)
        for x in range(8):
            for y in range(8):
                self.listboard[x][y] = tk.Button(self.area_board, bg='green')
                self.listboard[x][y].grid(row=x, column=y)

    def game_start(self):
        self.window_game.mainloop()


