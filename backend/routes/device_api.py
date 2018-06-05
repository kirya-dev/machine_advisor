from flask import jsonify

from ..app import app
from ..models.device import Device
from ..schema.device_schema import device_schema, devices_schema


@app.route('/api/devices')
def devices():
    _devices = Device.query.order_by(Device.created.asc()).all()
    return devices_schema.jsonify(_devices)


@app.route('/api/device/<int:id>')
def device(id):
    _device = Device.query.get(id)
    return device_schema.jsonify(_device)


@app.route('/api/device/<int:id>/analyze')
def analyzeDevice(id):
    _device = Device.query.get(id)
    if _device is None:
        raise Exception('Device not found')

    _device.estimate_signals()

    return jsonify({'status': 200})
