"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User, Post, PostTag, Tag

# from models import db, connect_db, User, Post

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

@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Remove a post from post display page"""
    
    post = Post.query.get_or_404(post_id)
    print(post)
    
    db.session.delete(post)
    db.session.commit()
    
    return redirect("/")    

  
@app.route('/tags_list')
def show_tags():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags)

@app.route('/tags')
def get_tags_form():
    """Show form to create new tags"""
    tag = Tag.query.all()
    return render_template('tag_form.html', tag=tag)

@app.route('/new_tag', methods=['POST'])
def create_tag():
    name = request.form["name"]

    new_tag = Tag(name=name)

    db.session.add(new_tag)
    db.session.commit()

    return redirect('/')




    return redirect(f"/{new_user.id}")

@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag_detail.html', tag=tag)




# @app.route('/tags/<int:tag_id>')
# def tags_show(tag_id):
#     """Show a page with info on a specific tag"""

#     tag = Tag.query.get_or_404(tag_id)
#     return render_template('tags/show.html', tag=tag)




# many-many seems to be set up right, but it still confuses me. App is mostly functional, got tags to render, and 
# on a list of links and can view tag details when clicked, still can't wrap my head around how the 3 tables are linked, have vague idea. 
#Haven't found the vids on many-to-many all that clear, not seeing how
# the relationsips work in app setting, assignment caused more confusion then helped with many-to-many. All else was a great
# learning experience, parts I and II were awesome. Don't want to fall behind so moving on for now. 