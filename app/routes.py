# from flask import render_template, flash, redirect
# from app import app, db
# from app.forms import RegisterForm, SignInForm, BlogForm, PokemonForm
# from app.models import User, Post, Pokemon
# from flask_login import current_user, login_user, logout_user, login_required
# import requests
# import random


# @app.route('/about')
# def about():
#     return render_template('about.jinja')


# @app.route('/register', methods=['GET','POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         email = form.email.data
#         password = form.password.data
#         u = User(username=username, email=email, password_hash='')
#         user_match = User.query.filter_by(username=username).first()
#         email_match = User.query.filter_by(email=email).first()
#         if user_match:
#             flash(f'Username {username} already exists, try again.')
#             return redirect('/register')
#         elif email_match:
#             flash(f'Email {email} already exists, try again')    
#             return redirect('/register')
#         else:
#             u.hash_password(password)
#             u.commit()
#                 # db.session.add(u)
#                 # db.session.commit()
#             flash(f'Request to register {username} successful')
#             return redirect('/')
#     return render_template('register.jinja', form=form)


# @app.route('/signin', methods=['GET','POST'])
# def signin():
#     form = SignInForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         user_match = User.query.filter_by(username=username).first()
#         if not user_match or not user_match.check_password(password):
#             flash(f'Username or Password was incorrect, try again.')
#             return redirect('/signin')
#         flash(f'{username} succesfully signed in!')
#         login_user(user_match, remember=False)
#         return redirect('/')
#     return render_template('signin.jinja',sign_in_form=form)


# @login_required
# @app.route('/signout')
# def signout():
#     logout_user()
#     return redirect('/')


# @app.route('/blog', methods=['GET','POST'])
# @login_required
# def blog():
#     form = BlogForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         body = form.body.data
#         user_id = current_user.id
#         p = Post(title=title, body=body, user_id=user_id)
#         # db.session.add(u)
#         # db.session.commit()
#         flash(f'{title} succesfully posted!')
#         p.commit()
#     return render_template('blog.jinja', blog_form=form)


# @app.route('/user/<username>')  #add in specific user use <> 
# @login_required
# def user(username):
#     user_match = User.query.filter_by(username=username).first()
#     if not user_match:
#         return redirect('/')
#     posts = user_match.posts
#     pokemons = user_match.pokemons
#     return render_template('user.jinja', user=user_match,posts=posts, pokemons=pokemons)

# @app.route('/', methods=['GET','POST'])
# def poke_api_call():
#     form = PokemonForm()
#     random_number = random.randint(1, 151)
#     url = f'https://pokeapi.co/api/v2/pokemon/{random_number}/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         pokemon_image = data['sprites']['other']['official-artwork']['front_default']
#         types = data['types']
#         types = list(map(lambda x: x['type']['name'], types))
#         pokemon_name = data['name'].title()
#         pokemon_type = ', '.join(types).title()
#         pokemon_weight = data['weight'] / 10
#         pokemon_abilities = ', '.join([a['ability']['name'].title() for a in data['abilities']])
#     if form.validate_on_submit():
#         flash(f'{pokemon_name} succesfully caught!')
#         p = Pokemon(pokemon_name=pokemon_name, pokemon_type=pokemon_type, pokemon_weight=pokemon_weight, pokemon_abilities=pokemon_abilities, user_id=current_user.id)
#         p.commit() 
#     return render_template('index.jinja',pokemon_name=pokemon_name, pokemon_type=pokemon_type, pokemon_weight=pokemon_weight, pokemon_abilities=pokemon_abilities, pokemon_image=pokemon_image, form=form)
