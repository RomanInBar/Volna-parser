import os

from dotenv import load_dotenv

load_dotenv()


class Configuration:
    DRIVER = 'sqlite'
    DB_NAME: str = 'storage.db'

    @property
    def get_url(self):
        return f"{self.DRIVER}:///{self.DB_NAME}"


conf = Configuration()
