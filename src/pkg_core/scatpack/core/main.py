import pkgutil
import pkg_resources
import importlib
import json

from scatpack.core.models import catalog

try:
    import scatpack.plugin

    plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules(scatpack.plugin.__path__, scatpack.plugin.__name__ + ".")
    }
except ModuleNotFoundError:
    plugins = dict()

env = "dev"
config = importlib.import_module(f"..config_{env}", __name__).Config()

master_steps = json.loads(pkg_resources.resource_string("scatpack.core", "step_definitions.json")).get('steps')
if plugins:
    # check for new or updated steps in plugins
    for plugin in plugins.values():
        if pkg_resources.resource_exists(plugin.__name__, "steps"):
            steps_module = importlib.import_module(".steps", plugin.__name__)
            if pkg_resources.resource_exists(steps_module.__name__, "step_definitions.json"):
                plugin_steps = json.loads(pkg_resources.resource_string(steps_module.__name__,
                                                                        "step_definitions.json")).get("steps")
                master_steps.extend(plugin_steps)


def summer(x, y):
    return x + y + x + y


def run(arg1, arg2):
    print(f"Name  = Core")
    print(f"Value = {summer(arg1, arg2)}")
    if 'scatpack.plugin.plugin_a' in plugins:
        plugin_a = plugins['scatpack.plugin.plugin_a']
        print(f"Name = {plugin_a.name}")
        print(f"Value= {plugin_a.multiplier(arg1, arg2)}")
    if 'scatpack.plugin.plugin_b' in plugins:
        plugin_b = plugins['scatpack.plugin.plugin_b']
        print(f"Name = {plugin_b.name}")
        print(f"Value= {plugin_b.subtractor(arg1, arg2)}")
    print(f"Config key = {config.key}")
    print(f"Steps = {','.join([x['displayName'] for x in master_steps])}")
    print(f"Catalog = {','.join([x['name'] for x in catalog.value_mapper_definition])}")
    print("finished")


if __name__ == "__main__":
    run(1, 2)
