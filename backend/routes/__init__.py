from flask import render_template
from ..app import app
from ..routes import ar_model_api, device_api, exception  # noqa


@app.route('/')
def index():
    return render_template('index.html', name='Hey')
