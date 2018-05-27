from flask_admin import Admin
from backend import app
from backend.app import db

from .type_signal_view import TypeSignalView
from .signal_view import SignalView
from .signal_sample_view import SignalSampleView
from .ar_model_view import ARModelView
from .ar_model_coeff_view import ARModelCoeffView
from .device_view import DeviceView

from ..models import TypeSignal, Signal, SignalSample, ARModel, ARModelCoeff, Device

admin = Admin(app, name='Admin', template_mode='bootstrap3')

admin.add_view(TypeSignalView(TypeSignal, db.session))
admin.add_view(SignalView(Signal, db.session))
admin.add_view(SignalSampleView(SignalSample, db.session))

admin.add_view(ARModelView(ARModel, db.session))
admin.add_view(ARModelCoeffView(ARModelCoeff, db.session))

admin.add_view(DeviceView(Device, db.session))