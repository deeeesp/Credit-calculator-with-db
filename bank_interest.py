class BankInterest(object):

    def __init__(self, summ, perc, period):
        self.summ = summ
        self.perc = perc
        self.period = period

    def diff_int(self):
        arr = []
        mp_cnt = self.period * 12
        rest = self.summ
        mp_real = self.summ / (self.period * 12.0)
        while mp_cnt != 0:
            mp = mp_real + (rest * self.perc / 1200)
            arr.append(round(mp, 2))
            rest = rest - mp_real
            mp_cnt = mp_cnt - 1
        return arr, sum(arr)

    def ann_int(self):
        mp_cnt = self.period * 12
        r = self.perc / 1200.0
        ak = (r * (1 + r) ** mp_cnt) / (((1 + r) ** mp_cnt) - 1)
        mp = self.summ * ak
        total = mp * mp_cnt
        return round(mp, 2), total
