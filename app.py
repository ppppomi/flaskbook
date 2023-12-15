from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy를 인스턴스화 한다.
db = SQLAlchemy()

# create_app함수 생성
def create_app():

    # 플라스크 인스턴스(객체) 생성
    app = Flask(__name__)

    from apps.crud import views as crud_views

    # register_blueprint
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # 앱의 config 설정을 한다.
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBs",
        SQLALCHEMY_DATABASE_URI = 
            f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    # SQLAlchemy와 앱을 연계한다.
    db.init_app(app)
    # Migrate와 앱을 연계한다.
    Migrate(app, db)

    return app

    

