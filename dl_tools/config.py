from collections import OrderedDict

import yaml

CONFIG_TYPE = "_type"


class ConfigError(Exception):
    """Exception class for errors in config."""
    pass


def read_config(filename):
    with open(filename) as fp:
        return yaml.safe_load(fp)


def write_config(config, filename):
    with open(filename, "w") as fp:
        yaml.dump(config, fp)


def prepare_config(self, config=None):
    """Set defaults and check fields.

    Config is a dictionary of values. Method creates new config using
    default class config. Result config keys are the same as default config keys.

    Args:
        self: object with get_default_config method.
        config: User-provided config.

    Returns:
        Config dictionary with defaults set.
    """
    default_config = self.get_default_config()
    if config is None:
        config = {}
    elif isinstance(config, str):
        config = read_config(config)
    elif not isinstance(config, dict):
        raise ConfigError("Config dictionary or filename expected, got {}".format(type(config)))

    # Check type.
    if CONFIG_TYPE in config:
        cls_name = type(self).__name__
        if cls_name != config[CONFIG_TYPE]:
            raise ConfigError("Type mismatch: expected {}, got {}".format(
                config[CONFIG_TYPE], cls_name))

    # Merge configs.
    for key in config:
        if key == CONFIG_TYPE:
            continue
        if key not in default_config:
            raise ConfigError("Unknown parameter {}".format(key))
    new_config = OrderedDict()
    for key, value in default_config.items():
        new_config[key] = config.get(key, value)
    return new_config
