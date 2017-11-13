class Config(object):
    """
    Common Configurations
    """

    # Put any configurations here so that they are common across all environments


class DevelopmentConfig(Config):
    """
    Development Configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production Configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}