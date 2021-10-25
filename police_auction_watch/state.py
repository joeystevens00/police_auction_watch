from typing import Dict
import json
import os

from .models import AuctionArgs


def init_state_dir():
    if not os.path.isdir('state'):
        os.mkdir('state')

def filename(args: AuctionArgs, source: str):
    police_str = "police-" if args.police_only else ""
    return f'state/{args.slug}-{source}.json'


def save(args: AuctionArgs, source: str, last: Dict):
    init_state_dir()
    with open(filename(args, source), 'w') as f:
        f.write(json.dumps(last))


def load(args: AuctionArgs, source: str):
    if os.path.exists(filename(args, source)):
        with open(filename(args, source), 'r') as f:
            return json.load(f)
