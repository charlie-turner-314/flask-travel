import time
from travel.models import Destination
from flask import Blueprint, render_template, url_for, request, session, templating, redirect

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    destinations = Destination.query.all()
    return render_template('index.html', destinations=destinations, epoch=time.time())

# route to allow users to search


@mainbp.route('/search')
def search():
    # get the search string from request
    if request.args['search']:
        dest = "%" + request.args['search'] + '%'
    # use filter and like function to search for matching destinations
        destinations = Destination.query.filter(Destination.name.like(dest)).all()
    # render index.html with few destinations
        return render_template('index.html', destinations=destinations, epoch=time.time())
    else:
        return redirect(url_for('main.index'))
        