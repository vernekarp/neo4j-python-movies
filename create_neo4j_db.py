#!/usr/bin/python3
"""A Post-install script which is used to create a Neo4j movie datastore nodes and its
relationships.

This script will be automatically executed via ``setup.py`` during installation.
"""
import os
from neo4j import GraphDatabase, basic_auth

from neo4jmoviesapi.utils import load_conf


def get_cypher_query(filename="etc/movies.cql"):
    """This method reads the cypher query from a input ``filename`` and
    returns in the form of string

    :param str filename: Absolute path of CQL filename.
    :return str: Cypher query.
    """
    if not os.path.isfile(filename):
        raise FileNotFoundError('file not found: {}'.format(filename))

    with open(filename, 'r') as data:
        cql = data.readlines()

    return ''.join(cql)


def create_neo4j_nodes(cypher_query):
    """Creates nodes and its relationship in the DB based on the ``cypher_query``

    :param str cypher_query: Query to be executed on neo4j DB
    """
    if not cypher_query:
        raise RuntimeError('No CQL found.')

    config = load_conf()
    driver = GraphDatabase.driver(config['uri'], auth=basic_auth(config['username'], config['password']))

    with driver.session() as db_session:
        db_session.run(cypher_query)


def main():
    """Main Program."""
    cypher_query = get_cypher_query()
    create_neo4j_nodes(cypher_query)


if __name__ == "__main__":
    main()
