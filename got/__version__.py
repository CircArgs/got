import toml
version = __version__ = toml.load("pyproject.toml")["tool"]["poetry"]["version"]
