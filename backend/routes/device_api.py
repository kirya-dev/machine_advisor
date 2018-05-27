from ..app import app
from ..models import Device
from ..schema.device_schema import device_schema, devices_schema


@app.route('/api/devices')
def devices():
    all = Device.query.all()
    return devices_schema.jsonify(all)


@app.route('/api/device/<int:id>')
def device(id):
    obj = Device.query.get(id)
    return device_schema.jsonify(obj)
