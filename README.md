# Police Auction Watch

Monitor propertyroom.com and notify over slack when new products are listed that were uploaded by police/other public

## Configuring
Set the `police_auction_watch_slack_hook` environment variable (supports .env) with a slack hook. Optionally set the args in a json string in `police_auction_watch_args`

## Running
Arguments should be passed in JSON to STDIN or placed in the `police_auction_watch_args` environment variable

    echo '{"query": "vehicle", "police_only": true}' | police_auction_watch

police_auction_watch.sh can be used to run with docker

    echo '{"query": "vehicle", "police_only": true}' | ./police_auction_watch.sh



### Arguments
**query**: search query on the auction website  
**police_only**: limit search to police and public auctions only
