import json
import sys
from typing import Dict

from . import propertyroom, notify
from .state import get_state, get_state_file, save_state
from .models import AuctionArgs


SOURCES = {
    'propertyroom': propertyroom.check_auctions
}


def run(args: AuctionArgs):
    for source, check_function in SOURCES.items():
        last = get_state(args, source) or {}
        current = check_function(args) or {}
        save_state(args, source, current)
        if last.get("name") != current.get("name"):
            notify.new_product(args, source, current)


def cli():
    args = None
    from .config import config
    if config.args:
        args = json.loads(config.args)
    else:
        input = sys.stdin.read()
        if input:
            args = json.loads(input)
    run(AuctionArgs(**args))
