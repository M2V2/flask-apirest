__author__ = 'hangvirus'

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from models.user import Person

from models.usuarios import Usuarios
from models.medico import Medico
from models.persona import Persona
from models.turnos import Turnos

connection.setup(['192.168.0.120'], "cqlengine", protocol_version=3)

sync_table(Usuarios)
sync_table(Medico)
# sync_table(Persona)
sync_table(Turnos)
