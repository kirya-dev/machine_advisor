from sqlalchemy_utils import force_auto_coercion

from .device import Device
from .type_signal import TypeSignal
from .signal import Signal
from .signal_sample import SignalSample
from .ar_model import ARModel
from .ar_model_coeff import ARModelCoeff

force_auto_coercion()
