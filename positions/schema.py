import graphene
from graphene_django import DjangoObjectType

from .models import Position
from .store import store


class PositionType(DjangoObjectType):
    class Meta:
        model = Position

    current_price = graphene.Float()
    market_value = graphene.Float()
    portfolio_percent = graphene.Float()
    profit_loss = graphene.Float()


class Query(graphene.ObjectType):
    positions = graphene.List(PositionType)

    def resolve_positions(self, info, **kwargs):
        return store.positions
