from flask_admin.contrib.sqla import ModelView


class ARModelView(ModelView):
    page_size = 50
    column_list = ['id', 'rank', 'signal', 'error', 'created', 'updated']
    form_columns = ['signal', 'rank']
