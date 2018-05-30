from ..app import db
from .base_mixin import BaseMixin


class SignalSample(BaseMixin, db.Model):
    __tablename__ = 'signal_samples'
    value = db.Column(db.Float, nullable=False)
    is_predict = db.Column(db.Boolean, nullable=False, default=False)

    signal_id = db.Column(db.ForeignKey('signals.id'), nullable=False)
    signal = db.relationship('Signal', backref=db.backref(__tablename__, lazy='dynamic'))

    def __init__(self, value=0, is_predict=False):
        self.value = value
        self.is_predict = is_predict

    def __str__(self):
        return '#{0} {1}'.format(self.id, self.value)

