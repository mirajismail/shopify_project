class Config(object):
  """
  Common configurations
  """

  DEBUG = True

class DevelopmentConfig(Config):
  """
  Development configurations
  """

  SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
  """
  Production configurations
  """

  DEBUG = False

app_config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig
}
