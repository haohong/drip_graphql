import graphene
from graphene_django import DjangoObjectType

from .models import Position
from .store import store


class PositionType(DjangoObjectType):
    class Meta:
        model = Position


class Query(graphene.ObjectType):
    positions = graphene.List(PositionType)

    def resolve_positions(self, info, **kwargs):
        return store.positions
