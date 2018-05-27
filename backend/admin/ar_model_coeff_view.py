from flask_admin.contrib.sqla import ModelView


class ARModelCoeffView(ModelView):
    page_size = 50
    column_list = ['id', 'ar_model', 'lag_order', 'value', 'updated']
    form_columns = ['ar_model', 'lag_order', 'value']
