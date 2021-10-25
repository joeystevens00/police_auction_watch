from pydantic import BaseModel

class AuctionArgs(BaseModel):
    query: str
    police_only: bool = False

    @property
    def slug(self):
        police_str = "-police" if self.police_only else ""
        return f"{self.query}{police_str}"
