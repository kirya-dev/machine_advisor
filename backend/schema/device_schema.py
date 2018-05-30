from ..app import ma
from ..models.device import Device
from .signal_schema import SignalSchema


class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device
        fields = ('id', 'name', 'status', 'comment', 'actual_signals', 'created')

    actual_signals = ma.List(ma.Nested(SignalSchema))


device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)
