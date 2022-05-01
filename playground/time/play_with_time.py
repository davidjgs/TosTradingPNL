from datetime import datetime

import dateutil.parser


def parse_time(ts):
    time = 'Mon, 31 Jan 2022 09:08:15 -0600 (CST)'
    timestamp = dateutil.parser.parse(time).timestamp()
    dt =datetime.fromtimestamp(timestamp)
    print(dt)

parse_time('Mon, 31 Jan 2022 09:08:15 -0600 (CST)')