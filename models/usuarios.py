from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Usuarios(Base):
    user = columns.Text(primary_key=True)
    password = columns.Text()
    estado = columns.Boolean()
    token_auth = columns.Text()

    def get_data(self):
        return {
            'user': self.user,
            'password': self.password,
            'estado': self.estado,
            'token_auth': self.token_auth
        }