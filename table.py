"""
create a 2D list to store all possible score
factor: dealer or challenger
        zimo or ron
        hand value
todo:
    make it 3D to store both dealer and challenger's data in one list
optimisation:
    try to read all scores from a txt file to shrink the length of this file
"""

"""
20 25 30 40 
"""
col = 4
"""
1 2 3 4 5("mangan") 6-7("haneman") 8-10("baiman") 11-12("sanbaiman") >13("yakuman")
"""
row = 9


class score:
    def __init__(self, han, fu, score_ron, score_zimo):
        self.hand = (han, fu)
        self.ron = score_ron
        self.zimo = score_zimo
        # notice a challenger zimo may cause 2 different score for
        # other challengers and dealer

    def get_hand(self):
        return self.hand

    def get_ron(self):
        return self.ron

    def get_zimo(self):
        return self.zimo


# make SCORE_TABLE[0] for dealer and [1] for challenger
default_score = score(0, 0, 0, 0)
SCORE_TABLE = [[[default_score for j in range(col)] for i in range(row)] for k in range(2)]

SCORE_TABLE[0][0][2] = score(1, 30, 15, 5)
SCORE_TABLE[1][0][2] = score(1, 30, 10, (3, 5))
SCORE_TABLE[0][0][3] = score(1, 40, 20, 7)
SCORE_TABLE[1][0][3] = score(1, 40, 13, (4, 7))
SCORE_TABLE[0][1][0] = score(2, 20, 20, 7)
SCORE_TABLE[1][1][0] = score(2, 20, 13, (4, 7))
SCORE_TABLE[0][1][1] = score(2, 25, 24, 8)
SCORE_TABLE[1][1][1] = score(2, 25, 16, (4, 8))
SCORE_TABLE[0][1][2] = score(2, 30, 29, 10)
SCORE_TABLE[1][1][2] = score(2, 30, 20, (5, 10))
SCORE_TABLE[0][1][3] = score(2, 40, 39, 13)
SCORE_TABLE[1][1][3] = score(2, 40, 26, (7, 13))
SCORE_TABLE[0][2][0] = score(3, 20, 39, 13)
SCORE_TABLE[1][2][0] = score(3, 20, 26, (7, 13))
SCORE_TABLE[0][2][1] = score(3, 25, 48, 16)
SCORE_TABLE[1][2][1] = score(3, 25, 32, (8, 16))
SCORE_TABLE[0][2][2] = score(3, 30, 58, 20)
SCORE_TABLE[1][2][2] = score(3, 30, 39, (10, 20))
SCORE_TABLE[0][2][3] = score(3, 40, 77, 26)
SCORE_TABLE[1][2][3] = score(3, 40, 52, (13, 26))
SCORE_TABLE[0][3][0] = score(4, 20, 77, 26)
SCORE_TABLE[1][3][0] = score(4, 20, 52, (13, 26))
SCORE_TABLE[0][3][1] = score(4, 25, 96, 32)
SCORE_TABLE[1][3][1] = score(4, 25, 64, (16, 32))
SCORE_TABLE[0][3][2] = score(4, 30, 116, 39)
SCORE_TABLE[1][3][2] = score(4, 30, 77, (20, 39))
SCORE_TABLE[0][3][3] = score("mangan", 0, 120, 40)
SCORE_TABLE[1][3][3] = score("mangan", 0, 80, (20, 40))
SCORE_TABLE[0][4][0] = score("mangan", 0, 120, 40)
SCORE_TABLE[1][4][0] = score("mangan", 0, 80, (20, 40))
SCORE_TABLE[0][5][2] = score("haneman", 0, 180, 60)
SCORE_TABLE[1][5][2] = score("haneman", 0, 120, (30, 60))
SCORE_TABLE[0][6][2] = score("baiman", 0, 240, 80)
SCORE_TABLE[1][6][2] = score("baiman", 0, 160, (40, 80))
SCORE_TABLE[0][7][2] = score("sanbaiman", 0, 360, 120)
SCORE_TABLE[1][7][2] = score("sanbaiman", 0, 240, (60, 120))
SCORE_TABLE[0][8][2] = score("yakuman", 0, 480, 160)
SCORE_TABLE[1][8][2] = score("yakuman", 0, 320, (80, 160))

default_score_challenger = score(0, 0, 0, (0, 0))
for han in range(len(SCORE_TABLE[1])):
    for fu in range(len(SCORE_TABLE[1][han])):
        if SCORE_TABLE[1][han][fu].get_ron() == 0:
            SCORE_TABLE[1][han][fu] = default_score_challenger

# print(SCORE_TABLE)
# print(len(SCORE_TABLE), len(SCORE_TABLE[0]), len(SCORE_TABLE[0][0]))
# print(SCORE_TABLE[0][0][2].get_zimo())
