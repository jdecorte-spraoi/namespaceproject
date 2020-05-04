# try:
#     import monorepo.plugin_a.scatpack.plugin_a
#     plugin_a = True
# except ImportError:
#     plugin_a = False
#
# try:
#     import monorepo.plugin_b.scatpack.plugin_b
#     plugin_b = True
# except ImportError:
#     plugin_b = False


def summer(x, y):
    return x + y + x + y


def run(arg1, arg2):
    print(f"Name  = Core")
    print(f"Value = {summer(arg1, arg2)}")
    # if plugin_a:
    #     print(f"Name = {plugin_a.name}")
    #     print(f"Value= {plugin_a.multiplier(arg1, arg2)}")
    # if plugin_b:
    #     print(f"Name = {plugin_b.name}")
    #     print(f"Value= {plugin_b.subtractor(arg1, arg2)}")
    print("finished")


if __name__ == "__main__":
    run(1, 2)
