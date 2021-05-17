from flask import (
    Blueprint, render_template
)

bp = Blueprint("error", __name__)
# handle 404 errors


@bp.app_errorhandler(404)
def urlnotfound(e):
    return render_template("error.html", error=e)

# handle 500 errors


@bp.app_errorhandler(500)
def internalservererror(e):
    return render_template("error.html", error=e)
