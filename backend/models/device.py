from .signal import Signal
from ..app import db
from .base_mixin import BaseMixin


class Device(BaseMixin, db.Model):
    __tablename__ = 'devices'
    name = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    status = db.Column(db.Float, nullable=False)

    def actual_signals(self):
        # Get Last Actual signal by created time
        # Distinct equals types
        return self.signals \
            .order_by(Signal.type_signal_id, Signal.created.desc()) \
            .distinct(Signal.type_signal_id)
