from flask import render_template
from . import main
from ..requests import get_sources, get_articles

# Views
@main.route('/')
def index():
    title="the scoop"
    heading="welcome to the illest blog"

    '''
    View root page function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    tech_sources = get_sources('technology')
    
    return render_template('index.html', title=title, heading=heading, general = general_sources, sports = sports_sources, business = business_sources, entertainment = entertainment_sources, tech = tech_sources)
    
    

@main.route('/sources/<id>')
def articles(id):
    articles_title = "Articles"
    read_article = get_articles(id)
    
    '''
        View movie page function that returns the movie details page and its data
    '''
    return render_template("articles.html", id = id, read_article=read_article, articles_title = articles_title )    