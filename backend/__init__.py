# this necessary to prevent circular import issues
from backend.app import app, manager  # noqa
from backend import models  # noqa
from backend.admin import admin  # noqa
from backend import routes  # noqa
