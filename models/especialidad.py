import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'hangvirus'


class Especialidad(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    especialidad = columns.Text()

    def get_data(self):
        return {
            'id': str(self.id),
            'especialidad': self.especialidad,
        }