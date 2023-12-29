import random
import pandas as pd


class MissionsDeck:
    def __init__(self, missions_df):
        missions_df["id_mission"] = range(len(missions_df))
        self.big_missions = missions_df[missions_df["points"] >= 20].sample(frac=1).reset_index(drop=True)
        self.simple_missions = (missions_df[missions_df["points"] < 20]).sample(frac=1).reset_index(drop=True)
        self.discard_missions_pile = pd.DataFrame(columns=missions_df.columns)

    def get_one_big_mission(self):
        big_mission_choosen = self.big_missions.iloc[0]
        self.big_missions = self.big_missions.drop(self.big_missions.index[0], inplace=True)
        return big_mission_choosen

    def get_simple_missions(self):
        self._refill_simple_missions()
        simple_missions_choosen = self.simple_missions.iloc[:3]
        self.simple_missions = self.simple_missions.drop(self.simple_missions.index[:3], inplace=True)
        return simple_missions_choosen

    def discard_mission(self, id_mission, player_missions_deck):
        mission_choosen = player_missions_deck[player_missions_deck["id_mission"] == id_mission]
        if mission_choosen["points"] >= 20:
            return player_missions_deck.drop(mission_choosen.index, inplace=True)
        else:
            self.discard_missions_pile = pd.concat([self.discard_missions_pile, mission_choosen], ignore_index=True)
            return player_missions_deck.drop(mission_choosen.index, inplace=True)

    def _refill_simple_missions(self):
        if len(self.simple_missions) == 0:
            self.simple_missions = self.discard_missions_pile.sample(frac=1).reset_index(drop=True)
            self.discard_missions_pile = pd.DataFrame(columns=self.simple_missions.columns)

        elif len(self.simple_missions) < 3:
            self.simple_missions = pd.concat(
                [self.simple_missions, self.discard_missions_pile.sample(frac=1).reset_index(drop=True)], ignore_index=True
            )
            self.discard_missions_pile = pd.DataFrame(columns=self.simple_missions.columns)
