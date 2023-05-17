"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User, Post

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
    update_user.first_name = request.form['first_name']
    update_user.last_name = request.form['last_name']
    update_user.image_url = request.form['image_url']

    db.session.add(update_user)
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

# Posts routes



@app.route('/post/<int:user_id>/new')
def new_post_form(user_id):
    """shows form to add a post"""
    user = User.query.get_or_404(user_id)
    return render_template('post_form.html', user=user)

@app.route('/post/<int:user_id>/new', methods=["POST"])
def make_post(user_id):
    # user = User.query.get_or_404(user_id)
    # title = request.form["post_title"]
    # content = request.form["post_content"]
   
   

    # new_post = Post(title=title, content=content, user_i=user)

    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['post_title'],
                    content=request.form['post_content'],
                    user=user)
                    # ^

    db.session.add(new_post)    
    db.session.commit()

    return redirect(f"/{user_id}")

@app.route('/<int:post_id>/new_post')
def show_post(post_id):  
    # user = User.query.get_or_404(user_id)
    # print(user)
    post = Post.query.get_or_404(post_id)
    return render_template('new_post.html', post=post)

@app.route('/all_posts')
def show_all_posts():
    posts = Post.query.order_by(Post.title.desc()).limit(5).all()
    return render_template('all_p.html', posts=posts)
    
@app.route('/post/<int:post_id>/edit')
def posts_edit(post_id):
    """Show a form to edit an existing post"""

    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)

    # new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    # db.session.add(new_user)
    # db.session.commit()

    # return redirect(f"/{new_user.id}")
@app.route('/post/<int:post_id>/edit', methods=['POST'])
def update_post(post_id):
    update_post = Post.query.get_or_404(post_id)
    update_post.title = request.form['title']
    update_post.content = request.form['content']
    # update_user.image_url = request.form['image_url']

    db.session.add(update_post)
    db.session.commit()

    return redirect(f"/{post_id}/new_post")



    