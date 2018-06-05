from flask_admin.contrib.sqla import ModelView


class DeviceView(ModelView):
    page_size = 50
    column_list = ['id', 'name', 'status', 'comment', 'updated']
    form_columns = ['name', 'comment']
