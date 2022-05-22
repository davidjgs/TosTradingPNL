import datetime
import json
import logging
import time
from queue import Queue
import os.path
from os import path
import dateutil.parser
import schedule

from ttb.cfg.config import Config
from ttb.util import timeutil

d_fmt = "%Y-%m-%dT%H:%M:%S"
logger = logging.getLogger(__name__)

class AlertReader:

    def __init__(self, config: Config, event_q: Queue):
        self.conf = config or Config()
        self.event_q = event_q
        self.alert_file_path = self.conf.alert_file_path
        self.alert_pull_interval_seconds = self.conf.alert_pull_interval_seconds
        self.cut_off_time_str = self.conf.trade_end_time
        self.cut_off_time = timeutil.parse_time(self.conf.trade_end_time)
        self.trade_start_time = timeutil.parse_time(self.conf.trade_start_time)
        self.buy_start_time = timeutil.parse_time(self.conf.buy_start_time)
        self.buy_end_time = timeutil.parse_time(self.conf.buy_end_time)
        self.alert_last_ts = 0

    def start(self):
        logger.info("getting alert ...")
        schedule.every(self.alert_pull_interval_seconds).seconds.until(self.cut_off_time_str).do(self.get_alert)
        while datetime.datetime.now().timestamp() < self.cut_off_time.timestamp():
            n = schedule.idle_seconds()
            if n and n > 0:
                logger.info(f'sleeping for {n} seconds ...')
                time.sleep(n)
            schedule.run_pending()

    def get_alert(self):
        # Reading from file
        logger.info(f"getting alert from {self.alert_file_path}")
        if not path.exists(self.alert_file_path):
            logger.info(f"File {self.alert_file_path} not exist ... ")
        else:
            alert_file = open(self.alert_file_path, "r")
            lines = alert_file.readlines()
            logger.info(f'Total records in file: {len(lines)}')
            i=1
            new_alert_c = 0
            for line in lines:
                #logger.info(f'processing line {i}')
                alert = json.loads(line)
                ts = alert['ts']
                dt = dateutil.parser.parse(ts)
                if self.alert_last_ts == 0 or dt.timestamp() > self.alert_last_ts:
                    action = alert['action']
                    if self.good_time_to_action(action, dt):
                        logger.info(f'==> new alert: {alert}')
                        sym_price_pairs = alert['search_results']
                        version = alert['version']
                        ts = alert['ts']
                        self.event_q.put((sym_price_pairs, action, version, ts))
                        self.alert_last_ts = max(dt.timestamp(), self.alert_last_ts)
                    else:
                        logger.info(f'alert out of time scope. ignored. alert = {alert} ')
                    new_alert_c += 1
                i+=1
            alert_file.close()
            logger.info(f'Total new alerts: {new_alert_c}')

    def good_time_to_action(self, action, dt: datetime):
        return self.within_trading_hours(dt) and (action != "BUY" or self.good_time_to_buy(dt))

    def within_trading_hours(self, dt: datetime):
        return self.trade_start_time.timestamp() < dt.timestamp() < self.cut_off_time.timestamp()

    def good_time_to_buy(self, dt):
        return self.buy_start_time.timestamp() < dt.timestamp() < self.buy_end_time.timestamp()

