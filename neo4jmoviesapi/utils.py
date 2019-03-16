import os
import json


def load_conf(conf_file="etc/neo4jnode.secrets"):
    """Loads and parses a neo4j configuration file and returns in the form
    of dictionary.

    :param str conf_file: Absolute path of configuration file
    :return dict: Configuration data.
    """
    if not os.path.isfile(conf_file):
        raise FileNotFoundError('Config file not found: {}'.format(conf_file))

    with open(conf_file, 'r') as conf:
        conf_data = conf.read()

    return json.loads(conf_data)
