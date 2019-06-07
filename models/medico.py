import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Medico(Base):
    cin = columns.Text(primary_key=True)
    nombre_doc = columns.Text()
    horario = columns.Text()
    estado = columns.Boolean()
    especialidad = columns.Text()

    def get_data(self):
        return {
            'cin': self.cin,
            'nombre_doc': self.nombre_doc,
            'horario': self.horario,
            'estado': self.estado,
            'especialidad': self.especialidad
        }