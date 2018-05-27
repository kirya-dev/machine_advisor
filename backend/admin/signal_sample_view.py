from flask_admin.contrib.sqla import ModelView


class SignalSampleView(ModelView):
    page_size = 50
    column_list = ['id', 'signal', 'value', 'is_predict', 'created']
    form_columns = ['signal', 'value', 'is_predict']
