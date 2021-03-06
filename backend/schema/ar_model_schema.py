from ..app import ma
from ..models.ar_model import ARModel
from ..models.ar_model_coeff import ARModelCoeff


class ARModelCoeffSchema(ma.ModelSchema):
    class Meta:
        model = ARModelCoeff
        fields = ('id', 'value')


class ARModelSchema(ma.ModelSchema):
    class Meta:
        model = ARModel
        fields = ('id', 'rank', 'error', 'steps_before_service', 'steps_before_shift', 'created')


ar_model_schema = ARModelSchema()
ar_models_schema = ARModelSchema(many=True)
