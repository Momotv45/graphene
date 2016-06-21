
from graphql import GraphQLInputObjectType, GraphQLString
from graphql.type.definition import GraphQLInputFieldDefinition

from ..field import InputField
from ..inputobjecttype import InputObjectType
from ..scalars import String


def test_generate_inputobjecttype():
    class MyObjectType(InputObjectType):
        '''Documentation'''

    graphql_type = MyObjectType._meta.graphql_type
    assert isinstance(graphql_type, GraphQLInputObjectType)
    assert graphql_type.name == "MyObjectType"
    assert graphql_type.description == "Documentation"


def test_generate_inputobjecttype_with_meta():
    class MyObjectType(InputObjectType):

        class Meta:
            name = 'MyOtherObjectType'
            description = 'Documentation'

    graphql_type = MyObjectType._meta.graphql_type
    assert isinstance(graphql_type, GraphQLInputObjectType)
    assert graphql_type.name == "MyOtherObjectType"
    assert graphql_type.description == "Documentation"


def test_empty_inputobjecttype_has_meta():
    class MyObjectType(InputObjectType):
        pass

    assert MyObjectType._meta


def test_generate_objecttype_with_fields():
    class MyObjectType(InputObjectType):
        field = InputField(GraphQLString)

    graphql_type = MyObjectType._meta.graphql_type
    fields = graphql_type.get_fields()
    assert 'field' in fields
    assert isinstance(fields['field'], GraphQLInputFieldDefinition)


def test_generate_objecttype_with_graphene_fields():
    class MyObjectType(InputObjectType):
        field = String()

    graphql_type = MyObjectType._meta.graphql_type
    fields = graphql_type.get_fields()
    assert 'field' in fields
    assert isinstance(fields['field'], GraphQLInputFieldDefinition)
