import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/snake-head-bieber.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )
    
    bieberqoutes = ['I make mistakes growing up. I\'m not perfect; I\'m not a robot. -Justin Bieber', 'I\'m crazy, I\'m nuts. Just the way my brain works. I\'m not normal. I think differently. -Justin Bieber', 'Friends are the best to turn to when you\'re having a rough day. -Justin Bieber', 'I leave the hip thrusts to Michael Jackson. -Justin Bieber', It's cool when fans spend so much time making things for me. It means a lot. -Justin Bieber']


    return {
        'color': '#00ff00',
        'head': head_url,
        'taunt': random.choice(bieberqoutes)
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    bieberqoutes = ['I make mistakes growing up. I\'m not perfect; I\'m not a robot. -Justin Bieber', 'I\'m crazy, I\'m nuts. Just the way my brain works. I\'m not normal. I think differently. -Justin Bieber', 'Friends are the best to turn to when you\'re having a rough day. -Justin Bieber', 'I leave the hip thrusts to Michael Jackson. -Justin Bieber', It's cool when fans spend so much time making things for me. It means a lot. -Justin Bieber']

    return {
        'taunt': random.choice(bieberqoutes)
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'move': 'north',
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
