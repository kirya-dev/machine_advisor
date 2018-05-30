from datetime import datetime
from ..app import db
from .base_mixin import BaseMixin


class ARModel(BaseMixin, db.Model):
    __tablename__ = 'ar_models'
    rank = db.Column(db.Integer, nullable=False)
    error = db.Column(db.Float, nullable=True)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    signal_id = db.Column(db.ForeignKey('signals.id'), nullable=False)
    signal = db.relationship('Signal', backref=db.backref(__tablename__, lazy='dynamic'))
