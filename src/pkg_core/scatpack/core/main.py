import pkgutil
import importlib
import scatpack.plugin


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in iter_namespace(scatpack.plugin)
}


def summer(x, y):
    return x + y + x + y


def run(arg1, arg2):
    print(f"Name  = Core")
    print(f"Value = {summer(arg1, arg2)}")
    if 'scatpack.plugin.plugin_a' in discovered_plugins:
        plugin_a = discovered_plugins['scatpack.plugin.plugin_a']
        print(f"Name = {plugin_a.name}")
        print(f"Value= {plugin_a.multiplier(arg1, arg2)}")
    if 'scatpack.plugin.plugin_b' in discovered_plugins:
        plugin_b = discovered_plugins['scatpack.plugin.plugin_b']
        print(f"Name = {plugin_b.name}")
        print(f"Value= {plugin_b.subtractor(arg1, arg2)}")
    print("finished")


if __name__ == "__main__":
    run(1, 2)
