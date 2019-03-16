#!/usr/bin/python3
"""Flask application executable."""
from neo4jmoviesapi.flask_api import app


def main():
    app.debug = True
    app.run(host='localhost', port=5000)


if __name__ == '__main__':
    main()

