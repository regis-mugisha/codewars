class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def inc_progress(self, activity_rank):
        if activity_rank not in self.ranks:
            raise ValueError("Invalid activity rank")

        if self.rank == 8:
            self.progress = 0
            return

        user_index = self.ranks.index(self.rank)
        activity_index = self.ranks.index(activity_rank)
        diff = activity_index - user_index

        if diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        elif diff > 0:
            self.progress += 10 * diff * diff

        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            user_index = self.ranks.index(self.rank)
            self.rank = self.ranks[user_index + 1]

        if self.rank == 8:
            self.progress = 0
