class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, prog_rank):
        rank_spectrum = range(-8, 9)
        rank_spectrum.remove(0)

        rank_diff = (rank_spectrum.index(prog_rank) -
                     rank_spectrum.index(self.rank))
        if rank_diff == 0:
            new_progress = 3
        elif rank_diff > 0:
            new_progress = 10*rank_diff*rank_diff
        elif rank_diff < -2:
            new_progress = 0
        else:
            new_progress = 1
        self.progress += new_progress

        while self.progress >= 100:
            self.progress -= 100
            self.rank = rank_spectrum[rank_spectrum.index(self.rank) + 1]

        if self.rank == 8:
            self.progress = 0
