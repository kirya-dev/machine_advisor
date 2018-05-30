from datetime import datetime

from ..app import db
from .base_mixin import BaseMixin
from .signal_sample import SignalSample


class ARModel(BaseMixin, db.Model):
    __tablename__ = 'ar_models'
    rank = db.Column(db.Integer, nullable=False)
    error = db.Column(db.Float, nullable=True)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    signal_id = db.Column(db.ForeignKey('signals.id'), nullable=False)
    signal = db.relationship('Signal', backref=db.backref(__tablename__, lazy='dynamic'))

    @property
    def steps_before_service(self):
        return self.steps_before(self.signal.type_signal.service)

    @property
    def steps_before_shift(self):
        return self.steps_before(self.signal.type_signal.shift)

    def steps_before(self, value):
        steps = self.signal.signal_samples\
            .filter(SignalSample.is_predict == True, SignalSample.value >= value)\
            .count()  # type: int
        return steps
