from ..app import db
from .base_mixin import BaseMixin


class ARModelCoeff(BaseMixin, db.Model):
    __tablename__ = 'ar_model_coeffs'
    lag_order = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)

    ar_model_id = db.Column(db.ForeignKey('ar_models.id'), unique=True, nullable=False)
    ar_model = db.relationship('ARModel', backref=db.backref(__tablename__, lazy='dynamic'))

