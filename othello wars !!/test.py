import tkinter as tk

class Othello:
    def __init__(self):
        self.window_game = tk.Tk()
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
        self.area_board = tk.Canvas(self.window_game, width=400, height=400)  # ระบุขนาด Canvas ที่คุณต้องการ
        self.area_board.pack()

        for x in range(8):
            for y in range(8):
                self.listboard[x][y] = self.area_board.create_rectangle(y * 50, x * 50, (y + 1) * 50, (x + 1) * 50, image =self.board)
                self.area_board.tag_bind(self.listboard[x][y], '<Button-1>', self.on_board_click)

    def on_board_click(self, event):
        item = self.area_board.find_withtag(tk.CURRENT)
        if item:
            self.area_board.itemconfig(item, fill='blue')  # ในตัวอย่างนี้เมื่อคลิก Canvas ปรับสีเป็นสีน้ำเงิน

    def game_start(self):
        self.window_game.mainloop()

if __name__ == '__main__':
    othello = Othello()
    othello.game_start()
