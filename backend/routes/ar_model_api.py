from flask import jsonify

from statsmodels.tsa.ar_model import AR

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


@app.route('/api/model/<int:id>/analyze')
def analyzeModel(id):
    model = ARModel.query.get(id)
    if model is None:
        raise Exception('Model not found')

    ar_signal = model.signal.endog_samples
    signals_len = len(ar_signal)
    if signals_len < 5:
        raise Exception('Too few "{0}" Endog Data'.format(signals_len))

    ar_model = AR(ar_signal)
    ar_res = ar_model.fit(model.rank)

    predict_res = ar_res.predict(signals_len, signals_len + 30)

    model.signal.save_predict_samples(predict_res)

    return jsonify({
        'signals': ar_signal,
        'predict': list(predict_res)
    })
