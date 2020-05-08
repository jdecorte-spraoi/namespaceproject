import pkg_resources
import json

value_mapper_definition = json.loads(pkg_resources.resource_string(__name__, 'value_mapper_definitions.json')).get("valueMapperDefinitions")
