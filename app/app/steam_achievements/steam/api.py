"""api.py"""
import httpx

from ..config.cfg import config


class Api:

    def __init__(self):
        self._base_api = config.api_config['base_api_url']
        self._base_store = config.api_config['base_store_url']
        self._user_key = config.api_config['user_key']

    # GetAppList
    def get_app_list(self, endpoint: str = 'ISteamApps/GetAppList/v2/') -> dict:
        """Gets the complete list of public apps."""
        with httpx.Client(base_url=self._base_api) as client:
            params = {
                'format': 'json'
            }
            r = client.get(url=endpoint, params=params)
            r_ = r.json()

        return r_

    # GetAppDetails
    def get_app_details(self, appids: int, endpoint: str = 'api/appdetails') -> dict:
        """Get all the details of public apps."""
        with httpx.Client(base_url=self._base_store) as client:
            params = {
                'format': 'json',
                'appids': appids
            }
            r = client.get(url=endpoint, params=params)
            r_ = r.json()

        return r_

    # GetNumberOfCurrentPlayers
    def get_number_of_current_players(self, appid: int, endpoint: str = 'ISteamUserStats/GetNumberOfCurrentPlayers/v1/') -> dict:
        """Get all the details of public apps."""
        with httpx.Client(base_url=self._base_api) as client:
            params = {
                'format': 'json',
                'appid': appid
            }
            r = client.get(url=endpoint, params=params)
            r_ = r.json()

        return r_
