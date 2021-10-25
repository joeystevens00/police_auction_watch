from typing import Optional

from pydantic import BaseSettings

class Settings(BaseSettings):
    slack_hook: str
    args: Optional[str]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'police_auction_watch_'

config = Settings()
