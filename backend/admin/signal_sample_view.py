from flask_admin.contrib.sqla import ModelView


class SignalSampleView(ModelView):
    page_size = 50
    can_create = False
    can_delete = False
    can_edit = False
    column_list = ['id', 'signal', 'value', 'is_predict', 'created']
    form_columns = ['signal', 'value', 'is_predict']
