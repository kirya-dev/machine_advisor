from sqlalchemy_utils import force_auto_coercion

from .device import Device as _Device
from .type_signal import TypeSignal as _TypeSignal
from .signal import Signal as _Signal
from .signal_sample import SignalSample as _SignalSample
from .ar_model import ARModel as _ARModel
from .ar_model_coeff import ARModelCoeff as _ARModelCoeff

force_auto_coercion()
