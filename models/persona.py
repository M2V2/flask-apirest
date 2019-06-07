import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Persona(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    nombre_pers = columns.Text()
    ci = columns.Text()
    fecha_nac = columns.Text()
    sexo = columns.Text()
    telefono = columns.Text()
    estado_pers = columns.Text()

    def get_data(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre_pers,
            'ci': self.ci,
            'fecha_nac': self.fecha_nac,
            'sexo': self.sexo,
            'telefono': self.telefono,
            'estado': self.estado_pers
        }