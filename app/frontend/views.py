from flask import Blueprint, render_template

frontend = Blueprint(
    'frontend', __name__, template_folder='templates', static_folder='static')


personajes = [
    {
        'nombre': 'gerald',
        'arma': 'pistola'
    },
    {
        'nombre': 'esen',
        'arma': 'hacha'
    }
]


@frontend.route('/')
def index():
    personajes.append({'nombre': 'carlos', 'arma': 'cuchillo'})

    return render_template(
        'index.html',
        entidad='Tsathotugga',
        nombre='Gerald',
        amigos=['pedro', 'esen', 'karel'],
        personajes=personajes
    )


@frontend.route('create')
def create():
    return render_template('create.html')
