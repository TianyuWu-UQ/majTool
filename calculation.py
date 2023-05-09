import table


def translate_score_text(score):
    if isinstance(score.get_hand()[0], str):
        if score.get_hand()[0] == "mangan":
            return "满贯"
        if score.get_hand()[0] == "haneman":
            return "跳满"
        if score.get_hand()[0] == "baiman":
            return "倍满"
        if score.get_hand()[0] == "sanbaiman":
            return "三倍满"
        if score.get_hand()[0] == "yakuman":
            return "役满"
    else:
        return "{}番{}符".format(score.get_hand()[0], score.get_hand()[1])


class calculation:
    """
    todo:完场判断以及判断条件
        终局pt收入估算（和段位相关，对四位无法得出精确pt）
    """

    def __init__(self, s=250, kami=250, toimen=250, shimo=250, rcb_c=0, hb_c=0, isDealer=0):
        self.score_self = dict(name="自家", score=s)
        self.score_kamicha = dict(name="上家", score=kami)
        self.score_toimen = dict(name="对家", score=toimen)
        self.score_shimocha = dict(name="下家", score=shimo)
        self.reach_bar_count = rcb_c
        self.honba_count = hb_c
        self.isDealer = isDealer
        self.table = table.SCORE_TABLE

        if isDealer == -1:
            raise ValueError("没有选择庄家")
        if not self.reach_bar_count * 10 + self.score_self["score"] + self.score_kamicha["score"] + self.score_toimen[
            "score"] + self.score_shimocha["score"] == 1000:
            raise ValueError("无效分数")

    def get_rank_order(self):
        rank_order = [self.score_self, self.score_kamicha, self.score_toimen, self.score_shimocha]
        for i in range(4):
            for j in range(0, 4 - i - 1):
                if rank_order[j]["score"] < rank_order[j + 1]["score"]:
                    rank_order[j], rank_order[j + 1] = rank_order[j + 1], rank_order[j]
        return rank_order

    """
    to calculate how big your hand needed to get the target
    """

    def chase(self):
        """
        todo:
            give a int as score that required to chase up the competitor
                a boolean if the competitor is the dealer
        """
        if self.first_rank_judge():
            return "已经是一位"
        else:
            competitor_name = self.get_competitor()
            score = 0
            for player in self.get_rank_order():
                if player["name"] == competitor_name:
                    score = player["score"] - self.score_self["score"]
            is_competitor_dealer = False
            if (self.isDealer == 1) and (competitor_name == "上家"):
                is_competitor_dealer = True
            if (self.isDealer == 2) and (competitor_name == "对家"):
                is_competitor_dealer = True
            if (self.isDealer == 3) and (competitor_name == "下家"):
                is_competitor_dealer = True
            return self.find_point(score, is_competitor_dealer)

    """
    To judge whether current score of all player can end game,
    if not, calculate how much score is required to end.
    :return True if game can be ended
        or a score that are required to end game.
    """

    def end_game_judge(self):
        rank_order = self.get_rank_order()
        if rank_order[0]["score"] < 300:
            for index, rank in enumerate(rank_order):
                if rank["name"] == "自家":
                    score_self = rank["score"]
                    diff = 300 - score_self
                    return diff
        else:
            return True

    def first_rank_judge(self):
        rank_order = self.get_rank_order()
        if rank_order[0]["name"] == "自家":
            return True
        else:
            return False

    def find_point(self, score, is_competitor_dealer):
        # if self is the dealer

        if self.isDealer == 0:
            result_ron = min([x for han in self.table[0] for x in han if
                              x.get_ron() > (score - self.reach_bar_count * 10 - self.honba_count * 3)],
                             key=lambda k: k.get_ron())
            result_ron_hit = min([x for han in self.table[0] for x in han if
                                  x.get_ron() > ((score - self.reach_bar_count * 10 - self.honba_count * 3) * 0.5)],
                                 key=lambda k: k.get_ron())
            result_zimo = min([x for han in self.table[0] for x in han if (x.get_zimo() * 3) > (
                    (score - self.reach_bar_count * 10 - self.honba_count * 3) * 0.75)],
                              key=lambda k: k.get_ron())
        # if self is not the dealer
        else:
            if is_competitor_dealer:
                result_ron = min([x for han in self.table[1] for x in han if
                                  x.get_ron() > (score - self.reach_bar_count * 10 - self.honba_count * 3)],
                                 key=lambda k: k.get_ron())
                result_ron_hit = min([x for han in self.table[1] for x in han if
                                      x.get_ron() > ((score - self.reach_bar_count * 10 - self.honba_count * 3) * 0.5)],
                                     key=lambda k: k.get_ron())
                result_zimo = min([x for han in self.table[1] for x in han if
                                   (x.get_zimo()[0] * 2 + x.get_zimo()[1]) > (
                                           (score - self.reach_bar_count * 10 - self.honba_count * 3) * 2 / 3)],
                                  key=lambda k: k.get_ron())
            else:
                result_ron = min([x for han in self.table[1] for x in han if
                                  x.get_ron() > (score - self.reach_bar_count * 10 - self.honba_count * 3)],
                                 key=lambda k: k.get_ron())
                result_ron_hit = min([x for han in self.table[1] for x in han if
                                      x.get_ron() > ((score - self.reach_bar_count * 10 - self.honba_count * 3) * 0.5)],
                                     key=lambda k: k.get_ron())
                result_zimo = min([x for han in self.table[1] for x in han if
                                   (x.get_zimo()[0] * 2 + x.get_zimo()[1]) > (
                                           (score - self.reach_bar_count * 10 - self.honba_count * 3) * 4 / 5)],
                                  key=lambda k: k.get_ron())
        return self.print_score(result_ron, result_ron_hit, result_zimo)

    """
    ron, ron_hit, zimo: score 
    competitor: 1/2/3
    """

    def print_score(self, ron, ron_hit, zimo):
        text = ""
        text += "荣和直击{}：{}".format(self.get_competitor(), translate_score_text(ron_hit)) + "\n"
        text += "荣和别家：{}".format(translate_score_text(ron)) + "\n"
        text += "自摸：{}".format(translate_score_text(zimo))
        return text

    def get_competitor(self):
        for index, player in enumerate(self.get_rank_order()):
            if player["name"] == "自家":
                competitor_score = self.get_rank_order()[index - 1]["score"]
                competitor_list = [x for x in self.get_rank_order() if x["score"] == competitor_score]
                if self.isDealer == 1:
                    for competitor in competitor_list:
                        if competitor["name"] == "上家":
                            return "上家"
                elif self.isDealer == 2:
                    for competitor in competitor_list:
                        if competitor["name"] == "对家":
                            return "对家"
                elif self.isDealer == 3:
                    for competitor in competitor_list:
                        if competitor["name"] == "下家":
                            return "下家"
                return competitor_list[0]["name"]
