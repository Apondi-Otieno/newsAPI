NEWS_API_KEY='< 9c6c93421cdc4624835c17adb457d9e7>'

class Config:
    '''
    General configuration parent class
    '''
    pass

class Config:
    '''
    General configuration parent class
    '''
  
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=9c6c93421cdc4624835c17adb457d9e7'
    NEWS_SOURCE_BASE_URL='https://newsapi.org/v2/top-headlines/sources?apiKey=9c6c93421cdc4624835c17adb457d9e7'
    NEWS_API_KEY =os.environ.get('9c6c93421cdc4624835c17adb457d9e7')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True