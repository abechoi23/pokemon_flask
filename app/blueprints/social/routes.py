from . import bp as social_bp
# from auth import bp as auth_bp
from flask import render_template, flash, redirect, url_for
from .forms import BlogForm
from .models import User, Post
from flask_login import current_user, login_required


@social_bp.route('/user/<username>')  #add in specific user use <> 
@login_required
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        return redirect(url_for('main.poke_api_call', username=current_user.username))
    posts = user_match.posts
    pokemons = user_match.pokemons
    return render_template('user.jinja', user=user_match,posts=posts, pokemons=pokemons)


@social_bp.route('/blog', methods=['GET','POST'])
@login_required
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        user_id = current_user.id
        p = Post(title=title, body=body, user_id=user_id)
        flash(f'{title} succesfully posted!')
        p.commit()
        return redirect(url_for('social.user', username=current_user.username))
    return render_template('blog.jinja', blog_form=form)

