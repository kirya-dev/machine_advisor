from flask import jsonify

from ..app import app
from ..models.device import Device
from ..schema.device_schema import device_schema, devices_schema


@app.route('/api/devices')
def devices():
    all = Device.query.all()
    return devices_schema.jsonify(all)


@app.route('/api/device/<int:id>')
def device(id):
    obj = Device.query.get(id)
    return device_schema.jsonify(obj)


@app.route('/api/device/<int:id>/analyze')
def analyzeDevice(id):
    _device = Device.query.get(id)
    if _device is None:
        raise Exception('Device not found')

    _device.estimateSignals()

    return jsonify({'status': 200})
