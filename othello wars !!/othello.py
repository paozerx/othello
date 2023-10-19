import tkinter as tk
from tkinter import *



class Othello:
    def __init__(self):
        self.window_game = tk.Tk()
        self.window_game.title("Othello")
        self.window_game.configure(bg='#212121')
        self.white = tk.PhotoImage(file='white.png')
        self.black = tk.PhotoImage(file='black.png')
        self.background = tk.PhotoImage(file='background.png')
        self.mark = tk.PhotoImage(file='mark.png')
        self.current = "pyimage1"
        self.another = "pyimage2"
        self.empty = "pyimage3"
        self.mark0 = "pyimage4"
        self.dichar = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
        self.listboard = []
        self.move_history = []
        

        for x in range(8):
            self.listboard.append([])
            for y in range(8):
                self.listboard[x].append(None)

        self.create_widgets()
        self.marker()
       
        

    def create_widgets(self):
        self.area_board = tk.Frame(self.window_game)
        self.area_board.grid(row=2, column=2,sticky=W+E+S+N)
        self.area_board.configure(bg='#212121')
        for x in range(8):
            for y in range(8):
                self.listboard[x][y] = tk.Button(self.area_board, image=self.background)
                self.listboard[x][y].grid(row=x+1, column=y+1)
        self.listboard[3][3].configure(image=self.white)
        self.listboard[3][4].configure(image=self.black)
        self.listboard[4][3].configure(image=self.black)
        self.listboard[4][4].configure(image=self.white)
        for x in range(8):
            self.positionx = tk.Label(self.area_board, text='{}'.format(x+1),font=('courier',24,'bold'),bg ='#212121',fg ='#f2f2f2')
            self.positionx.grid(row=x+1,column=0)
        for x in range(8):
            self.positiony = tk.Label(self.area_board,text='{}'.format(self.dichar[x+1]),font=('courier',24,'bold'),bg ='#212121',fg ='#f2f2f2')
            self.positiony.grid(row=0,column=x+1)

        self.area_buttom = tk.Frame(self.window_game)
        self.area_buttom.grid(row=3,column=2,sticky=W+E+S+N)
        self.area_buttom.configure(bg='#212121')
        self.button_new = tk.Button(self.area_buttom, bg = '#f5f754', text='New Game',font=('courier',24,'bold'))
        self.button_new.grid(row=0,column=0,pady=100)
        self.button_re = tk.Button(self.area_buttom, bg = '#ff3030', text='Reset Game',font=('courier',24,'bold'))
        self.button_re.grid(row=0,column=3,pady=100,padx=30)

        self.area_infomation = self.area_infomation = tk.Frame(self.window_game)
        self.area_infomation.grid(row=0,column=0,sticky=W+E+S+N)
        self.area_infomation.configure(bg='#212121')

        self.area_history = self.area_history = tk.Frame(self.window_game)
        self.area_history.grid(row=2,column=3,sticky=W+E+S+N)
        self.area_history.configure(bg='#212121')
        self.move_history_text = tk.Text(self.area_history, height=10, width=30, wrap=tk.WORD)
        self.move_history_text.grid(row=0, column=3,pady=100,padx=30)
        self.move_history_text.configure(bg='#212121', fg='#f2f2f2', font=('courier', 24))

    
    def marker(self):
        for i in range(8):
            for j in range(8):
                if self.listboard[i][j]["image"] == self.another:
                    for k in range(8):
                        if self.listboard[i][j] in self.listboard[k]:
                            o = self.listboard[k].index(self.listboard[i][j])
                            break
                    self.c_maker_top(k,o)
                    self.c_maker_bottom(k,o)
                    self.c_maker_left(k,o)
                    self.c_maker_right(k,o)
                    self.c_maker_top_left(k, o)
                    self.c_maker_top_right(k, o)
                    self.c_maker_bottom_left(k, o)
                    self.c_maker_bottom_right(k, o)
    
    def play_thegame(self, event):
        clicker = event.widget
        clicker["image"] = self.current
        for k in range(8):
            if clicker in self.listboard[k]:
                o = self.listboard[k].index(clicker)
                break
        self.play_top(k,o)
        self.play_bottom(k,o)
        self.play_left(k,o)
        self.play_right(k,o)
        self.play_top_left(k,o)
        self.play_top_right(k,o)
        self.play_bottom_left(k,o)
        self.play_bottom_right(k,o)

        for i in range(8):
            for j in range(8):
                self.listboard[i][j].unbind("<Button-1>")
                if self.listboard[i][j]["image"] == self.mark0:
                    self.listboard[i][j]["image"] = self.empty
        
        move = f"Player {self.current[-1]}: row {k+1}, colunm {self.dichar[o+1]}"
        self.move_history.append(move)
        self.move_history_text.delete("1.0", tk.END)
        for move in self.move_history:
            self.move_history_text.insert(tk.END, move + '\n')

        
        self.current= "pyimage2" if self.current == "pyimage1" else "pyimage1"
        self.another= "pyimage1" if self.another == "pyimage2" else "pyimage2"
        self.marker()
   

        
    
    def c_maker_top(self,r,c):
        for nrow in range(r-1,-1,-1):
            if self.listboard[nrow][c]["image"] == self.empty or self.listboard[nrow][c]["image"] == self.mark0:
                break
            elif self.listboard[nrow][c]["image"] == self.another:
                continue
            elif self.listboard[nrow][c]["image"] == self.current:
                for irow in range(r+1,8):
                    if self.listboard[irow][c]["image"] == self.empty:
                        self.listboard[irow][c]["image"] = self.mark0
                        self.listboard[irow][c].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.listboard[irow][c]["image"] == self.mark0:
                        break
                    elif self.listboard[irow][c]["image"] == self.current or self.listboard[nrow][c]["image"] == self.mark0:
                        break
                    elif self.listboard[irow][c]["image"] == self.another:
                        continue
    
    def c_maker_bottom(self,r,c):
        for nrow in range(r+1,8):
            if self.listboard[nrow][c]["image"] == self.empty or self.listboard[nrow][c]["image"] == self.mark0:
                break
            elif self.listboard[nrow][c]["image"] == self.another:
                continue
            elif self.listboard[nrow][c]["image"] == self.current:
                for irow in range(r-1,-1,-1):
                    if self.listboard[irow][c]["image"] == self.empty:
                        self.listboard[irow][c]["image"] = self.mark0
                        self.listboard[irow][c].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.listboard[irow][c]["image"] == self.mark0:
                        break
                    elif self.listboard[irow][c]["image"] == self.current or self.listboard[nrow][c]["image"] == self.mark0:
                        break
                    elif self.listboard[irow][c]["image"] == self.another:
                        continue

    def c_maker_left(self,r,c):
        for ncolumn in range(c-1,-1,-1):
            if self.listboard[r][ncolumn]["image"] == self.empty or self.listboard[r][ncolumn]["image"] == self.mark0:
                break
            elif self.listboard[r][ncolumn]["image"] == self.another:
                continue
            elif self.listboard[r][ncolumn]["image"] == self.current:
                for icolumn in range(c+1,8):
                    if self.listboard[r][icolumn]["image"] == self.empty:
                        self.listboard[r][icolumn]["image"] = self.mark0
                        self.listboard[r][icolumn].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.listboard[r][icolumn]["image"] == self.mark0:
                        break
                    elif self.listboard[r][icolumn]["image"] == self.current or self.listboard[r][ncolumn]["image"] == self.mark0:
                        break
                    elif self.listboard[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_right(self,r,c):
        for ncolumn in range(c+1,8):
            if self.listboard[r][ncolumn]["image"] == self.empty or self.listboard[r][ncolumn]["image"] == self.mark0:
                break
            elif self.listboard[r][ncolumn]["image"] == self.another:
                continue
            elif self.listboard[r][ncolumn]["image"] == self.current:
                for icolumn in range(c-1,-1,-1):
                    if self.listboard[r][icolumn]["image"] == self.empty:
                        self.listboard[r][icolumn]["image"] = self.mark0
                        self.listboard[r][icolumn].bind("<Button-1>",self.play_thegame)
                        break
                    elif self.listboard[r][icolumn]["image"] == self.mark0:
                        break
                    elif self.listboard[r][icolumn]["image"] == self.current or self.listboard[r][ncolumn]["image"] == self.mark0:
                        break
                    elif self.listboard[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_top_left(self, r, c):
        for n in range(1, min(r, c) ):
            if self.listboard[r - n][c - n]["image"] == self.empty or self.listboard[r - n][c - n]["image"] == self.mark0:
                break
            elif self.listboard[r - n][c - n]["image"] == self.another:
                continue
            elif self.listboard[r - n][c - n]["image"] == self.current:
                for i in range(1, min(8 - r, 8 - c)):
                    if self.listboard[r + i][c + i]["image"] == self.empty:
                        self.listboard[r + i][c + i]["image"] = self.mark0
                        self.listboard[r + i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r + i][c + i]["image"] == self.mark0:
                        break
                    elif self.listboard[r + i][c + i]["image"] == self.current or self.listboard[r - n][c - n]["image"] == self.mark0:
                        break
                    elif self.listboard[r + i][c + i]["image"] == self.another:
                        continue

    def c_maker_top_right(self, r, c):
        for n in range(1, min(r, 7 - c) ):
            if self.listboard[r - n][c + n]["image"] == self.empty or self.listboard[r - n][c + n]["image"] == self.mark0:
                break
            elif self.listboard[r - n][c + n]["image"] == self.another:
                continue
            elif self.listboard[r - n][c + n]["image"] == self.current:
                for i in range(1, min(8 - r, c )):
                    if self.listboard[r + i][c - i]["image"] == self.empty:
                        self.listboard[r + i][c - i]["image"] = self.mark0
                        self.listboard[r + i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r + i][c - i]["image"] == self.mark0:
                        break
                    elif self.listboard[r + i][c - i]["image"] == self.current or self.listboard[r - n][c + n]["image"] == self.mark0:
                        break
                    elif self.listboard[r + i][c - i]["image"] == self.another:
                        continue

    def c_maker_bottom_left(self, r, c):
        for n in range(1, min(7 - r, c) ):
            if self.listboard[r + n][c - n]["image"] == self.empty or self.listboard[r + n][c - n]["image"] == self.mark0:
                break
            elif self.listboard[r + n][c - n]["image"] == self.another:
                continue
            elif self.listboard[r + n][c - n]["image"] == self.current:
                for i in range(1, min(r , 8 - c)):
                    if self.listboard[r - i][c + i]["image"] == self.empty:
                        self.listboard[r - i][c + i]["image"] = self.mark0
                        self.listboard[r - i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r - i][c + i]["image"] == self.mark0:
                        break
                    elif self.listboard[r - i][c + i]["image"] == self.current or self.listboard[r + n][c - n]["image"] == self.mark0:
                        break
                    elif self.listboard[r - i][c + i]["image"] == self.another:
                        continue

    def c_maker_bottom_right(self, r, c):
        for n in range(1, min(7 - r, 7 - c) ):
            if self.listboard[r + n][c + n]["image"] == self.empty or self.listboard[r + n][c + n]["image"] == self.mark0:
                break
            elif self.listboard[r + n][c + n]["image"] == self.another:
                continue
            elif self.listboard[r + n][c + n]["image"] == self.current:
                for i in range(1, min(r , c )):
                    if self.listboard[r - i][c - i]["image"] == self.empty:
                        self.listboard[r - i][c - i]["image"] = self.mark0
                        self.listboard[r - i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r - i][c - i]["image"] == self.mark0:
                        break
                    elif self.listboard[r - i][c - i]["image"] == self.current or self.listboard[r + n][c + n]["image"] == self.mark0:
                        break
                    elif self.listboard[r - i][c - i]["image"] == self.another:
                        continue

    
    def play_top(self,r,c):
        memory = []
        for nrow in range(r-1,-1,-1):
            if self.listboard[nrow][c]["image"] == self.empty or self.listboard[nrow][c]["image"] == self.mark0:
                break
            elif self.listboard[nrow][c]["image"] == self.another:
                memory.append([nrow,c])
                continue
            elif self.listboard[nrow][c]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break

    def play_bottom(self,r,c):
        memory = []
        for nrow in range(r+1,8):
            if self.listboard[nrow][c]["image"] == self.empty or self.listboard[nrow][c]["image"] == self.mark0:
                break
            elif self.listboard[nrow][c]["image"] == self.another:
                memory.append([nrow,c])
                continue
            elif self.listboard[nrow][c]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break

    def play_left(self,r,c):
        memory = []
        for ncolumn in range(c-1,-1,-1):
            if self.listboard[r][ncolumn]["image"] == self.empty or self.listboard[r][ncolumn]["image"] == self.mark0:
                break
            elif self.listboard[r][ncolumn]["image"] == self.another:
                memory.append([r,ncolumn])
                continue
            elif self.listboard[r][ncolumn]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break
    
    def play_right(self,r,c):
        memory = []
        for ncolumn in range(c+1,8):
            if self.listboard[r][ncolumn]["image"] == self.empty or self.listboard[r][ncolumn]["image"] == self.mark0:
                break
            elif self.listboard[r][ncolumn]["image"] == self.another:
                memory.append([r,ncolumn])
                continue
            elif self.listboard[r][ncolumn]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break
    
    def play_top_left(self, r, c):
        memory = []
        for n in range(1, min(r, c) ):
            if self.listboard[r - n][c - n]["image"] == self.empty or self.listboard[r - n][c - n]["image"] == self.mark0:
                break
            elif self.listboard[r - n][c - n]["image"] == self.another:
                memory.append([r - n,c - n])
                continue
            elif self.listboard[r - n][c - n]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break
    
    def play_top_right(self, r, c):
        memory = []
        for n in range(1, min(r, 7 - c) ):
            if self.listboard[r - n][c + n]["image"] == self.empty or self.listboard[r - n][c + n]["image"] == self.mark0:
                break
            elif self.listboard[r - n][c + n]["image"] == self.another:
                memory.append([r - n,c + n])
                continue
            elif self.listboard[r - n][c + n]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break
    
    def play_bottom_left(self, r, c):
        memory = []
        for n in range(1, min(7 - r, c) ):
            if self.listboard[r + n][c - n]["image"] == self.empty or self.listboard[r + n][c - n]["image"] == self.mark0:
                break
            elif self.listboard[r + n][c - n]["image"] == self.another:
                memory.append([r + n,c - n])
                continue
            elif self.listboard[r + n][c - n]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break
    
    def play_bottom_right(self, r, c):
        memory = []
        for n in range(1, min(7 - r, 7 - c) ):
            if self.listboard[r + n][c + n]["image"] == self.empty or self.listboard[r + n][c + n]["image"] == self.mark0:
                break
            elif self.listboard[r + n][c + n]["image"] == self.another:
                memory.append([r + n,c + n])
                continue
            elif self.listboard[r + n][c + n]["image"] == self.current:
                for i in memory:
                    self.listboard[i[0]][i[1]]["image"] = self.current
                break
                

    def game_start(self):
        self.window_game.mainloop()


