from flask import jsonify
from . import bp as api_bp
from app.blueprints.social.models import Post, User, Pokemon

@api_bp.get('/pokemons')
def api_pokemons():
    result = []
    pokemons = Pokemon.query.all()
    for pokemon in pokemons:
        result.append({
            'name': pokemon.pokemon_name,
            'type': pokemon.pokemon_type,
            'timestamp': pokemon.timestamp,
            'user_id': pokemon.user_id
        })
    return jsonify(result)

@api_bp.route('/pokemons/<id>', methods=['GET'])
def api_pokemon(id):
    pokemon = Pokemon.query.get(int(id))
    return jsonify({
        'name': pokemon.pokemon_name,
        'type': pokemon.pokemon_type,
        'timestamp': pokemon.timestamp,
        'user_id': pokemon.user_id
    })


@api_bp.get('/posts')
def api_posts():
    result = []
    posts = Post.query.all()
    for post in posts:
        result.append({
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp,
            'user_id': post.user_id
        })
    return jsonify(result)


@api_bp.route('/post/<id>', methods=['GET']) #Same as above route['get'] and .get
def api_post(id):
    post = Post.query.get(int(id))
    return jsonify({
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp,
            'user_id': post.user_id
        })


@api_bp.get('/user_posts/<username>')
def api_user_posts(username):
    result = []
    user = User.query.filter_by(username=username).first()
    for post in user.posts:
        result.append({
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp,
            'user_id': post.user_id
        })
    return jsonify(result)


@api_bp.get('/user_pokemons/<username>')
def api_user_pokemons(username):
    result = []
    user = User.query.filter_by(username=username).first()
    for pokemon in user.pokemons:
        result.append({
            'name': pokemon.pokemon_name,
            'type': pokemon.pokemon_type,
            'timestamp': pokemon.timestamp,
            'user_id': pokemon.user_id
        })
    return jsonify(result)
