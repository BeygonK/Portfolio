from flask import Blueprint, render_template, request
from .utils.github_api import fetch_user, search_users

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    results = search_users(query)
    return render_template('search.html', results=results)
