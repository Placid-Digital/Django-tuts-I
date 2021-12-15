import graphene
from graphene_django import DjangoObjectType
from. models import person


class PersonType(DjangoObjectType):
    class Meta:
        model = person
        fields = ('first_name', 'email', 'phone_no', 'password', 'address')


class Query(graphene.ObjectType):
    person = graphene.List(PersonType)

    def resolve_person(root, info, **kwargs):
        # Querying a list
        return person.objects.all()


schema = graphene.Schema(query=Query)
