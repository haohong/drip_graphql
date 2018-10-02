import graphene

import positions.schema


class Query(positions.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
