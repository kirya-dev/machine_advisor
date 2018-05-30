from ..app import db
from .base_mixin import BaseMixin


class Signal(BaseMixin, db.Model):
    __tablename__ = 'signals'
    comment = db.Column(db.Text, nullable=True)

    device_id = db.Column(db.ForeignKey('devices.id'), nullable=False)
    device = db.relationship('Device', backref=db.backref(__tablename__, lazy='dynamic'))

    type_signal_id = db.Column(db.ForeignKey('type_signals.id'), nullable=False)
    type_signal = db.relationship('TypeSignal', backref=db.backref(__tablename__, lazy='dynamic'))

    def primary_ar_model(self):
        return self.ar_models.first()

    def __str__(self):
        return 'Cигнал {1} №{0}'.format(self.id, self.type_signal.name)
