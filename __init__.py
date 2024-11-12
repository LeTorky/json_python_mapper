from json_schema_mapper.json_schema_mapper import JSONSchemaMapper

from pydantic import RootModel

schema = """
    {
        test: string;
        pew: integer;
    }[]
"""

x = JSONSchemaMapper(schema)
model = RootModel[x.pydantic_model]

print(model([{"test": '1', "pew": 1}]).root[0])
