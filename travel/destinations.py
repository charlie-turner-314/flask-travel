import sqlalchemy
from travel.auth import login
from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
)

from flask_login import login_required, current_user

from .models import Destination,Comment
from .forms import *
from . import db

#create a blueprint
bp = Blueprint('destination', __name__, url_prefix='/destinations')

@bp.route('/')
def destinations():
    return redirect(url_for('main.index'))

#create a page that will show the details fo the destination
@bp.route('/<id>') 
def show(id): 
    destination = Destination.query.filter_by(id=id).first()
    cform = CommentForm() # create the comment form and passit to render_template
    #in the html this is access as a varible named form
    return render_template('destinations/show.html', destination=destination, form=cform)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    form = DestinationForm()
    print('Method type: ', request.method)
    if form.validate_on_submit():
        destination = Destination(name=form.name.data,
                description=form.description.data,
                image=form.image.data,
                currency=form.currency.data)
        # add the object to the db session
        db.session.add(destination)
        # commit to the database
        db.session.commit()
        return redirect(url_for('destination.create'))
    return render_template('destinations/create.html', form=form)

@bp.route('/deletedestination', methods = ['GET', 'POST'])
@login_required
def delete():
    destinationId = request.args.get('destination')
    destination_obj = Destination.query.filter_by(id=destinationId).first()
    # remove the destination instance from the database session
    db.session.delete(destination_obj)
    db.session.commit()
    # redirect the user to the main page
    return redirect(url_for('main.index'))


@bp.route('/<destination>/comment', methods = ['GET', 'POST'])  
@login_required
def comment(destination):  
    #get the destination object associated to the page and the comment
    destination_obj = Destination.query.filter_by(id=destination).first() 
    #here the form is created 
    form = CommentForm()  
    if form.validate_on_submit():  #this is true only in case of POST method
        comment = Comment(text=form.text.data, 
                destination=destination_obj, user=current_user)
        db.session.add(comment)
        db.session.commit()
        print("Comment posted by the user:", form.text.data)  
    
    # in any case we go back to the same page. 
    return redirect(url_for('destination.show', id=destination))
