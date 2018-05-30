from ..app import ma
from ..models.signal import Signal
from ..models.signal_sample import SignalSample
from ..models.type_signal import TypeSignal
from .ar_model_schema import ARModelSchema


class TypeSignalSchema(ma.ModelSchema):
    class Meta:
        model = TypeSignal
        fields = ('id', 'name', 'service', 'shift')


class SignalSampleSchema(ma.ModelSchema):
    class Meta:
        model = SignalSample
        fields = ('id', 'created', 'value')


class SignalSchema(ma.ModelSchema):
    class Meta:
        model = Signal
        fields = ('id', 'created', 'comment', 'type_signal', 'endog_samples', 'predict_samples', 'primary_ar_model')

    type_signal = ma.Nested(TypeSignalSchema)
    primary_ar_model = ma.Nested(ARModelSchema)


signal_schema = SignalSchema()
signals_schema = SignalSchema(many=True)
