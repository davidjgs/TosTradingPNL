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

class PriceReader:

    def __init__(self, config: Config):
        self.conf = config or Config()
        self.eod_price_file_path = self.conf.eod_price_file_path

    def read(self):
        logger.info("getting eod prices from files ...")
        num_tries = 0
        while num_tries < 20:
            if not path.exists(self.eod_price_file_path):
                logger.info(f"File {self.eod_price_file_path} not exist ... ")
                time.sleep(30)
                num_tries += 1
            else:
                eod_p_file = open(self.eod_price_file_path, "r")
                lines = eod_p_file.readlines()
                prices = json.loads(lines[0])
                return prices['eod_prices']
        return {}