from ..app import db
from .base_mixin import BaseMixin


class TypeSignal(BaseMixin, db.Model):
    __tablename__ = 'type_signals'
    name = db.Column(db.String(255), nullable=False)
    service = db.Column(db.Float, nullable=False)
    shift = db.Column(db.Float, nullable=False)

    def __str__(self):
        return '#{0} {1}'.format(self.id, self.name)
