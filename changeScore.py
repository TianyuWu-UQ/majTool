from calculation import calculation
import tkinter as tk
class changeScore:
    def __init__(self,main,cal):
        self.main = main
        self.current_score = cal
        self.root = tk.Toplevel(self.main)
        self.button_ryuukyoku = tk.Button(self.root,text="流局")
        self.button_ron = tk.Button(self.root,text="荣和")
        self.button_zimo = tk.Button(self.root,text="自摸")

    def click_button_ryuukyoku(self):
        pass












    def excu_changeScore(self):
        self.root.title("changeScore")
        self.root.geometry("400x400")
        font = ("Helvetica", 20, "bold")

        self.button_ryuukyoku.config(font=font, width=4, height=2)
        self.button_ron.config(font=font,width=4,height=2)
        self.button_zimo.config(font=font,width=4,height=2)

        self.button_ryuukyoku.place(x=40,y=20)
        self.button_ron.place(x=170,y=20)
        self.button_zimo.place(x=300,y=20)

        self.root.mainloop()

