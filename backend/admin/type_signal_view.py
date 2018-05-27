from flask_admin.contrib.sqla import ModelView


class TypeSignalView(ModelView):
    page_size = 50
    column_list = ['id', 'name', 'service', 'shift', 'created']
    form_columns = ['name', 'service', 'shift']
