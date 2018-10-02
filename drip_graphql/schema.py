import graphene

import positions.schema


class Query(positions.schema.Query, graphene.ObjectType):
    pass


class Mutation(positions.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
