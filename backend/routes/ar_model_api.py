from ..models.ar_model import ARModel
from ..app import app
from ..schema.ar_model_schema import ar_model_schema, ar_models_schema


@app.route('/api/models')
def models():
    all = ARModel.query.all()
    return ar_models_schema.jsonify(all)


@app.route('/api/model/<int:id>')
def model(id):
    model = ARModel.query.get(id)
    return ar_model_schema.jsonify(model)
