from typing import Dict
import json
import os

from .models import AuctionArgs

def get_state_file(args: AuctionArgs, source: str):
    police_str = "police-" if args.police_only else ""
    return f'state/{args.slug}-{source}.json'


def save_state(args: AuctionArgs, source: str, last: Dict):
    with open(get_state_file(args, source), 'w') as f:
        f.write(json.dumps(last))


def get_state(args: AuctionArgs, source: str):
    if os.path.exists(get_state_file(args, source)):
        with open(get_state_file(args, source), 'r') as f:
            return json.load(f)
