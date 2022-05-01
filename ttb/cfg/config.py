import os
from datetime import datetime

from ttb.util.singleton import Singleton

fmt_Ymd = "%Y%m%d"


class Config(metaclass=Singleton):
    def __init__(self, config_file=None):
        self.config_file = config_file

    @property
    def alert_pull_interval_seconds(self):
        return 10

    @property
    def date_today(self):
        return datetime.now().strftime(fmt_Ymd)

    ## trading day start time
    @property
    def trade_start_time(self):
        return "9:30"

    ## BUY start time
    @property
    def buy_start_time(self):
        return "9:30"

    ## BUY end time
    @property
    def buy_end_time(self):
        return "15:00"

    ## trading day end time
    @property
    def trade_end_time(self):
        return "16:00"

    ## default by quantity
    @property
    def trade_default_qty(self):
        return 100

    @property
    def trades_journal(self):
        return "trades"

    @property
    def events_journal(self):
        return "events"

    @property
    def pnl_journal(self):
        return "pnl"

    @property
    def open_positions_journal(self):
        return "open_positions"

    @property
    def gdrive_path(self):
        return "G:\\My Drive\\TradingBot"
        #return "C:\\tosBot\\reports"

    @property
    def out_dir(self):
        return f'{self.gdrive_path}{os.sep}{self.date_today}_rpa'

    @property
    def input_dir(self):
        return f'{self.gdrive_path}{os.sep}{self.date_today}'
        #return f'C:/tosBot{os.sep}{self.date_today}'

    @property
    def alert_file_path(self):
        return f'{self.input_dir}{os.sep}scanner_alerts_extended_{self.date_today}.json'
