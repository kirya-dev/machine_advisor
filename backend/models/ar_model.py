from datetime import datetime
from ..app import db
from .signal_sample import SignalSample
from .base_mixin import BaseMixin


class ARModel(BaseMixin, db.Model):
    __tablename__ = 'ar_models'
    rank = db.Column(db.Integer, nullable=False)
    error = db.Column(db.Float, nullable=True)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    signal_id = db.Column(db.ForeignKey('signals.id'), nullable=False)
    signal = db.relationship('Signal', backref=db.backref(__tablename__, lazy='dynamic'))

    @property
    def endog_samples(self):
        data = self.signal.signal_samples.filter(SignalSample.is_predict == False).all()
        return [x.value for x in data]

    @property
    def predict_samples(self):
        data = self.signal.signal_samples.filter(SignalSample.is_predict == True).all()
        return [x.value for x in data]

    def save_predict_samples(self, rawData):
        # remove old
        self.signal.signal_samples.filter(SignalSample.is_predict == True).delete()
        # add new
        for x in rawData:
            self.signal.signal_samples.append(SignalSample(x, True))
        db.session.commit()
