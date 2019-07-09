import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    APP_ID = 'wxfb561a**********b'
    SECRET = '19078e44***********'
    REDIS_STORAGE = 'redis://127.0.0.1:6379/0'
    WECHAT_TOKEN = 'wechat_token'
    CODE_PATH = '/home/pi/code/Wechat-public-account-on-Raspberry-Pi/others'


# 生产环境的配置
class ProductionConfig(Config):
    APP_ID = 'wxfb561a**********b'
    SECRET = '19078e44***********'
    REDIS_STORAGE = 'redis://127.0.0.1:6379/0'
    WECHAT_TOKEN = 'wechat_token'
    CODE_PATH = '/home/pi/code/Wechat-public-account-on-Raspberry-Pi/others'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
