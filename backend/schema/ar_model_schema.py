from backend.app import ma
from backend.models import ARModel, Signal, ARModelCoeff


class ARModelCoeffSchema(ma.ModelSchema):
    class Meta:
        model = ARModelCoeff
        fields = ('id', 'value')


class SignalSchema(ma.ModelSchema):
    class Meta:
        model = Signal
        fields = ('id', 'created', 'comment')


class ARModelSchema(ma.ModelSchema):
    class Meta:
        model = ARModel
        fields = ('id', 'rank', 'error', 'signal', 'endog_samples', 'predict_samples', 'created')

    signal = ma.Nested(SignalSchema)


ar_model_schema = ARModelSchema()
ar_models_schema = ARModelSchema(many=True)
