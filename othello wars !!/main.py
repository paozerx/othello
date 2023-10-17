import tkinter as tk
import customtkinter
from othello import Othello

def main():
    program = Start()
    program.window.mainloop()


class Start :
    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.title("Othello Wars")
        self.create_widgets()
    def playgame(self):
        game = Othello()
        game.game_start()

    def create_widgets(self):
        self.window.geometry("900x600+400+200")
        
        customtkinter. set_default_color_theme('green')
        topic = customtkinter.CTkLabel(self.window,font=('courier',40,'bold'), text='Othello Wars').place(x=320, y=120)
        pvp = customtkinter.CTkButton(self.window,font=('courier',24,'bold'), text='Player vs Player', command=self.playgame).place(x=150, y=250)
        pva1 = customtkinter.CTkButton(self.window,font=('courier',24,'bold'), text='Player vs Mr.Jarvis').place(x=500, y=250)
        pva2 = customtkinter.CTkButton(self.window,font=('courier',24,'bold'), text='Player vs Mr.Dose').place(x=150, y=390)
        ava = customtkinter.CTkButton(self.window,font=('courier',24,'bold'), text='Mr.Jarvis vs Mr.Dose').place(x=500, y=390)
    


        
        
        

if __name__ == '__main__':
    main()