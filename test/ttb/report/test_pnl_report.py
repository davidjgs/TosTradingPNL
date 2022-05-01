from unittest import TestCase

from ttb.report.pnl_report import PnlReporter, PnlReporter_RPA


class TestPnlReporter(TestCase):

    def setUp(self) -> None:
        pass

    def test_gen_report(self):
        data = [
            {"event_type": "PNL", "ticker": "SPXL", "price_bought": 115.51, "price_sold": 115.42,
             "price_chg_pct": -0.0779, "qty": 100, "time_bought": "2022/04/20-09:37:58",
             "time_sold": "2022/04/20-09:38:28", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "SPXL", "price_bought": 115.28, "price_sold": 115.19,
             "price_chg_pct": -0.0781, "qty": 100, "time_bought": "2022/04/20-09:40:09",
             "time_sold": "2022/04/20-09:40:29", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "DAL", "price_bought": 43.8, "price_sold": 43.67, "price_chg_pct": -0.2968,
             "qty": 100, "time_bought": "2022/04/20-09:42:21", "time_sold": "2022/04/20-09:42:41",
             "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#", "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "DAL", "price_bought": 43.54, "price_sold": 43.3999,
             "price_chg_pct": -0.3218, "qty": 100, "time_bought": "2022/04/20-09:44:22",
             "time_sold": "2022/04/20-09:45:02", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "LABD", "price_bought": 41.08, "price_sold": 41.56, "price_chg_pct": 1.1685,
             "qty": 100, "time_bought": "2022/04/20-09:44:23", "time_sold": "2022/04/20-10:04:28",
             "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#", "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "SPXS", "price_bought": 18.3, "price_sold": 18.28, "price_chg_pct": -0.1093,
             "qty": 100, "time_bought": "2022/04/20-09:49:53", "time_sold": "2022/04/20-10:14:40",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "LABU", "price_bought": 12.285, "price_sold": 12.17,
             "price_chg_pct": -0.9361, "qty": 100, "time_bought": "2022/04/20-10:14:00",
             "time_sold": "2022/04/20-10:27:46", "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#",
             "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "ASO", "price_bought": 42.31, "price_sold": 42.4, "price_chg_pct": 0.2127,
             "qty": 100, "time_bought": "2022/04/20-10:12:59", "time_sold": "2022/04/20-10:28:47",
             "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#", "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "CEIX", "price_bought": 46.72, "price_sold": 47.22, "price_chg_pct": 1.0702,
             "qty": 100, "time_bought": "2022/04/20-10:14:02", "time_sold": "2022/04/20-10:31:59",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "BTU", "price_bought": 30.2, "price_sold": 29.99, "price_chg_pct": -0.6954,
             "qty": 100, "time_bought": "2022/04/20-10:24:54", "time_sold": "2022/04/20-10:49:39",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "CRXT", "price_bought": 2.05, "price_sold": 2.245, "price_chg_pct": 9.5122,
             "qty": 100, "time_bought": "2022/04/20-10:30:37", "time_sold": "2022/04/20-10:50:39",
             "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#", "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "AR", "price_bought": 35.76, "price_sold": 35.75, "price_chg_pct": -0.028,
             "qty": 100, "time_bought": "2022/04/20-10:38:02", "time_sold": "2022/04/20-10:53:51",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "GNK", "price_bought": 24.91, "price_sold": 25.04, "price_chg_pct": 0.5219,
             "qty": 100, "time_bought": "2022/04/20-10:14:02", "time_sold": "2022/04/20-10:53:52",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "APA", "price_bought": 44.2, "price_sold": 44.44, "price_chg_pct": 0.543,
             "qty": 100, "time_bought": "2022/04/20-10:14:00", "time_sold": "2022/04/20-10:58:14",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "M", "price_bought": 26.81, "price_sold": 26.72, "price_chg_pct": -0.3357,
             "qty": 100, "time_bought": "2022/04/20-10:18:22", "time_sold": "2022/04/20-10:58:15",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "METC", "price_bought": 17.3, "price_sold": 17.5564,
             "price_chg_pct": 1.4821, "qty": 100, "time_bought": "2022/04/20-10:39:05",
             "time_sold": "2022/04/20-11:01:36", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "TQQQ", "price_bought": 49.06, "price_sold": 48.945,
             "price_chg_pct": -0.2344, "qty": 100, "time_bought": "2022/04/20-10:18:21",
             "time_sold": "2022/04/20-11:02:37", "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#",
             "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "FNGU", "price_bought": 14.9701, "price_sold": 14.9687,
             "price_chg_pct": -0.0094, "qty": 100, "time_bought": "2022/04/20-10:20:32",
             "time_sold": "2022/04/20-11:02:37", "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#",
             "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "HZO", "price_bought": 42.21, "price_sold": 42.07, "price_chg_pct": -0.3317,
             "qty": 100, "time_bought": "2022/04/20-10:20:33", "time_sold": "2022/04/20-11:02:37",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "PLTR", "price_bought": 12.97, "price_sold": 12.995,
             "price_chg_pct": 0.1928, "qty": 1.0, "time_bought": "2022/04/20-10:41:34",
             "time_sold": "2022/04/20-11:08:10", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "GSL", "price_bought": 25.4604, "price_sold": 25.4899,
             "price_chg_pct": 0.1159, "qty": 100, "time_bought": "2022/04/20-10:38:03",
             "time_sold": "2022/04/20-11:17:36", "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#",
             "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "EDRY", "price_bought": 39.2, "price_sold": 39.1947,
             "price_chg_pct": -0.0135, "qty": 93.0, "time_bought": "2022/04/20-10:40:13",
             "time_sold": "2022/04/20-11:19:48", "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#",
             "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "METC", "price_bought": 17.23, "price_sold": 17.77, "price_chg_pct": 3.1341,
             "qty": 100, "time_bought": "2022/04/20-10:24:55", "time_sold": "2022/04/20-11:26:21",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "EGY", "price_bought": 7.63, "price_sold": 7.66, "price_chg_pct": 0.3932,
             "qty": 100, "time_bought": "2022/04/20-10:38:03", "time_sold": "2022/04/20-11:46:24",
             "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#", "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "JBLU", "price_bought": 13.125, "price_sold": 13.225,
             "price_chg_pct": 0.7619, "qty": 100, "time_bought": "2022/04/20-10:39:05",
             "time_sold": "2022/04/20-11:51:48", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "SQQQ", "price_bought": 38.43, "price_sold": 39.06, "price_chg_pct": 1.6393,
             "qty": 100, "time_bought": "2022/04/20-09:44:21", "time_sold": "2022/04/20-12:00:25",
             "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#", "version": "V5.4", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "SBLK", "price_bought": 30.33, "price_sold": 30.31,
             "price_chg_pct": -0.0659, "qty": 100, "time_bought": "2022/04/20-10:38:02",
             "time_sold": "2022/04/20-12:07:59", "buy_scanner": "#B4#V5.4.1#", "sell_scanner": "#B4#V5.4.1#",
             "version": "V5.4.1", "pnl_type": "REALIZED"},
            {"event_type": "PNL", "ticker": "LABU", "price_bought": 12.5302, "price_sold": 12.8501,
             "price_chg_pct": 2.553, "qty": 100, "time_bought": "2022/04/20-10:34:50",
             "time_sold": "2022/04/20-12:59:18", "buy_scanner": "#B4#V5.4#", "sell_scanner": "#B4#V5.4#",
             "version": "V5.4", "pnl_type": "REALIZED"},
        ]
        pnl_reporter = PnlReporter_RPA()
        pnl_reporter.gen_report(data)
