import pkgutil
import importlib
import scatpack.plugin

plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in pkgutil.iter_modules(scatpack.plugin.__path__, scatpack.plugin.__name__ + ".")
}


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
    print("finished")


if __name__ == "__main__":
    run(1, 2)
