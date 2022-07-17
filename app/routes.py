from flask import Blueprint, render_template, redirect, request
import requests
from datetime import datetime
from .utils.helpers import tdelta
import os
news = Blueprint('news', __name__)


@news.route('/')
def home():

    params = {
        'q': 'India',
        'from': datetime.now().strftime('%Y-%m-%d'),
        'language': 'en',
        'sortBy': 'publishedAt',
        'apiKey': os.environ.get('FLASK_NEWS_API_KEY'),
    }
    news = requests.get(url=os.environ.get(
        'FLASK_NEWS_URL')+'everything', params=params)

    data = {

        'news': news.json(),
        'date': tdelta,

    }

    return render_template('home.html', **data)


@news.route('/search/', methods=['GET'])
def search():

    q = request.args['q'] if request.args['q'] is not None else 'India'

    params = {
        'q': q.replace(" ","+"),
        'sortBy': request.args['sortby'],
        'language': 'en',
        'from': datetime.strptime(request.args['from_date'], '%Y-%m-%d') if request.args['from_date'] else datetime.now().strftime('%Y-%m-%d'),
        'to': datetime.strptime(request.args['to_date'], '%Y-%m-%d') if request.args['to_date'] else datetime.now().strftime('%Y-%m-%d'),
        'apiKey': os.environ.get('FLASK_NEWS_API_KEY')
    }

    news = requests.get(url=os.environ.get(
        'FLASK_NEWS_URL')+'everything', params=params)

    data = {

        'news': news.json(),
        'date': tdelta,

    }

    return render_template('home.html', **data, search=q)
