from ..app import db
from .base_mixin import BaseMixin


class Device(BaseMixin, db.Model):
    __tablename__ = 'devices'
    name = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    status = db.Column(db.Float, nullable=False)
