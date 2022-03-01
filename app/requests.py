from app import app
import urllib.request,json
from .models import source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the base url for the news api
base_url=app.config['NEWS_API_BASE_URL']