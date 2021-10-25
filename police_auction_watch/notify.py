from typing import Dict

import requests
import json

from .config import config
from .models import AuctionArgs

def new_product(args: AuctionArgs, source: str, product: Dict):
    res = requests.post(
        config.slack_hook,
        json={
            "text": f"New product ({args.slug}) listing on {source}: " + json.dumps(product),
        }
    )
    print(res, res.text)
