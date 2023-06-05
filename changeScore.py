from calculation import calculation
import tkinter as tk
from tkinter import ttk


class changeScore:
    def __init__(self, main, cal):
        self.main = main
        self.current_score = cal
        self.root = tk.Toplevel(self.main)

        self.style_method = ttk.Style()
        self.style_method.configure('Method.TRadiobutton', font=("Helvetica", 20, "bold"))

        self.method_choose = tk.StringVar()
        self.method_ryuukyoku = ttk.Radiobutton(self.root, text="流局", variable=self.method_choose, value="ryuukyoku",
                                                command=self.click_button_ryuukyoku, style='Method.TRadiobutton')
        self.method_ron = ttk.Radiobutton(self.root, text="荣和", variable=self.method_choose, value="ron",
                                          command=self.click_button_ron, style='Method.TRadiobutton')
        self.method_zimo = ttk.Radiobutton(self.root, text="自摸", variable=self.method_choose, value="zimo",
                                           command=self.click_button_zimo, style='Method.TRadiobutton')

        self.score_change = [0, 0, 0, 0]

    def click_button_ryuukyoku(self):
        pass

    def click_button_ron(self):
        loser = tk.StringVar()
        loser_self = ttk.Radiobutton(self.root, text="自家", variable=loser, value="self", style="Method.TRadiobutton")
        loser_kamicha = ttk.Radiobutton(self.root, text="上家", variable=loser, value="kamicha",
                                        style="Method.TRadiobutton")
        loser_toimen = ttk.Radiobutton(self.root, text="对家", variable=loser, value="toimen",
                                       style="Method.TRadiobutton")
        loser_shimocha = ttk.Radiobutton(self.root, text="下家", variable=loser, value="shimocha",
                                         style="Method.TRadiobutton")

        loser_self.place(x=20, y=60)
        loser_kamicha.place(x=90, y=60)
        loser_toimen.place(x=160, y=60)
        loser_shimocha.place(x=230, y=60)

        label_deal_to = tk.Label(self.root, text="放铳至", font=("Helvetica", 20, "bold"))
        label_deal_to.place(x=10, y=90)

        winner_list = []


    def click_button_zimo(self):
        pass

    def excu_changeScore(self):
        self.root.title("changeScore")
        self.root.geometry("400x400")

        self.method_ryuukyoku.place(x=60, y=20)
        self.method_ron.place(x=160, y=20)
        self.method_zimo.place(x=260, y=20)

        self.root.mainloop()
