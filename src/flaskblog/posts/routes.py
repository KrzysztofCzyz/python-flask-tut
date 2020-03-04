from flask import Blueprint, flash, render_template, redirect, url_for, abort, request
from flask_login import login_required, current_user

from flaskblog import db
from flaskblog.users.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has ben created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post1 = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post1.title, post=post1)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post1 = Post.query.get_or_404(post_id)
    if post1.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post1.title = form.title.data
        post1.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    elif request.method == 'GET':
        form.content.data = post1.content
        form.title.data = post1.title
    return render_template('create_post.html', form=form, title=post1.title, post=post1, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post1 = Post.query.get_or_404(post_id)
    if post1.author != current_user:
        abort(403)
    db.session.delete(post1)
    db.session.commit()
    flash("Your post has been deleted!", 'success')
    return redirect(url_for('main.home'))