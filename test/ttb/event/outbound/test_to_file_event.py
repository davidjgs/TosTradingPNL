from unittest import TestCase

from ttb.cfg.config import Config
from ttb.data.event_type import EventType
from ttb.event.outbound.to_file_event import ToFileEventHandler


class TestToFileEventHandler(TestCase):
    def setUp(self):
        self.e_handler = ToFileEventHandler(conf=Config())

    def test_handle_event(self):
        long_positions = {'AMRS': {'price': 4.55, 'exec_time': '2022/02/02-15:20:52'},
                          'CHPT': {'price': 13.6111, 'exec_time': '2022/02/02-15:20:53'},
                          'CI': {'price': 230.43, 'exec_time': '2022/02/02-15:20:53'},
                          'CRWD': {'price': 178.42, 'exec_time': '2022/02/02-15:20:54'},
                          'HL': {'price': 4.995, 'exec_time': '2022/02/02-15:20:54'},
                          'KKR': {'price': 72.82, 'exec_time': '2022/02/02-15:20:55'},
                          'MNKD': {'price': 3.655, 'exec_time': '2022/02/02-15:20:55'},
                          'SWN': {'price': 4.8099, 'exec_time': '2022/02/02-15:20:56'},
                          'UPST': {'price': 107.02, 'exec_time': '2022/02/02-15:20:56'},
                          'YNDX': {'price': 48.14, 'exec_time': '2022/02/02-15:20:57'},
                          'HIG': {'price': 73.155, 'exec_time': '2022/02/02-15:39:03'}
                          }
        payload = dict(event_type=EventType.POSITIONS, positions=long_positions)
        self.e_handler.handle_event(payload)
