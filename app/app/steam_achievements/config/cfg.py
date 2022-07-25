"""cfg.py"""
import configparser
import os


class Config:

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(os.path.dirname(os.path.realpath(__file__)) + '/config.ini')
        self._api_config = self._config['steam']

    @property
    def api_config(self):
        return self._api_config


config = Config()
