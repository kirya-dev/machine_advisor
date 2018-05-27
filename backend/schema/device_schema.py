from backend.app import ma
from backend.models import Device, TypeSignal


class TypeSignalSchema(ma.ModelSchema):
    class Meta:
        model = TypeSignal
        fields = ('id', 'name', 'signals')


class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device
        fields = ('id', 'name', 'status', 'comment', 'type_signals', 'created')

    type_signals = ma.Nested(TypeSignalSchema)


device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)
