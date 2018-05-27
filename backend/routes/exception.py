from flask import render_template
from . import app


@app.errorhandler(Exception)
def handle_exception(ex):
    app.logger.exception(ex)
    return render_template('exception.html', message=ex)
