import tkinter as tk
from tkinter import *
from botMrjarvis import jarvis
from botMsolivia import Bot_MsOlivia
import os,sys,time



class Othello_game:
    def __init__(self,botvs):
        # ตัวแปรที่ใช้ข้ามฟังก์ชัน
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
        self.check_coin_white = 2
        self.check_coin_black = 2
        self.check_marker = 0
        self.dichar = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
        self.start_time = None  
        self.game_over = False
        self.start_time = time.time()
        self.listboard = []
        self.move_history = []
        self.jarvis = jarvis()
        self.olivia = Bot_MsOlivia()
        self.botvs = botvs
        
        # สร้าง list None
        for x in range(8):
            self.listboard.append([])
            for y in range(8):
                self.listboard[x].append(None)

        # เรียกใช้ฟังก์ชันที่ต้องแสดงผลเมื่อเปิดโปรแกรม
        self.create_widgets()
        self.marker()
        self.start_timer()
        
       

    def create_widgets(self):
        # สร้าง Frame ของบอร์ด othello
        if self.botvs == "pvp":
            self.colorturn = "Player white"
        if self.botvs == "jarvis":
            self.colorturn = "Player"
        if self.botvs == "olivia":
            self.colorturn = "Player"
        if self.botvs == "bot":
            self.colorturn = "Mr.Jarvis"

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

        # Frame ของ ปุ่ม newgame resetgame และ เทิร์นของผู้เล่นปัจจุบัน
        self.area_buttom = tk.Frame(self.window_game)
        self.area_buttom.grid(row=3,column=2,sticky=W+E+S+N)
        self.area_buttom.configure(bg='#212121')
        self.turnswap = tk.Label(self.area_buttom, text=f"Turn : {self.colorturn}",font=('courier',19,'bold'),bg='#212121', fg='#f2f2f2')
        if self.botvs == "jarvis" or self.botvs == "olivia":
            self.turnswap.configure(text=f"Turn :    {self.colorturn}")
        if self.botvs == "bot":
            self.turnswap.configure(text=f"Turn :  {self.colorturn}")
        self.turnswap.place(x = 60,y = 4)
        self.turnpic = tk.Label(self.area_buttom, image=self.current,bg='#212121')
        self.turnpic.place(x = 360,y = -4)
        self.button_new = tk.Button(self.area_buttom, bg = '#FFD700', text='New Game',font=('courier',24,'bold'), command=self.back_to_menu)
        self.button_new.grid(row=1,column=1,pady=70)
        self.button_re = tk.Button(self.area_buttom, bg = '#ff3030', text='Reset Game',font=('courier',24,'bold'), command=self.reset_game)
        self.button_re.grid(row=1,column=2,pady=70,padx=80)

        # Frame ของเวลา
        self.area_infomation = self.area_infomation = tk.Frame(self.window_game)
        self.area_infomation.grid(row=1,column=1,sticky=W+E+S+N)
        self.area_infomation.configure(bg='#212121')
        self.timer_label = tk.Label(self.area_infomation, text="Time: 00:00", font=('courier', 19, 'bold'), bg='#CD5C5C', fg='#f2f2f2')
        self.timer_label.pack()

        # Frame ของประวัติการเล่น
        self.area_history = tk.Frame(self.window_game)
        self.area_history.grid(row=2, column=3, sticky=W + E + S + N)
        self.area_history.configure(bg='#212121')
        self.move_history_text = tk.Text(self.area_history, height=10, width=30, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(self.area_history, command=self.move_history_text.yview)
        self.move_history_text.config(yscrollcommand=scrollbar.set)
        self.move_history_text.grid(row=0, column=3, pady=100, padx=30)
        self.move_history_text.configure(bg='#FF8C00', fg='#000000', font=('courier', 20, 'bold'))
        scrollbar.grid(row=0, column=4, sticky='ns')
        
        # Frame ของสกอร์การเล่น
        self.area_num = tk.Frame(self.window_game)
        self.area_num.grid(row=3 ,column=3, sticky=N+W+S+E)
        self.area_num.configure(bg='#212121')
        self.num_write = tk.Label(self.area_num, text=f'white : {self.check_coin_white}',font=('courier',19,'bold'),bg='#212121', fg='#f2f2f2')
        self.num_write.place(x = 270, y = 10)
        self.num_black = tk.Label(self.area_num, text=f'black : {self.check_coin_black}',font=('courier',19,'bold'),bg='#212121', fg='#f2f2f2')
        self.num_black.place(x = 270, y = 92)
        self.picnum_white = tk.Label(self.area_num, image="pyimage1",bg='#212121')
        self.picnum_white.place(x = 200,y = 0)
        self.picnum_black = tk.Label(self.area_num, image="pyimage2",bg='#212121')
        self.picnum_black.place(x = 200,y = 80)

        
        
    def start_timer(self): # ฟังก์ชันของตัวจับเวลา ref: ChatGPT
        if not self.game_over:
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.time_str = f"Time: {minutes:02d}:{seconds:02d}"
            self.timer_label.configure(text=self.time_str)
            self.window_game.after(1000, self.start_timer)
            

    def marker(self): # ฟังก์ชันเช็คว่าสามารถวางจุดไหนได้บ้างแล้ว mark มัน
        for i in range(8):
            for j in range(8):
                if self.listboard[i][j]["image"] == self.another:
                    self.c_maker_top(i, j)
                    self.c_maker_bottom(i, j)
                    self.c_maker_left(i, j)
                    self.c_maker_right(i, j)
                    self.c_maker_top_left(i, j)
                    self.c_maker_top_right(i, j)
                    self.c_maker_bottom_left(i, j)
                    self.c_maker_bottom_right(i, j)

        # เช็คว่ามี mark อยู่ไหม ถ้าไม่มีให้เช็คแพ้ชนะ      
        checkingwin = False
        for k in range(8):
            for o in range(8):
                if self.listboard[k][o]["image"] == self.mark0:
                    checkingwin = True

        if not(checkingwin): 
            self.wincheck()

        if self.current == "pyimage2" and self.botvs == "jarvis":
            self.botjarvis()

        if self.current == "pyimage2" and self.botvs == "olivia":
            self.botolivia()

        if self.current == "pyimage1" and self.botvs == "bot":
            self.botjarvis()

        if self.current == "pyimage2" and self.botvs == "bot":
            self.botolivia()
            
    
    def play_thegame(self, event): # ฟังก์ชันการเล่นเกม ได้แก่ การกิน การเดิน การสลับสี ส่งค่าการนับสกอร์ ส่งค่าประวัติการเล่น
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
        
        move = f"{self.colorturn}: row {k+1}, column {self.dichar[o+1]}"
        self.move_history.append(move)
        self.move_history_text.delete("1.0", tk.END)
        for move in self.move_history:
            self.move_history_text.insert(tk.END, move + '\n')
        self.move_history_text.see("end")
        
        self.check_coin_white = 0
        self.check_coin_black = 0
        self.check_coin()
        self.current= "pyimage2" if self.current == "pyimage1" else "pyimage1"
        self.another= "pyimage1" if self.another == "pyimage2" else "pyimage2"
        if self.botvs == "pvp":
            self.colorturn = "Player black" if self.colorturn == "Player white" else "Player white"
            self.turnswap.configure(text=f"Turn : {self.colorturn}")
        if self.botvs == "jarvis":
            self.colorturn = "Mr.Jarvis" if self.colorturn == "Player" else "Player"
            if self.colorturn == "Player":
                self.turnswap.configure(text=f"Turn :    {self.colorturn}")
            elif self.colorturn == "Mr.Jarvis":
                self.turnswap.configure(text=f"Turn :  {self.colorturn}")

        if self.botvs == "olivia":
            self.colorturn = "Ms.Olivia" if self.colorturn == "Player" else "Player"
            if self.colorturn == "Player":
                self.turnswap.configure(text=f"Turn :    {self.colorturn}")
            elif self.colorturn == "Ms.Olivia":
                self.turnswap.configure(text=f"Turn :  {self.colorturn}")
        if self.botvs == "bot":
            self.colorturn = "Ms.Olivia" if self.colorturn == "Mr.Jarvis" else "Mr.Jarvis"
            if self.colorturn == "Mr.Jarvis":
                self.turnswap.configure(text=f"Turn :  {self.colorturn}")
            elif self.colorturn == "Ms.Olivia":
                self.turnswap.configure(text=f"Turn :  {self.colorturn}")
        
        self.turnpic.configure(image=self.current)
        self.num_write.configure(text=f"white : {self.check_coin_white}")
        self.num_black.configure(text=f"black : {self.check_coin_black}")
        self.marker()
        
    
    def check_coin(self): # นับตัวหมาก
        for i in range (8):
            for j in range(8):
                if self.listboard[i][j]["image"] == "pyimage1":
                    self.check_coin_white += 1 
                elif self.listboard[i][j]["image"] == "pyimage2":
                    self.check_coin_black += 1

    def wincheck(self): # ฟังก์ชันเช็คแพ้ชนะและแสดงผล
        wincon = ""
        t = ""
        if self.check_coin_white > self.check_coin_black:
            t = "winnnnn!!"
            if self.botvs == "pvp":
                wincon = "Player white"
            if self.botvs == "jarvis" or self.botvs == "olivia":
                wincon = "Player"
            if self.botvs == "bot":
               wincon = "Mr.Jarvis"
        elif self.check_coin_black > self.check_coin_white:
            t = "winnnnn!!"
            if self.botvs == "pvp":
                wincon = "Player black"
            if self.botvs == "jarvis":
                wincon = "Mr.Jarvis"
            if self.botvs == "olivia":
                wincon = "Ms.Olivia"
            if self.botvs == "bot":
               wincon = "Ms.Olivia"
        elif self.check_coin_white == self.check_coin_black:
            t = "drawwww!!!"
            wincon = "Two player"
        self.game_over = True
        display = tk.Tk()
        display.title("Othello")
        display.geometry("700x500+450+400")
        display.configure(bg='#212121')
        l1 = tk.Label(display,text=f" {wincon} {t}",font=('courier', 27, 'bold'),bg ='#212121',fg ='#f2f2f2')
        l1.place(x = 135,y = 50)
        timel = tk.Label(display,text=f"{self.time_str}",font=('courier', 19, 'bold'),bg ='#212121',fg ='#f2f2f2')
        timel.place(x = 255,y = 130)
        picl1 = tk.Label(display,text=f"White {self.check_coin_white} : {self.check_coin_black} Black",font=('courier', 19, 'bold'),bg ='#212121',fg ='#f2f2f2')
        picl1.place(x = 205,y = 210)
        butl1 = tk.Button(display, bg = '#FFD700', text='New Game',font=('courier',24,'bold'), command=self.back_to_menu)
        butl1.place(x = 120, y=320)
        butl2 = tk.Button(display, bg = '#ff3030', text='Reset Game',font=('courier',24,'bold'), command=self.reset_game)
        butl2.place(x = 400, y=320)

        def on_button_release(event):
            self.reset_game()
            display.destroy()

        butl2.bind("<ButtonRelease-1>",on_button_release)
            
        

    def reset_game(self): # ฟังก์ชันปรับทุกอย่างในเกมให้เป็นค่าเริ่มต้น
        self.move_history = []
        for x in range(8):
            for y in range(8):
                self.listboard[x][y]["image"] = self.background
                self.listboard[x][y].unbind("<Button-1>")
        self.listboard[3][3].configure(image=self.white)
        self.listboard[3][4].configure(image=self.black)
        self.listboard[4][3].configure(image=self.black)
        self.listboard[4][4].configure(image=self.white)
        if self.botvs == "pvp":
            self.colorturn = "Player white"
            self.turnswap.configure(text=f"Turn : {self.colorturn}")
        if self.botvs == "jarvis":
            self.colorturn = "Player"
            self.turnswap.configure(text=f"Turn :    {self.colorturn}")
        if self.botvs == "olivia":
            self.colorturn = "Player"
            self.turnswap.configure(text=f"Turn :    {self.colorturn}")
        if self.botvs == "bot":
            self.colorturn = "Mr.Jarvis"
            self.turnswap.configure(text=f"Turn :  {self.colorturn}")
        self.current = "pyimage1"
        self.another = "pyimage2"
        self.check_coin_white = 2
        self.check_coin_black = 2
        self.turnpic.configure(image=self.current)
        self.num_write.configure(text=f"white : {self.check_coin_white}")
        self.num_black.configure(text=f"black : {self.check_coin_black}")
        self.move_history_text.delete("1.0", tk.END)
        for move in self.move_history:
            self.move_history_text.insert(tk.END, move + '\n')
        self.move_history_text.see("end")
        self.game_over = False
        self.start_time = time.time()
        self.elapsed_time = 0
        self.start_timer()
        self.marker()

    def back_to_menu(self): # ฟังก์ชัน restart โปรแกรม ref: https://bobbyhadz.com/blog/how-to-restart-python-script-from-within-itself
        os.execv(sys.executable, ['python'] + sys.argv)

    def botjarvis(self):
        x = self.jarvis.control_area(self.mark0,self.listboard)
        self.window_game.after(1500, lambda: self.listboard[x[0]][x[1]].event_generate("<Button-1>"))
        self.window_game.after(1500, lambda: self.listboard[x[0]][x[1]].event_generate("<ButtonRelease-1>"))
       
    def botolivia(self):
        get = self.olivia.check_position_can_move(self.mark0,self.listboard,self.another,self.empty,self.current)
        self.window_game.after(1500, lambda: self.listboard[get[0]][get[1]].event_generate("<Button-1>"))
        self.window_game.after(1500, lambda: self.listboard[get[0]][get[1]].event_generate("<ButtonRelease-1>"))
        
        
        
        
        
        

    # ตั้งแต่จุดนี้จะเป็นฟังก์ชันการเช็คหมากทั้งหมด ref: กานต์ สุขสมกิจ
    
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
                    elif self.listboard[irow][c]["image"] == self.current or self.listboard[irow][c]["image"] == self.mark0:
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
                    elif self.listboard[irow][c]["image"] == self.current or self.listboard[irow][c]["image"] == self.mark0:
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
                    elif self.listboard[r][icolumn]["image"] == self.current or self.listboard[r][icolumn]["image"] == self.mark0:
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
                    elif self.listboard[r][icolumn]["image"] == self.current or self.listboard[r][icolumn]["image"] == self.mark0:
                        break
                    elif self.listboard[r][icolumn]["image"] == self.another:
                        continue

    def c_maker_top_left(self, r, c):
        for n in range(1, min(r, c)):
            if self.listboard[r - n][c - n]["image"] == self.empty or self.listboard[r - n][c - n]["image"] == self.mark0:
                break
            elif self.listboard[r - n][c - n]["image"] == self.another:
                continue
            elif self.listboard[r - n][c - n]["image"] == self.current:
                for i in range(1, min(7 - r, 7 - c)+1):
                    if self.listboard[r + i][c + i]["image"] == self.empty:
                        self.listboard[r + i][c + i]["image"] = self.mark0
                        self.listboard[r + i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r + i][c + i]["image"] == self.mark0:
                        break
                    elif self.listboard[r + i][c + i]["image"] == self.current or self.listboard[r + i][c + i]["image"] == self.mark0:
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
                for i in range(1, min(7 - r, c )+1):
                    if self.listboard[r + i][c - i]["image"] == self.empty:
                        self.listboard[r + i][c - i]["image"] = self.mark0
                        self.listboard[r + i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r + i][c - i]["image"] == self.mark0:
                        break
                    elif self.listboard[r + i][c - i]["image"] == self.current or self.listboard[r + i][c - i]["image"] == self.mark0:
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
                for i in range(1, min(r , 7 - c)+1):
                    if self.listboard[r - i][c + i]["image"] == self.empty:
                        self.listboard[r - i][c + i]["image"] = self.mark0
                        self.listboard[r - i][c + i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r - i][c + i]["image"] == self.mark0:
                        break
                    elif self.listboard[r - i][c + i]["image"] == self.current or self.listboard[r - i][c + i]["image"] == self.mark0:
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
                for i in range(1, min(r , c )+1):
                    if self.listboard[r - i][c - i]["image"] == self.empty:
                        self.listboard[r - i][c - i]["image"] = self.mark0
                        self.listboard[r - i][c - i].bind("<Button-1>", self.play_thegame)
                        break
                    elif self.listboard[r - i][c - i]["image"] == self.mark0:
                        break
                    elif self.listboard[r - i][c - i]["image"] == self.current or self.listboard[r - i][c - i]["image"] == self.mark0:
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


