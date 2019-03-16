# neo4j-python-movies
Neo4j application with Flask using the neo4j-python-driver

### Pre-requisites
The setup was carried using the below environment
* Ubuntu 16.04 
* Python3:
  ``sudo apt-get install python3``
* Python3 dev and virtualenv tools:
``sudo apt-get install python3-dev python3-virtualenv``
* Download & Install [Neo4j Server](http://neo4j.com/download)

### Stack

* [neo4j-python-driver](https://github.com/neo4j/neo4j-python-driver) - Neo4j Bolt Driver for Python
* [Flask](http://flask.pocoo.org/) - Python microframework based on Werkzeug, Jinja 2 and good intentions.
* Neo4j-Server

### Setup
Make sure your Neo4j-Server is up and running
```
$ sudo service neo4j status
```

Clone the repository into your local environment
```
$ git clone https://github.com/vernekarp/neo4j-python-movies.git
$ cd neo4j-python-movies
```

Modify the file ``etc/neo4jnode.secrets`` to provide your neo4j access credentials and save it.
Similar to the format as shown below
```
$ cat etc/neo4jnode.secrets
{
  "uri": "bolt://localhost:7687",
  "username": "neo4j",
  "password": "your-password"
}
```

Setup with [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs) so we don't break any other Python stuff you have on your machine. 
After you've got that installed let's setup an environment for our app:

```
$ python3.5 -m venv --clear  venv
$ source venv/bin/activate
```

Install the app and its dependencies:
```
(venv)$ pip install .
```

And finally start the Flask server.
```
(venv)$ neo4jmovies
 * Serving Flask app "neo4jmoviesapi.flask_api" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!

```

Navigate and access the respective API and its response:
* Actor (http://localhost:5000/actor/full-name):
  * [Tom Hanks](http://localhost:5000/actor/Tom%20Hanks)
    ```
    {
      "actor": "Tom Hanks", 
      "movies": [
        "Charlie Wilson's War", 
        "Apollo 13", 
        "That Thing You Do", 
        "The Polar Express", 
        "The Green Mile", 
        "A League of Their Own", 
        "The Da Vinci Code", 
        "Cast Away", 
        "Cloud Atlas", 
        "Sleepless in Seattle", 
        Joe Versus the Volcano", 
        "You've Got Mail"
      ]
    }
    ```
  * [Robin Williams](http://localhost:5000/actor/Robin%20Williams)
    ```
    {
      "movies": [
        "What Dreams May Come", 
        "The Birdcage", 
        "Bicentennial Man"
       ], 
       "actor": "Robin Williams"
    }
    ```
* Movie (http://localhost:5000/movie/title): 
  * [Apollo 13](http://localhost:5000/movie/Apollo%2013)
    ```
    {
      "title": "Apollo 13",
      "cast": [
        "Ron Howard",
        "Tom Hanks",
        "Bill Paxton",
        "Kevin Bacon",
        "Gary Sinise",
        "Ed Harris"
      ]
    }
    ```
  * [Bicentennial Man](http://localhost:5000/movie/Bicentennial%20Man)
    ```
    {
      "title": "Bicentennial Man",
      "cast": [
        "Oliver Platt",
        "Chris Columbus",
        "Robin Williams"
      ]
    }
    ```