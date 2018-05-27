from datetime import datetime
from ..app import db


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return '#{0}'.format(self.id)
