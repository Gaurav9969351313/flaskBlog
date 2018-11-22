from flask import Flask, render_template,Blueprint

errorpages = Blueprint('errorpages',__name__)

@errorpages.app_errorhandler(404)
def error_404(error):
    return render_template('errorpages/404.html'), 404


@errorpages.app_errorhandler(403)
def error_403(error):
    return render_template('errorpages/403.html'), 403
