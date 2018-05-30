from ..app import ma
from ..models.device import Device
from ..models.signal import Signal
from ..models.type_signal import TypeSignal
from .ar_model_schema import ARModelSchema


class TypeSignalSchema(ma.ModelSchema):
    class Meta:
        model = TypeSignal
        fields = ('id', 'name', 'service', 'shift')


class SignalSchema(ma.ModelSchema):
    class Meta:
        model = Signal
        fields = ('id', 'created', 'comment', 'type_signal', 'primary_ar_model')

    type_signal = ma.Nested(TypeSignalSchema)
    primary_ar_model = ma.Nested(ARModelSchema)


class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device
        fields = ('id', 'name', 'status', 'comment', 'actual_signals', 'created')

    actual_signals = ma.List(ma.Nested(SignalSchema))


device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)
