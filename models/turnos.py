import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Turnos(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    nro_turno = columns.Text(default='AAA')
    fecha = columns.Text()
    hora = columns.Text()
    medico_cin = columns.Text()
    persona_cin = columns.Text()
    estado = columns.Boolean(default=True)

    def get_data(self):
        return {
            'id': str(self.id),
            'nro_turno': self.nro_turno,
            'fecha': self.fecha,
            'hora': self.hora,
            'medico_cin': self.medico_cin,
            'persona_cin': self.persona_cin,
            'estado': self.estado
        }