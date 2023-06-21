from calculation import calculation
import tkinter as tk
from tkinter import ttk

winner_player_y = 150
visible_winner_self = True

class changeScore:
    # class ron_select:
    #     def __init__(self,root,winner):
    #
    #         han_count = tk.StringVar()
    #         self.han_1 = ttk.Radiobutton(root, text="1", variable=han_count, value=1, style="Winner.TRadiobutton")
    #         self.han_2 = ttk.Radiobutton(root, text="2", variable=han_count, value=2, style="Winner.TRadiobutton")
    #         self.han_3 = ttk.Radiobutton(root, text="3", variable=han_count, value=3, style="Winner.TRadiobutton")
    #         self.han_4 = ttk.Radiobutton(root, text="4", variable=han_count, value=4, style="Winner.TRadiobutton")
    #         self.han_mangan = ttk.Radiobutton(root, text="满贯", variable=han_count, value="满贯",
    #                                      style="Winner.TRadiobutton")
    #         self.han_haneman = ttk.Radiobutton(root, text="跳满", variable=han_count, value="跳满",
    #                                       style="Winner.TRadiobutton")
    #         self.han_baiman = ttk.Radiobutton(root, text="倍满", variable=han_count, value="倍满",
    #                                      style="Winner.TRadiobutton")
    #         self.han_sanbaiman = ttk.Radiobutton(root, text="三倍满", variable=han_count, value="三倍满",
    #                                         style="Winner.TRadiobutton")
    #         self.han_yakuman = ttk.Radiobutton(root, text="役满", variable=han_count, value="役满",
    #                                       style="Winner.TRadiobutton")
    #
    #         fu_count = tk.StringVar()
    #         self.fu_null = ttk.Radiobutton(root, text="-", variable=fu_count, value=0, style="Winner.TRadiobutton")
    #         self.fu_20 = ttk.Radiobutton(root, text=20, variable=fu_count, value=20, style="Winner.TRadiobutton")
    #         self.fu_30 = ttk.Radiobutton(root, text=30, variable=fu_count, value=30, style="Winner.TRadiobutton")
    #         self.fu_40 = ttk.Radiobutton(root, text=40, variable=fu_count, value=40, style="Winner.TRadiobutton")
    #
    #     def place(self,coordinate):
    #         pass
    #
    #     def __del__(self):


    def __init__(self, main, cal):
        global winner_player_y
        winner_player_y = 150

        self.main = main
        self.current_score = cal
        self.root = tk.Toplevel(self.main)

        self.style_method = ttk.Style()
        self.style_method.configure('Method.TRadiobutton', font=("Helvetica", 20, "bold"))
        self.style_winner = ttk.Style()
        self.style_winner.configure('Winner.TRadiobutton', font=("Helvetica", 14, "bold"))
        self.method_choose = tk.StringVar()
        self.method_ryuukyoku = ttk.Radiobutton(self.root, text="流局", variable=self.method_choose, value="ryuukyoku",
                                                command=self.click_button_ryuukyoku, style='Method.TRadiobutton')
        self.method_ron = ttk.Radiobutton(self.root, text="荣和", variable=self.method_choose, value="ron",
                                          command=self.click_button_ron, style='Method.TRadiobutton')
        self.method_zimo = ttk.Radiobutton(self.root, text="自摸", variable=self.method_choose, value="zimo",
                                           command=self.click_button_zimo, style='Method.TRadiobutton')
        self.button_confirm = tk.Button(self.root, text="确认", font=("Helvetica", 20, "bold"),
                                        command=self.click_confirm)
        self.score_change = [0, 0, 0, 0]

    def click_button_ryuukyoku(self):
        pass

    def click_button_ron(self):

        def click_winner_self():
            global winner_player_y
            if winner_player_y >= 375:
                raise ValueError("Not Valid winner number")
            label_winner_self = tk.Label(self.root, text="自家", font=("Helvetica", 14, "bold"))
            label_winner_self.place(x=10, y=winner_player_y)
            winner_player_y += 25
            widget_list = winner_score_board()
            winner_player_y += 25

        def click_winner_kamicha():
            global winner_player_y
            if winner_player_y >= 375:
                raise ValueError("Not Valid winner number")
            label_winner_kamicha = tk.Label(self.root, text="上家", font=("Helvetica", 14, "bold"))
            label_winner_kamicha.place(x=10, y=winner_player_y)
            winner_player_y += 25
            widget_list = winner_score_board()
            winner_player_y += 25

        def click_winner_toimen():
            global winner_player_y
            if winner_player_y >= 375:
                raise ValueError("Not Valid winner number")
            label_winner_toimen = tk.Label(self.root, text="对家", font=("Helvetica", 14, "bold"))
            label_winner_toimen.place(x=10, y=winner_player_y)
            winner_player_y += 25
            widget_list = winner_score_board()
            winner_player_y += 25

        def click_winner_shimocha():
            global winner_player_y
            if winner_player_y >= 375:
                raise ValueError("Not Valid winner number")
            label_winner_shimocha = tk.Label(self.root, text="下家", font=("Helvetica", 14, "bold"))
            label_winner_shimocha.place(x=10, y=winner_player_y)
            winner_player_y += 25
            widget_list = winner_score_board()
            winner_player_y += 25


        def winner_score_board():
            global winner_player_y
            han_count = tk.StringVar()
            han_1 = ttk.Radiobutton(self.root, text="1", variable=han_count, value=1, style="Winner.TRadiobutton")
            han_2 = ttk.Radiobutton(self.root, text="2", variable=han_count, value=2, style="Winner.TRadiobutton")
            han_3 = ttk.Radiobutton(self.root, text="3", variable=han_count, value=3, style="Winner.TRadiobutton")
            han_4 = ttk.Radiobutton(self.root, text="4", variable=han_count, value=4, style="Winner.TRadiobutton")
            han_mangan = ttk.Radiobutton(self.root, text="满贯", variable=han_count, value="满贯",
                                         style="Winner.TRadiobutton")
            han_haneman = ttk.Radiobutton(self.root, text="跳满", variable=han_count, value="跳满",
                                          style="Winner.TRadiobutton")
            han_baiman = ttk.Radiobutton(self.root, text="倍满", variable=han_count, value="倍满",
                                         style="Winner.TRadiobutton")
            han_sanbaiman = ttk.Radiobutton(self.root, text="三倍满", variable=han_count, value="三倍满",
                                            style="Winner.TRadiobutton")
            han_yakuman = ttk.Radiobutton(self.root, text="役满", variable=han_count, value="役满",
                                          style="Winner.TRadiobutton")
            han_1.place(x=0, y=winner_player_y)
            han_2.place(x=30, y=winner_player_y)
            han_3.place(x=60, y=winner_player_y)
            han_4.place(x=90, y=winner_player_y)
            han_mangan.place(x=120, y=winner_player_y)
            han_haneman.place(x=170, y=winner_player_y)
            han_baiman.place(x=220, y=winner_player_y)
            han_sanbaiman.place(x=270, y=winner_player_y)
            han_yakuman.place(x=340, y=winner_player_y)

            winner_player_y += 25

            fu_count = tk.StringVar()
            fu_null = ttk.Radiobutton(self.root, text="-", variable=fu_count, value=0, style="Winner.TRadiobutton")
            fu_20 = ttk.Radiobutton(self.root, text=20, variable=fu_count, value=20, style="Winner.TRadiobutton")
            fu_30 = ttk.Radiobutton(self.root, text=30, variable=fu_count, value=30, style="Winner.TRadiobutton")
            fu_40 = ttk.Radiobutton(self.root, text=40, variable=fu_count, value=40, style="Winner.TRadiobutton")

            fu_20.place(x=0, y=winner_player_y)
            fu_30.place(x=40, y=winner_player_y)
            fu_40.place(x=80, y=winner_player_y)
            fu_null.place(x=120, y=winner_player_y)

            score_board_list = [han_1, han_2, han_3, han_4, han_mangan, han_haneman, han_baiman, han_sanbaiman,
                                han_yakuman, fu_20, fu_30, fu_40]

            return score_board_list

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

        winner_self = tk.Button(self.root, text="自家", font=("Helvetica", 20, "bold"), command=click_winner_self)
        winner_kamicha = tk.Button(self.root, text="上家", font=("Helvetica", 20, "bold"), command=click_winner_kamicha)
        winner_toimen = tk.Button(self.root, text="对家", font=("Helvetica", 20, "bold"), command=click_winner_toimen)
        winner_shimo = tk.Button(self.root, text="下家", font=("Helvetica", 20, "bold"), command=click_winner_shimocha)

        winner_self.place(x=10, y=120)
        winner_kamicha.place(x=90, y=120)
        winner_toimen.place(x=170, y=120)
        winner_shimo.place(x=250, y=120)

        winner_list = []

    def click_button_zimo(self):
        pass

    def click_confirm(self):
        self.score_change = [0, 1, 2, 3]
        self.root.quit()
        self.root.destroy()

    def excu_changeScore(self):
        self.root.title("changeScore")
        self.root.geometry("400x400")

        self.method_ryuukyoku.place(x=60, y=20)
        self.method_ron.place(x=160, y=20)
        self.method_zimo.place(x=260, y=20)

        self.button_confirm.place(x=300, y=370)
        self.root.mainloop()
