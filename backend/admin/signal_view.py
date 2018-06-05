from flask_admin.contrib.sqla import ModelView
from flask_admin.form import Select2Field
from flask_admin.model import InlineFormAdmin, BaseModelView

from flask_wtf.file import FileField
from wtforms_components import fields
from wtforms_alchemy import ModelForm, ModelFormField, ModelUpdateForm

from backend.app import db
from backend.models.device import Device
from backend.models.signal import Signal
from backend.models.signal_sample import SignalSample


class SignalSampleForm(InlineFormAdmin):
    form_columns = ('id', 'value')


class SignalForm(ModelForm):
    class Meta:
        model = Signal

    inline_models = [SignalSampleForm(SignalSample)]

    column_list = ('device', 'comment')
    # device = ModelFormField(widget=Select2Field)
    # inline_models = ['']
    # comment =
    file = FileField()


class SignalView(ModelView):
    page_size = 50
    column_list = ['id', 'device', 'type_signal', 'comment', 'created']
    form_columns = ['device', 'type_signal', 'comment']

    # form = SignalForm
    inline_models = [SignalSampleForm(SignalSample)]

    # list_template = '/admin/signal/list.html'
