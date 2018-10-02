from django.db import models

from .store import store


class Position(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.FloatField()
    purchase_price = models.FloatField()

    @classmethod
    def build_from_dict(cls, data):
        """
        Build instance from dict
        """

        return cls(
            symbol=data['symbol'],
            quantity=float(data['quantity']),
            purchase_price=float(data['purchase_price']),
        )

    @property
    def current_price(self):
        price = store.get_price_of_symbol(self.symbol)

        # Return current price if found, else return purchase price
        return price or self.purchase_price

    @property
    def market_value(self):
        return self.quantity * self.current_price

    @property
    def portfolio_percent(self):
        return self.market_value / store.total_market_value

    @property
    def profit_loss(self):
        return (self.current_price - self.purchase_price) * self.quantity

    def sell(self, trade):
        self.quantity -= trade.quantity

    def buy(self, trade):
        self.purchase_price = (self.purchase_price *
                               self.quantity + trade.price * trade.quantity) / (self.quantity + trade.quantity)
        self.quantity += trade.quantity


class Price(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.FloatField()

    @classmethod
    def build_from_dict(cls, data):
        """
        Build instance from dict
        """

        return cls(
            symbol=data['symbol'],
            price=float(data['price']),
        )


class Trade(models.Model):
    TRADE_SIDE_SELL = 'sell'
    TRADE_SIDE_BUY = 'buy'

    TRADE_SIDES = (
        (TRADE_SIDE_SELL, 'Sell'),
        (TRADE_SIDE_BUY, 'Buy'),
    )

    side = models.CharField(choices=TRADE_SIDES, max_length=10)
    symbol = models.CharField(max_length=10)
    quantity = models.FloatField()
    price = models.FloatField()

    @classmethod
    def build_from_dict(cls, data):
        """
        Build instance from dict
        """

        return cls(
            side=data['side'],
            symbol=data['symbol'],
            quantity=float(data['quantity']),
            price=float(data['price']),
        )
