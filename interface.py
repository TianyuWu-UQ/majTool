import tkinter as tk
import platform
from calculation import calculation


class interface:
    def __init__(self):
        self.OS = platform.system()
        self.isDealer = -1
        self.root = tk.Tk()

        self.button_Dealer_self = tk.Button(self.root, text="庄", command=self.click_isDealer_self)
        self.button_Dealer_kamicha = tk.Button(self.root, text="庄", command=self.click_isDealer_kamicha)
        self.button_Dealer_toimen = tk.Button(self.root, text="庄", command=self.click_isDealer_toimen)
        self.button_Dealer_shimocha = tk.Button(self.root, text="庄", command=self.click_isDealer_shimocha)
        self.label_self = tk.Label(self.root, text="自家：")
        self.label_self_00 = tk.Label(self.root, text="00")
        self.label_kamicha = tk.Label(self.root, text="上家：")
        self.label_kamicha_00 = tk.Label(self.root, text="00")
        self.label_toimen = tk.Label(self.root, text="对家：")
        self.label_toimen_00 = tk.Label(self.root, text="00")
        self.label_shimocha = tk.Label(self.root, text="下家：")
        self.label_shimocha_00 = tk.Label(self.root, text="00")
        self.text_self = tk.Text(self.root)
        self.text_kamicha = tk.Text(self.root)
        self.text_toimen = tk.Text(self.root)
        self.text_shimocha = tk.Text(self.root)
        self.label_reach_bar_count = tk.Label(self.root, text="立直棒：")
        self.text_reach_bar_count = tk.Text(self.root)
        self.label_honba_count = tk.Label(self.root, text="x本场：")
        self.text_honba_count = tk.Text(self.root)
        self.button_calculate = tk.Button(self.root, text="计算", command=self.calculate)
        font_output = ("Helvetica", 16)
        self.label_output = tk.Label(self.root, text="输入场况")

    def click_isDealer_self(self):
        self.isDealer = 0
        if self.OS == "Windows":
            self.button_Dealer_self.config(bg="red")
            self.button_Dealer_kamicha.config(bg="SystemButtonFace")
            self.button_Dealer_toimen.config(bg="SystemButtonFace")
            self.button_Dealer_shimocha.config(bg="SystemButtonFace")
        else:

            self.button_Dealer_self.config(highlightbackground="red")
            self.button_Dealer_kamicha.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_toimen.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_shimocha.config(highlightbackground="SystemButtonFace")

    def click_isDealer_kamicha(self):
        self.isDealer = 1
        if self.OS == "Windows":
            self.button_Dealer_self.config(bg="SystemButtonFace")
            self.button_Dealer_kamicha.config(bg="red")
            self.button_Dealer_toimen.config(bg="SystemButtonFace")
            self.button_Dealer_shimocha.config(bg="SystemButtonFace")
        else:
            self.button_Dealer_self.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_kamicha.config(highlightbackground="red")
            self.button_Dealer_toimen.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_shimocha.config(highlightbackground="SystemButtonFace")

    def click_isDealer_toimen(self):
        self.isDealer = 2
        if self.OS == "Windows":
            self.button_Dealer_self.config(bg="SystemButtonFace")
            self.button_Dealer_kamicha.config(bg="SystemButtonFace")
            self.button_Dealer_toimen.config(bg="red")
            self.button_Dealer_shimocha.config(bg="SystemButtonFace")
        else:
            self.button_Dealer_self.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_kamicha.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_toimen.config(highlightbackground="red")
            self.button_Dealer_shimocha.config(highlightbackground="SystemButtonFace")

    def click_isDealer_shimocha(self):
        self.isDealer = 3
        if self.OS == "Windows":
            self.button_Dealer_self.config(bg="SystemButtonFace")
            self.button_Dealer_kamicha.config(bg="SystemButtonFace")
            self.button_Dealer_toimen.config(bg="SystemButtonFace")
            self.button_Dealer_shimocha.config(bg="red")
        else:
            self.button_Dealer_self.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_kamicha.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_toimen.config(highlightbackground="SystemButtonFace")
            self.button_Dealer_shimocha.config(highlightbackground="red")

    def calculate(self):
        if self.OS == "Windows":
            self.button_calculate.config(bg="red")
            self.root.after(100, lambda: self.button_calculate.config(bg="SystemButtonFace"))
        else:
            self.button_calculate.config(highlightbackground="red")
            self.root.after(100, lambda: self.button_calculate.config(highlightbackground="SystemButtonFace"))

        score_self = self.get_score(self.text_self)
        score_kamicha = self.get_score(self.text_kamicha)
        score_toimen = self.get_score(self.text_toimen)
        score_shimocha = self.get_score(self.text_shimocha)
        reach_bar_count = self.get_extra(self.text_reach_bar_count)
        honba_count = self.get_extra(self.text_honba_count)

        try:
            cal = calculation(score_self, score_kamicha, score_toimen, score_shimocha, reach_bar_count, honba_count,
                              self.isDealer)

            self.label_output.config(text=cal.chase())
        except Exception as e:
            self.label_output.config(text=str(e))

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def get_score(self, widget):
        text = widget.get("1.0", "end-1c")
        if not text:
            return 250
        else:
            return int(text)

    def get_extra(self, widget):
        text = widget.get("1.0", "end-1c")
        if not text:
            return 0
        else:
            return int(text)

    def button_next_return(self):
        self.text_self.bind("<Return>", self.focus_next_widget)
        self.text_kamicha.bind("<Return>", self.focus_next_widget)
        self.text_toimen.bind("<Return>", self.focus_next_widget)
        self.text_shimocha.bind("<Return>", self.focus_next_widget)
        self.text_reach_bar_count.bind("<Return>", self.focus_next_widget)
        self.text_honba_count.bind("<Return>", self.focus_next_widget)

    def exec_Darwin(self):
        self.root.title("Mahjong Tool")
        self.root.geometry("400x500")

        font = ("Helvetica", 20, "bold")

        self.button_Dealer_self.config(font=font, width=2, height=2)
        self.button_Dealer_kamicha.config(font=font, width=2, height=2)
        self.button_Dealer_toimen.config(font=font, width=2, height=2)
        self.button_Dealer_shimocha.config(font=font, width=2, height=2)

        self.label_self.config(font=font)
        self.label_kamicha.config(font=font)
        self.label_toimen.config(font=font)
        self.label_shimocha.config(font=font)

        self.label_self_00.config(font=font)
        self.label_kamicha_00.config(font=font)
        self.label_toimen_00.config(font=font)
        self.label_shimocha_00.config(font=font)

        self.text_self.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)
        self.text_kamicha.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)
        self.text_toimen.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)
        self.text_shimocha.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)

        self.label_reach_bar_count.config(font=font)
        self.text_reach_bar_count.config(highlightthickness=1, highlightbackground="black", height=1, width=2,
                                         font=font)
        self.label_honba_count.config(font=font)
        self.text_honba_count.config(highlightthickness=1, highlightbackground="black", height=1, width=2, font=font)
        self.button_calculate.config(font=font, width=10, height=1)
        font_output = ("Helvetica", 16)
        self.label_output.config(background="grey", width=40, height=9, font=font_output)

        self.button_next_return()

        self.button_Dealer_self.place(x=10, y=10)
        self.button_Dealer_kamicha.place(x=10, y=70)
        self.button_Dealer_toimen.place(x=10, y=130)
        self.button_Dealer_shimocha.place(x=10, y=190)
        self.label_self.place(x=70, y=20)
        self.label_self_00.place(x=190, y=20)
        self.label_kamicha.place(x=70, y=80)
        self.label_kamicha_00.place(x=190, y=80)
        self.label_toimen.place(x=70, y=140)
        self.label_toimen_00.place(x=190, y=140)
        self.label_shimocha.place(x=70, y=200)
        self.label_shimocha_00.place(x=190, y=200)
        self.text_self.place(x=140, y=20)
        self.text_kamicha.place(x=140, y=80)
        self.text_toimen.place(x=140, y=140)
        self.text_shimocha.place(x=140, y=200)
        self.label_reach_bar_count.place(x=250, y=100)
        self.text_reach_bar_count.place(x=330, y=100)
        self.label_honba_count.place(x=250, y=150)
        self.text_honba_count.place(x=330, y=150)
        self.button_calculate.place(x=120, y=250)
        self.label_output.place(x=10, y=300)

        self.root.mainloop()

    def exec_Windows(self):
        self.root.title("Mahjong Tool")
        self.root.geometry("400x500")

        font = ("simsunb.ttf", 19, "bold")

        self.button_Dealer_self.config(font=font, width=3, height=1)
        self.button_Dealer_kamicha.config(font=font, width=3, height=1)
        self.button_Dealer_toimen.config(font=font, width=3, height=1)
        self.button_Dealer_shimocha.config(font=font, width=3, height=1)

        self.label_self.config(font=font)
        self.label_kamicha.config(font=font)
        self.label_toimen.config(font=font)
        self.label_shimocha.config(font=font)

        self.label_self_00.config(font=font)
        self.label_kamicha_00.config(font=font)
        self.label_toimen_00.config(font=font)
        self.label_shimocha_00.config(font=font)

        self.text_self.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)
        self.text_kamicha.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)
        self.text_toimen.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)
        self.text_shimocha.config(highlightthickness=1, highlightbackground="black", height=1, width=4, font=font)

        self.label_reach_bar_count.config(font=font)
        self.text_reach_bar_count.config(highlightthickness=1, highlightbackground="black", height=1, width=2,
                                         font=font)
        self.label_honba_count.config(font=font)
        self.text_honba_count.config(highlightthickness=1, highlightbackground="black", height=1, width=2, font=font)
        self.button_calculate.config(font=font, width=10, height=1)
        font_output = ("Helvetica", 13)
        self.label_output.config(background="grey", width=40, height=9, font=font_output)

        self.button_next_return()

        self.button_Dealer_self.place(x=10, y=10)
        self.button_Dealer_kamicha.place(x=10, y=70)
        self.button_Dealer_toimen.place(x=10, y=130)
        self.button_Dealer_shimocha.place(x=10, y=190)
        self.label_self.place(x=72, y=20)
        self.label_self_00.place(x=220, y=20)
        self.label_kamicha.place(x=72, y=80)
        self.label_kamicha_00.place(x=220, y=80)
        self.label_toimen.place(x=72, y=140)
        self.label_toimen_00.place(x=220, y=140)
        self.label_shimocha.place(x=72, y=200)
        self.label_shimocha_00.place(x=220, y=200)
        self.text_self.place(x=155, y=20)
        self.text_kamicha.place(x=155, y=80)
        self.text_toimen.place(x=155, y=140)
        self.text_shimocha.place(x=155, y=200)
        self.label_reach_bar_count.place(x=255, y=100)
        self.text_reach_bar_count.place(x=360, y=100)
        self.label_honba_count.place(x=255, y=150)
        self.text_honba_count.place(x=360, y=150)
        self.button_calculate.place(x=120, y=250)
        self.label_output.place(x=20, y=320)

        self.root.mainloop()
        pass

    def execute(self):
        if self.OS == "Windows":
            self.exec_Windows()
        if self.OS == "Darwin":
            self.exec_Darwin()
