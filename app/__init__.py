from flask import Flask
from config import config

app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .routes import main
    from .routes import weixin
    app.register_blueprint(main.bp, url_prefix='/')
    # app.register_blueprint(weixin.bp, url_prefix='/weixin')
    app.add_url_rule(
        '/weixin',
        view_func=weixin.view.WechatView.as_view('weixin'),
        methods=['GET', 'POST']
    )
    return app
