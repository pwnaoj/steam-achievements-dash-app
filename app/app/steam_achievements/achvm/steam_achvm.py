"""steam_achvm.py"""
from ..steam.api import Api


class SteamAchievements(Api):

    def __init__(self):
        super().__init__()
        self._app_list = None

    @property
    def app_list(self):
        return self._app_list

    @app_list.setter
    def app_list(self, r):
        if isinstance(r, dict):
            try:
                self._app_list = r['applist']['apps']
            except KeyError:
                self._app_list = []


steam_achvm = SteamAchievements()
