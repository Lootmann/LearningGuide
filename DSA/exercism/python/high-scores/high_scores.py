class HighScores:
    def __init__(self, scores):
        self.s = scores

    @property
    def scores(self):
        return self.s

    def latest(self):
        return self.s[-1]

    def personal_best(self):
        return max(self.s)

    def personal_top_three(self):
        result = self.s.copy()
        result.sort(reverse=True)

        return result[:3]
