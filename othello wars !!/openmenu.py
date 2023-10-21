import tkinter as tk
import customtkinter
from othello import Othello



class Starts :
    def __init__(self):
        self.window0 = customtkinter.CTk()
        self.window0.title("Othello Wars")
        self.create_widgets()
    def playgame(self):
        self.window0.destroy()
        game = Othello()
        game.game_start()

    def create_widgets(self):
        self.window0.geometry("900x600+400+200")
        
        customtkinter. set_default_color_theme('green')
        topic = customtkinter.CTkLabel(self.window0,font=('courier',40,'bold'), text='Othello Wars').place(x=320, y=120)
        pvp = customtkinter.CTkButton(self.window0,font=('courier',24,'bold'), text='Player vs Player', command=self.playgame).place(x=150, y=250)
        pva1 = customtkinter.CTkButton(self.window0,font=('courier',24,'bold'), text='Player vs Mr.Jarvis').place(x=500, y=250)
        pva2 = customtkinter.CTkButton(self.window0,font=('courier',24,'bold'), text='Player vs Mr.Dose').place(x=150, y=390)
        ava = customtkinter.CTkButton(self.window0,font=('courier',24,'bold'), text='Mr.Jarvis vs Mr.Dose').place(x=500, y=390)

    def open(self):
        self.window0.mainloop()

    


        
        
        

