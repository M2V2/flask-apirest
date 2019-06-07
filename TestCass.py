from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from flask import Flask
from models.user import Person
from models.usuarios import Usuarios
from models.medico import Medico
from models.persona import Persona
from models.turnos import Turnos
from models.especialidad import Especialidad
from views.api import api

KEYSPACE = "turnos"


def create_app():
    app = Flask(__name__)

    app.debug = True
    app.register_blueprint(api)

    cluster = Cluster(['192.168.0.120', '192.168.0.121', '192.168.0.122'])
    session = cluster.connect()
    # session.execute(
    #     """
    #     CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 };
    #     """ % KEYSPACE)
    session = cluster.connect(keyspace=KEYSPACE)

    return app


app = create_app()

if __name__ == '__main__':
    connection.setup(['192.168.0.120'], "cqlengine", protocol_version=3)
    #sync_table(Person)
    sync_table(Usuarios)
    sync_table(Medico)
    sync_table(Especialidad)
    sync_table(Turnos)
    app.run(host="0.0.0.0", port=9042)
