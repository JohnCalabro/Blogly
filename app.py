"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User

app = Flask(__name__)

app.debug = True

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

@app.route('/')
def list_pets():
    """Shows list of all users in db"""
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/users/new')
def show_user_form():
    """Renders form to enter new user"""
    users = User.query.all()
    return render_template('form.html', users=users)

@app.route('/users/new', methods=['POST'])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    # hunger = int(hunger) if hunger else None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/{new_user.id}")

@app.route('/<int:user_id>')
def show_pet(user_id):
    """Show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)


@app.route('/<int:user_id>/edit')
def show_edit_form(user_id):
     user = User.query.get_or_404(user_id)
     return render_template('update.html', user=user)

@app.route('/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    update_user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/<int:user_id>/delete', methods=['POST'])
def remove_user(user_id):
    """Show details about a single user"""
    # user = User.query.get_or_404(user_id)
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")


