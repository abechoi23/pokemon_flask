from . import bp as main_bp
# from auth import bp as auth_bp
from flask import render_template, flash
from .forms import PokemonForm
from app.blueprints.social.models import Pokemon
from flask_login import current_user
import requests
import random

@main_bp.route('/', methods=['GET','POST'])
def poke_api_call():
    form = PokemonForm()
    random_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{random_number}/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_image = data['sprites']['other']['official-artwork']['front_default']
        types = data['types']
        types = list(map(lambda x: x['type']['name'], types))
        pokemon_name = data['name'].title()
        pokemon_type = ', '.join(types).title()
        pokemon_weight = data['weight'] / 10
        pokemon_abilities = ', '.join([a['ability']['name'].title() for a in data['abilities']])
    if form.validate_on_submit():
        flash(f'{pokemon_name} succesfully caught!')
        p = Pokemon(pokemon_name=pokemon_name, pokemon_type=pokemon_type, pokemon_weight=pokemon_weight, pokemon_abilities=pokemon_abilities, user_id=current_user.id)
        p.commit() 
    return render_template('index.jinja',pokemon_name=pokemon_name, pokemon_type=pokemon_type, pokemon_weight=pokemon_weight, pokemon_abilities=pokemon_abilities, pokemon_image=pokemon_image, form=form)


@main_bp.route('/about')
def about():
    return render_template('about.jinja')