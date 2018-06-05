from ..app import db
from .base_mixin import BaseMixin
from .signal import Signal


class Device(BaseMixin, db.Model):
    __tablename__ = 'devices'
    name = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    status = db.Column(db.Float, nullable=False, default=0)

    def estimate_signals(self):
        for signal in self.actual_signals():
            ar_model = signal.primary_ar_model
            if ar_model is not None:
                ar_model.estimate()
            else:
                raise Exception('Signal "{0}" has no ARModel. Please Add in Admin.'.format(signal))

        db.session.commit()

    def actual_signals(self):
        # Get Last Actual signal by created time
        # Distinct equals types
        return self.signals \
            .order_by(Signal.type_signal_id, Signal.created.desc()) \
            .distinct(Signal.type_signal_id)

    def __str__(self):
        return '#{0} {1}'.format(self.id, self.name)
