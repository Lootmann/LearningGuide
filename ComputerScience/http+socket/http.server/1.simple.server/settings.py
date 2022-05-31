import yaml


def get_setting(filename: str) -> dict:
    d = {}

    with open(filename, "r") as f:
        yml = yaml.safe_load(f)
        d = yml

    return d
