import os

from dotenv import load_dotenv

load_dotenv()


class Configuration:
    DRIVER: str = os.getenv("DRIVER")
    DB_NAME: str = os.getenv("DB_NAME")

    @property
    def get_url(self):
        return f"{self.DRIVER}:///database/{self.DB_NAME}"


conf = Configuration()
