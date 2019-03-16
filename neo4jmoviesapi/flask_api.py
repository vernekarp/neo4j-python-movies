"""Simple Flask API library interacting with Neo4j Movies Datastore.

This library provides access to Movies datastore using below API's:
    actor/<name>: Lists out the movie's title on which the actor ``name`` has acted in.
    movie/<title>: Lists out the actors name who have acted in the movie ``title``.

These APIs can be access (using a web browser or CURL command) as:
    http://<hostname>:<port>/actor/<name>
    http://<hostname>:<port>/movie/<title>
"""
from json import dumps
from flask import Flask, g, Response
from neo4j.v1 import GraphDatabase, basic_auth

from .utils import load_conf

app = Flask(__name__)
config = load_conf()
driver = GraphDatabase.driver(config['uri'], auth=basic_auth(config['username'], config['password']))


def get_db():
    """Loads and returns a DB session object.

    :return GraphDatabase.driver.session: Neo4j DB session object.
    """
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


@app.teardown_appcontext
def close_db(error):
    """Handles the DB session closure upon app termination."""
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()


@app.route("/actor/<name>")
def get_movie_by_actor(name):
    """Flask API provides a GET method, which responses with a list of movie titles
    on which the actor ``name`` has acted in.

    :param str name: Full name of the actor as per Neo4j datastore.
    :return flask.Response: List of movie titles along with actor name."""
    db = get_db()
    results = db.run("MATCH (actor:Person {name: {name}})-[:ACTED_IN]->(actorMovies) "
                     "RETURN actor.name as actor, collect(actorMovies.title) as movies", {"name": name})
    result = results.single()
    return Response(dumps({"actor": result['actor'],
                           "movies": result['movies']}),
                    mimetype="application/json")


@app.route("/movie/<title>")
def get_actor_by_movie(title):
    """Flask API provides a GET method, which responses with a list of actors
    acted in the movie ``title``.

    :param str title: The movie title as per Neo4j datastore.
    :return flask.Response: List of actor names along with the movie title."""
    db = get_db()
    results = db.run("MATCH (movie: Movie {title: {title}})<-[ACTED_IN]-(actors) "
                     "RETURN movie.title as title, collect(actors.name) as cast", {"title": title})
    result = results.single()
    return Response(dumps({"title": result['title'],
                           "cast": result['cast']}),
                    mimetype="application/json")
