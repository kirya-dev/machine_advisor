from ..app import db
from .base_mixin import BaseMixin
from .signal_sample import SignalSample


class Signal(BaseMixin, db.Model):
    __tablename__ = 'signals'
    comment = db.Column(db.Text, nullable=True)

    device_id = db.Column(db.ForeignKey('devices.id'), nullable=False)
    device = db.relationship('Device', backref=db.backref(__tablename__, lazy='dynamic'))

    type_signal_id = db.Column(db.ForeignKey('type_signals.id'), nullable=False)
    type_signal = db.relationship('TypeSignal', backref=db.backref(__tablename__, lazy='dynamic'))

    @property
    def primary_ar_model(self):
        return self.ar_models.first()  # TODO

    @property
    def endog_samples(self):
        data = self.signal_samples\
            .filter(SignalSample.is_predict == False)\
            .all()
        return [x.value for x in data]

    @property
    def predict_samples(self):
        data = self.signal_samples\
            .filter(SignalSample.is_predict == True)\
            .all()
        return [x.value for x in data]

    def save_predict_samples(self, rawData):
        # remove old
        self.signal_samples.filter(SignalSample.is_predict == True).delete()
        # add new
        for x in rawData:
            self.signal_samples.append(SignalSample(x, True))

    def __str__(self):
        return 'Cигнал {1} №{0}'.format(self.id, self.type_signal.name)
