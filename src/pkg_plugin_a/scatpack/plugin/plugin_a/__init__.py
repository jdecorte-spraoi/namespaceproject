import sys

if sys.version_info.major == 3 and sys.version_info.minor < 8:
    from importlib_metadata import version
else:
    from importlib.metadata import version

# __version__ = '0.1.0'
__version__ = version('scatpack.plugina')


name = "multiplier"


def multiplier(x, y):
    return x * y * x * y
