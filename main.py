__author__ = 'filipe'

from flask import Flask
from flask import render_template
from summoner import Summoner

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    s = Summoner()
    data = s.grab_profile()
    rg_data = s.grab_recent_games(data['gravelordnito']['id'])
    m_data = s.grab_masteries(data['gravelordnito']['id'])
    r_data = s.grab_runes(data['gravelordnito']['id'])
    return render_template('index.html', data=[data, m_data, r_data, rg_data])


@app.route('/sample/', methods=['GET'])
@app.route('/sample/<arg>', alias=True, methods=['GET'])
def sample(arg=None):
    if arg is None:
        arg = 1

    return render_template('sample.html', data=arg)


@app.route('/wat')
def youdoing():
    return 'blank page :)'


@app.errorhandler(403)
def forbidden(error):
    return 'Stap or exhaust!'

@app.errorhandler(404)
def page_not_found(error):
    return 'Page mia'

@app.errorhandler(500)
def internal_server(error):
    return 'wat'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
