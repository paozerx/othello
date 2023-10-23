import customtkinter as cs #ref: https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22
from othellogame import Othello_game


def main():
    program = Start()
    program.window.mainloop()


class Start :
    def __init__(self):
        self.window = cs.CTk()
        self.window.title("Othello Wars")
        self.create_widgets()
    def playgame(self):
        self.window.destroy()
        game = Othello_game()
        game.game_start()

    def create_widgets(self):
        self.window.geometry("900x600+400+200")
        
        cs. set_default_color_theme('green')
        topic = cs.CTkLabel(self.window,font=('courier',40,'bold'), text='Othello Wars').place(x=320, y=120)
        pvp = cs.CTkButton(self.window,font=('courier',24,'bold'), text='Player vs Player', command=self.playgame).place(x=150, y=250)
        pva1 = cs.CTkButton(self.window,font=('courier',24,'bold'), text='Player vs Mr.Jarvis').place(x=500, y=250)
        pva2 = cs.CTkButton(self.window,font=('courier',24,'bold'), text='Player vs Mr.Dose').place(x=150, y=390)
        ava = cs.CTkButton(self.window,font=('courier',24,'bold'), text='Mr.Jarvis vs Mr.Dose').place(x=500, y=390)
    


        
        
        

if __name__ == '__main__':
    main()