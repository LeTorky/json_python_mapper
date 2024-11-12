from typing import List

from json_schema_mapper.mapper_types import MappedType
from json_schema_mapper.type_mapper import (
    DictOpenMapper,
    DictCloseMapper,
    ArrayMapper,
    OptionalMapper,
    StringMapper,
    IntegerMapper,
    FloatMapper,
    BooleanMapper,
    SemiColonMapper
)


class JSONSchemaMapper:

    def __init__(self, json_schema: str):
        self.__json_schema = self.__clean_string(json_schema)
        self.__mapped_type_stack: List[MappedType] = []
        self.__perform_mapping(self.__json_schema)

    def __clean_string(self, json_schema: str) -> str:
        return json_schema.replace('\n', '').strip().replace(' ', '')

    def __perform_mapping(self, json_schema: str):

        while json_schema:
            first_entry = json_schema[0]

            match first_entry:

                case '{':
                    mapper = DictOpenMapper
                case '}':
                    mapper = DictCloseMapper
                case '[':
                    mapper = ArrayMapper
                case '?':
                    mapper = OptionalMapper
                case ';':
                    mapper = SemiColonMapper
                case _:
                    colon_index = json_schema.find(':')
                    semi_colon_index = json_schema.find(';')

                    if semi_colon_index != -1 and semi_colon_index != -1:
                        var_type = json_schema[colon_index +
                                               1: semi_colon_index]
                        match var_type:
                            case "string":
                                mapper = StringMapper
                            case "float":
                                mapper = FloatMapper
                            case "integer":
                                mapper = IntegerMapper
                            case "boolean":
                                mapper = BooleanMapper
                            case "{":
                                mapper = DictOpenMapper

            mapper_instance = mapper(self.__mapped_type_stack)
            json_schema = mapper_instance.perform_mapping_on_list(json_schema)

    @property
    def mapped_type(self) -> MappedType:
        return self.__mapped_type_stack[0]