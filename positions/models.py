from django.db import models


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
