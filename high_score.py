from os import path


class HighScore:

    def __init__(self):
        self.high_score = 0

    def new_score(self, score):
        if (score > self.high_score):
            self.high_score = score
            self.save()

    def load(self):
        if (not path.exists("tetris_high_score.txt")):
            return
        score_file = open("tetris_high_score.txt", "r")
        try:
            self.high_score = int(score_file.read())
        finally:
            score_file.close()

    def save(self):
        score_file = open("tetris_high_score.txt", "w")
        try:
            score_file.write(str(self.high_score))
        finally:
            score_file.close()


high_score = HighScore()
high_score.load()
