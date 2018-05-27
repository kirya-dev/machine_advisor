from flask_admin.contrib.sqla import ModelView


class SignalView(ModelView):
    page_size = 50
    column_list = ['id', 'device', 'type_signal', 'comment', 'created']
    form_columns = ['device', 'type_signal', 'comment']
