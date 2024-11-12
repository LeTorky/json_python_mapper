from json_schema_mapper.json_schema_mapper import JSONSchemaMapper

schema = """
    {
        test: string;
        pew: integer;
    }
"""

x = JSONSchemaMapper(schema)
[print(entry.type) for entry in x.mapped_type.mapped_children]
