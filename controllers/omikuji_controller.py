import random
import pandas as pd
class OmikujiController:
    def __init__(self):
        self.data = pd.read_csv("/Users/khein21502/Documents/中間/project1/data/omikuji_fortune.csv")
        self.omikuji_list = self.data["運勢"].tolist()
        self.result = random.choice(self.omikuji_list)
    def draw(self):
        today_data = self.data[self.data["運勢"] == self.result]
        return today_data

    




    