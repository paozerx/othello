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
        self.colorturn = "white"
        self.check_coin_write = 2
        self.check_coin_black = 2
        self.check_marker = 0
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
        self.turnswap = tk.Label(self.area_buttom, text=f"Turn : Player {self.colorturn}",font=('courier',19,'bold'),bg='#212121', fg='#f2f2f2')
        self.turnswap.place(x = 60,y = 4)
        self.turnpic = tk.Label(self.area_buttom, image=self.current,bg='#212121')
        self.turnpic.place(x = 360,y = -4)
        self.button_new = tk.Button(self.area_buttom, bg = '#FFD700', text='New Game',font=('courier',24,'bold'))
        self.button_new.grid(row=1,column=1,pady=70)
        self.button_re = tk.Button(self.area_buttom, bg = '#ff3030', text='Reset Game',font=('courier',24,'bold'))
        self.button_re.grid(row=1,column=2,pady=70,padx=30)

        self.area_infomation = self.area_infomation = tk.Frame(self.window_game)
        self.area_infomation.grid(row=2,column=0,sticky=W+E+S+N)
        self.area_infomation.configure(bg='#212121')

        self.area_history = tk.Frame(self.window_game)
        self.area_history.grid(row=2, column=3, sticky=W + E + S + N)
        self.area_history.configure(bg='#212121')
        self.move_history_text = tk.Text(self.area_history, height=10, width=30, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(self.area_history, command=self.move_history_text.yview)
        self.move_history_text.config(yscrollcommand=scrollbar.set)
        self.move_history_text.grid(row=0, column=3, pady=100, padx=30)
        self.move_history_text.configure(bg='#FF8C00', fg='#000000', font=('courier', 20, 'bold'))
        scrollbar.grid(row=0, column=4, sticky='ns')
        
        self.area_num = tk.Frame(self.window_game)
        self.area_num.grid(row=3 ,column=3, sticky=N+W+S+E)
        self.area_num.configure(bg='#212121')
        self.num_write = tk.Label(self.area_num, text=f'white : {self.check_coin_write}',font=('courier',19,'bold'),bg='#212121', fg='#f2f2f2')
        self.num_write.place(x = 270, y = 10)
        self.num_black = tk.Label(self.area_num, text=f'black : {self.check_coin_black}',font=('courier',19,'bold'),bg='#212121', fg='#f2f2f2')
        self.num_black.place(x = 270, y = 92)
        self.picnum_white = tk.Label(self.area_num, image="pyimage1",bg='#212121')
        self.picnum_white.place(x = 200,y = 0)
        self.picnum_black = tk.Label(self.area_num, image="pyimage2",bg='#212121')
        self.picnum_black.place(x = 200,y = 80)

        
        

    
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
        
        move = f"Player {self.colorturn}: row {k+1}, colunm {self.dichar[o+1]}"
        self.move_history.append(move)
        self.move_history_text.delete("1.0", tk.END)
        for move in self.move_history:
            self.move_history_text.insert(tk.END, move + '\n')
        self.move_history_text.see("end")
        
        self.check_coin_write = 0
        self.check_coin_black = 0
        self.check_coin()
        self.current= "pyimage2" if self.current == "pyimage1" else "pyimage1"
        self.another= "pyimage1" if self.another == "pyimage2" else "pyimage2"
        self.colorturn = "black" if self.colorturn == "white" else "white"
        self.turnswap.configure(text=f"Turn : Player {self.colorturn}")
        self.turnpic.configure(image=self.current)
        self.num_write.configure(text=f"white : {self.check_coin_write}")
        self.num_black.configure(text=f"black : {self.check_coin_black}")
        self.marker()
        
    
    def check_coin(self):
        for i in range (8):
            for j in range(8):
                if self.listboard[i][j]["image"] == "pyimage1":
                    self.check_coin_write += 1 
                elif self.listboard[i][j]["image"] == "pyimage2":
                    self.check_coin_black += 1
                # elif self.listboard[i][j]["image"] == "pyimage4":
                #     self.check_marker += 1
    
    # def check_winlose(self):
    #     if self.check_marker == 0:
    #         if self.check_coin_write > self.check_coin_black:
    #             print("Player white winnnn")
    #         elif self.check_coin_write < self.check_coin_black:
    #             print("Player black winnn")
    #         elif self.check_coin_write == self.check_coin_black:
    #             print("draw!")
    #     else:
    #         pass
    
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


