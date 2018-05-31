from datetime import datetime

from statsmodels.tsa.ar_model import AR

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

    def estimate(self):
        ar_signal = self.signal.endog_samples
        signals_len = len(ar_signal)
        if signals_len < 2*self.rank:
            raise Exception('Too few "{0}" Endog Data, required {1} for signal "{2}"'.
                            format(signals_len, 2*self.rank, self.signal))

        ar_model_ = AR(ar_signal)
        ar_res = ar_model_.fit(self.rank)

        predict_res = ar_res.predict(signals_len, signals_len + 30)

        self.signal.save_predict_samples(predict_res)
