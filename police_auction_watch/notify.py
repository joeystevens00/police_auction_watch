from typing import Dict

import requests
import json

from .config import config
from .models import AuctionArgs

def new_product(args: AuctionArgs, source: str, product: Dict):
    res = requests.post(
        config.slack_hook,
        json={
            "text": (
                f"New product ({args.slug}) listing on {source}:"
                f" \"{product['name']}\" {product['link']} price {product['last_price']}"
                f" time remaining {product['time_remaining']}"
            )
        }
    )
    print(res, res.text)
