import csv


def import_csv_into_models(filename, model_cls):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(
            file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)

        return [model_cls.build_from_dict(row) for row in csv_reader]


class DataStore:
    """
    DataStore class that mocks db store read from CSV
    """

    POSITION_CSV = 'data/position.csv'
    PRICE_CSV = 'data/price.csv'
    TRADE_CSV = 'data/trade.csv'

    def __init__(self):
        self.positions = []
        self.prices = []
        self.trades = []

    def load_all(self):
        self.load_positions()
        self.load_prices()
        self.load_trades()

    def load_positions(self):
        from .models import Position

        self.positions = import_csv_into_models(self.POSITION_CSV, Position)

    def load_prices(self):
        from .models import Price

        self.prices = import_csv_into_models(self.PRICE_CSV, Price)

    def load_trades(self):
        from .models import Trade

        self.trades = import_csv_into_models(self.TRADE_CSV, Trade)


store = DataStore()
