import importlib.metadata

try:
    __core__ = importlib.metadata.version("animdl2")
except importlib.metadata.PackageNotFoundError:
    import pathlib

    from animdl2.utils.optopt import regexlib
    __core__ = regexlib.search(
        r'name = "animdl2"\nversion = "(.+?)"',
        (pathlib.Path(__file__).parent.parent / "pyproject.toml").read_text(),
    ).group(1)

